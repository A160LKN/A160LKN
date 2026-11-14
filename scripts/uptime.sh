#!/usr/bin/env bash
# Проверка, что демо всех проектов открываются и отвечают данными.
# Бесплатные серверы Render засыпают после 15 минут простоя и просыпаются около полутора минут
# (всё это время отвечают 503), поэтому сначала будим их все сразу, а потом ждём до 4 минут.
set -uo pipefail

CHECKS=(
  "Shop API — каталог из базы|https://shop-api-yka7.onrender.com/products?limit=1|\"items\""
  "Бірге API|https://birge-api-j4n8.onrender.com/health|\"ok\""
  "Касса API — афиша из базы|https://kassa-api-419n.onrender.com/events|\"items\""
  "Дүкен — сайт магазина|https://shop-web-azure.vercel.app/|<div id=\"root\">"
  "Бірге — сайт доски|https://birge-seven.vercel.app/|<div id=\"root\">"
)

# Будим все серверы параллельно, ответ не важен
for c in "${CHECKS[@]}"; do curl -s -o /dev/null --max-time 10 "$(cut -d'|' -f2 <<<"$c")" & done
wait

failed=0
echo "| Проект | Результат | Время ответа |" >> "${GITHUB_STEP_SUMMARY:-/dev/null}"
echo "| --- | --- | --- |" >> "${GITHUB_STEP_SUMMARY:-/dev/null}"
for c in "${CHECKS[@]}"; do
  IFS='|' read -r name url expect <<<"$c"
  ok=""
  for attempt in $(seq 1 16); do
    body=$(curl -s --max-time 30 -w '\n%{http_code} %{time_total}' "$url") || true
    meta=$(tail -n1 <<<"$body"); code=${meta%% *}; time=${meta##* }
    if [ "$code" = "200" ] && grep -qF -- "$expect" <<<"$body"; then ok=1; break; fi
    sleep 15
  done
  if [ -n "$ok" ]; then
    echo "✅ $name — ${time} с (попытка $attempt)"
    echo "| $name | ✅ | ${time} с |" >> "${GITHUB_STEP_SUMMARY:-/dev/null}"
  else
    echo "::error title=Демо не отвечает::$name — $url (последний код: ${code:-нет ответа})"
    echo "| $name | ❌ код ${code:-нет ответа} | — |" >> "${GITHUB_STEP_SUMMARY:-/dev/null}"
    failed=1
  fi
done
exit $failed
