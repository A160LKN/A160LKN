#!/usr/bin/env python3
"""Общий код в проектах не должен молча расходиться.

Лимиты попыток, хеширование паролей и часть интерфейса скопированы между проектами: так каждый
репозиторий можно клонировать и запустить отдельно. Цена копий — исправление легко внести в одну
и забыть в другой. Этот скрипт сравнивает копии и падает, если они разошлись.

    python3 scripts/check-shared.py              # файлы из ветки main на GitHub
    python3 scripts/check-shared.py --local ..   # рабочие копии рядом: ../birge, ../shop-api, …

Python сравнивается по синтаксическому дереву: комментарии и переносы строк не важны, логика — важна.
Остальные файлы — построчно, кроме строк, отличие которых разрешено (ignore).
"""
from __future__ import annotations

import argparse
import ast
import difflib
import os
import re
import sys
import urllib.request
from pathlib import Path

OWNER = "A160LKN"

CHECKS = [
    {
        "name": "Лимиты попыток входа и регистрации, адрес клиента за прокси",
        "files": ["birge:backend/app/ratelimit.py", "shop-api:app/ratelimit.py"],
    },
    {
        "name": "Хеширование паролей (scrypt)",
        "files": ["birge:backend/app/security.py", "shop-api:app/security.py"],
        "symbols": ["_SCRYPT", "hash_password", "verify_password"],
    },
    {
        "name": "Проверка силы пароля",
        "files": ["birge:backend/app/routers/auth.py", "shop-api:app/routers/auth.py"],
        "symbols": ["COMMON_PASSWORDS", "check_password_strength"],
    },
    {
        "name": "Список популярных паролей — одинаковый в Python и TypeScript",
        "kind": "password-list",
        "files": ["birge:backend/app/routers/auth.py", "kassa-api:src/lib/security.ts"],
    },
    {
        "name": "Хранение токена входа",
        "files": ["birge:frontend/src/auth/token.ts", "shop-web:src/auth/token.ts"],
        "ignore": [r"^const KEY = "],  # у каждого сайта свой ключ в localStorage
    },
    *(
        {"name": f"Интерфейс: {path}", "files": [f"birge:frontend/{path}", f"shop-web:{path}"]}
        for path in ["src/lib/storage.ts", "src/lib/plural.ts", "src/components/Button.tsx",
                     "src/components/Field.tsx", "src/components/Field.module.css", "src/components/States.tsx"]
    ),
]


def fetch(spec: str, local: Path | None) -> str:
    repo, path = spec.split(":", 1)
    if local is not None:
        return (local / repo / path).read_text(encoding="utf-8")
    url = f"https://raw.githubusercontent.com/{OWNER}/{repo}/main/{path}"
    request = urllib.request.Request(url, headers={"User-Agent": "shared-code-check"})
    with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310 — адрес собран из констант
        return response.read().decode("utf-8")


def python_view(source: str, symbols: list[str] | None) -> list[str]:
    """Синтаксическое дерево файла (или только нужных функций и констант) — построчно, для diff."""
    tree = ast.parse(source)
    nodes = tree.body
    if symbols:
        found = {}
        for node in tree.body:
            names = [node.name] if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) else [
                t.id for t in getattr(node, "targets", [getattr(node, "target", None)]) if isinstance(t, ast.Name)]
            for name in names:
                if name in symbols:
                    found[name] = node
        missing = [s for s in symbols if s not in found]
        if missing:
            return [f"<нет в файле: {', '.join(missing)}>"]
        nodes = [found[s] for s in symbols]
    view = []
    for node in nodes:
        # Строки документации не сравниваем: у проектов свои пояснения
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and ast.get_docstring(node):
            node.body = node.body[1:]
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            continue
        view.extend(ast.unparse(node).splitlines())
    return view


def text_view(source: str, ignore: list[str]) -> list[str]:
    patterns = [re.compile(p) for p in ignore]
    return [line.rstrip() for line in source.splitlines() if not any(p.search(line) for p in patterns)]


def password_list(source: str) -> list[str]:
    """Пароли из COMMON_PASSWORDS = {...} в Python или new Set([...]) в TypeScript."""
    match = re.search(r"COMMON_PASSWORDS\s*=\s*(?:new Set\(\[|\{)(.*?)(?:\]\)|\})", source, re.S)
    return sorted(re.findall(r"""["']([^"']+)["']""", match.group(1))) if match else ["<COMMON_PASSWORDS не найден>"]


def view(check: dict, source: str, spec: str) -> list[str]:
    if check.get("kind") == "password-list":
        return password_list(source)
    if spec.endswith(".py"):
        return python_view(source, check.get("symbols"))
    return text_view(source, check.get("ignore", []))


def summary(line: str) -> None:
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as out:
            out.write(line + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--local", type=Path, help="папка, где рядом лежат клоны проектов")
    args = parser.parse_args()

    failed = 0
    summary("| Общий код | Результат |\n| --- | --- |")
    for check in CHECKS:
        first, *others = check["files"]
        try:
            base = view(check, fetch(first, args.local), first)
            diffs = []
            for spec in others:
                other = view(check, fetch(spec, args.local), spec)
                if other != base:
                    diffs.append("\n".join(difflib.unified_diff(base, other, first, spec, lineterm="")))
        except (OSError, SyntaxError) as exc:
            diffs = [f"не удалось прочитать: {exc}"]
        if diffs:
            failed += 1
            print(f"::error title=Общий код разошёлся::{check['name']}")
            print("\n".join(diffs), "\n")
            summary(f"| {check['name']} | ❌ разошёлся |")
        else:
            print(f"✅ {check['name']}")
            summary(f"| {check['name']} | ✅ |")
    if failed:
        print(f"\nРазошлось: {failed}. Перенесите исправление во все копии — или уберите файл из CHECKS, "
              "если различие задумано.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
