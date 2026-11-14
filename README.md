<h1 align="center">Айбол Казбаев</h1>

<p align="center">
  <b>QA Engineer</b> · автотесты UI, API и бэкенда · fullstack-проекты на React, FastAPI и Node.js · Астана
</p>

<p align="center">
  <a href="mailto:aibolkazbayev@gmail.com"><img src="https://img.shields.io/badge/Написать-aibolkazbayev@gmail.com-1f4e8c?style=for-the-badge&logo=gmail&logoColor=white" alt="Написать: aibolkazbayev@gmail.com"></a>
  <a href="https://www.linkedin.com/in/aibolkazbayev/"><img src="https://img.shields.io/badge/LinkedIn-aibolkazbayev-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn: aibolkazbayev"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/900+-автотестов-1f4e8c?style=flat-square" alt="больше 900 автотестов">
  <img src="https://img.shields.io/badge/9-CI_пайплайнов-1f4e8c?style=flat-square" alt="9 CI-пайплайнов">
  <img src="https://img.shields.io/badge/13-репозиториев-1f4e8c?style=flat-square" alt="13 репозиториев">
</p>

---

### 👋 Обо мне

- 🔍 **Ручное тестирование:** тест-кейсы и баг-репорты в Jira, проверка API в Postman и данных через SQL, тест-дизайн и тестовая документация.
- 🤖 **Автоматизация:** UI-тесты на Selenium и Playwright, API-тесты на requests и Pydantic, отчёты Allure, запуск в GitHub Actions.
- 🗄 **Бэкенд:** тестирую сервис целиком — PostgreSQL, транзакции и одновременные запросы, моки внешних сервисов, Docker, нагрузка на k6.
- 🧠 **Тестирование AI:** проверяю ответы ассистентов на галлюцинации, prompt injection и стабильность, сравниваю версии перед релизом.
- 🧩 **Fullstack:** React + TypeScript, FastAPI, Node.js + Fastify — три проекта работают онлайн, у каждого тесты, CI и деплой.

---

### 📂 Проекты

#### ⚡ Fullstack: доска задач «Бірге» в реальном времени — [открыть онлайн](https://birge-seven.vercel.app)

| Проект | Что внутри | CI |
| --- | --- | --- |
| [**birge**](https://github.com/A160LKN/birge) | Доска задач для команды: изменения коллег приходят по WebSocket сразу, с подсветкой цветом автора. FastAPI (async) + PostgreSQL, React + TypeScript. Рассылка событий через LISTEN/NOTIFY и очередь фоновых задач на `FOR UPDATE SKIP LOCKED` — без Redis. Защита от одновременных правок (оптимистическая блокировка), вложения с проверкой типа по содержимому и превью в фоне. 196 тестов бэкенда (98 %), 83 фронтенда, 12 E2E в **двух браузерах одновременно**. После деплоя нашёл, что через пул соединений Neon теряются уведомления, — исправил · [демо](https://birge-seven.vercel.app) | [![CI](https://github.com/A160LKN/birge/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/A160LKN/birge/actions/workflows/ci.yml) |

#### 🛒 Fullstack: магазин «Дүкен» — [открыть онлайн](https://shop-web-azure.vercel.app)

| Проект | Что внутри | CI |
| --- | --- | --- |
| [**shop-web**](https://github.com/A160LKN/shop-web) | Витрина и админка на React и TypeScript: каталог с фильтрами, корзина, сверенная с сервером, оплата с отказом банка и таймаутом, сводка для админа с графиком выручки. Типы API генерируются из OpenAPI, CI сверяет контракт с работающим бэкендом. 120 компонентных тестов (Vitest, MSW) и 25 E2E на Playwright против настоящего API в Docker · [демо](https://shop-web-azure.vercel.app) | [![CI](https://github.com/A160LKN/shop-web/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/A160LKN/shop-web/actions/workflows/ci.yml) |
| [**shop-api**](https://github.com/A160LKN/shop-api) | Бэкенд на FastAPI и PostgreSQL и 227 тестов к нему: юнит, интеграционные, API. Одновременные заказы (последний товар не продаётся дважды), мок платёжного шлюза, IDOR и подделка токенов, нагрузка на k6 — 240 запросов/с без ошибок. 9 найденных и закрытых дефектов, один из них — гонка при отмене заказа, пойманная проверкой целостности данных после нагрузки. Docker, деплой на Render · [документация API](https://shop-api-yka7.onrender.com/docs) | [![CI](https://github.com/A160LKN/shop-api/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/A160LKN/shop-api/actions/workflows/ci.yml) |

#### ⚙️ Бэкенд и API

| Проект | Что внутри | CI |
| --- | --- | --- |
| [**kassa-api**](https://github.com/A160LKN/kassa-api) | API продажи билетов на **Node.js + TypeScript** (Fastify, PostgreSQL, Drizzle, Zod): бронь мест на 10 минут — двойная продажа невозможна на уровне базы; заказы с Idempotency-Key; оплата через вебхуки с HMAC-подписью, защитой от повтора и возвратом при поздней оплате. 92 теста (99 %): 50 покупателей на одно место, fast-check по конечному автомату, настоящий HTTP-вебхук; смоук всего пути покупки в Docker · [документация онлайн](https://kassa-api-419n.onrender.com/docs) | [![CI](https://github.com/A160LKN/kassa-api/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/A160LKN/kassa-api/actions/workflows/ci.yml) |
| [**booker-api-tests**](https://github.com/A160LKN/booker-api-tests) | Тесты публичного REST API: CRUD, авторизация по токену, контракт ответов на Pydantic, 3 задокументированных дефекта. Коллекция Postman с запуском через Newman в CI · [Allure-отчёт](https://a160lkn.github.io/booker-api-tests/) | [![API tests](https://github.com/A160LKN/booker-api-tests/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/A160LKN/booker-api-tests/actions/workflows/tests.yml) |

#### 🖥 UI-автотесты

| Проект | Что внутри | CI |
| --- | --- | --- |
| [**taskflow-autotests**](https://github.com/A160LKN/taskflow-autotests) | 21 UI-тест для моего приложения TaskFlow: Python, Selenium, pytest, Page Object · [Allure-отчёт](https://a160lkn.github.io/taskflow-autotests/) | [![UI tests](https://github.com/A160LKN/taskflow-autotests/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/A160LKN/taskflow-autotests/actions/workflows/tests.yml) |
| [**saucedemo-autotests-java**](https://github.com/A160LKN/saucedemo-autotests-java) · [**python**](https://github.com/A160LKN/saucedemo-autotests-python) | Один набор UI-тестов интернет-магазина на двух языках: JUnit 5 и pytest, Allure со скриншотом при падении | |

#### 🧠 Тестирование AI

| Проект | Что внутри | CI |
| --- | --- | --- |
| [**ai-eval-kit**](https://github.com/A160LKN/ai-eval-kit) | 14 проверочных сценариев для AI-ассистента маркетплейса: выдуманные цены, prompt injection, неполные данные, повторные вопросы. Сравнение версий и quality gate перед релизом | [![AI eval](https://github.com/A160LKN/ai-eval-kit/actions/workflows/eval.yml/badge.svg?branch=main)](https://github.com/A160LKN/ai-eval-kit/actions/workflows/eval.yml) |

#### 💡 Мои веб-приложения

| Проект | Что внутри | CI |
| --- | --- | --- |
| [**FinFlow**](https://github.com/A160LKN/FinFlow) | Учёт личных финансов: бюджеты, SVG-графики, импорт и экспорт CSV, работает офлайн. 71 юнит- и 32 E2E-теста на Playwright, полная тестовая документация (требования, тест-стратегия, тест-дизайн, матрица покрытия), main защищена — изменения только через PR · [демо](https://a160lkn.github.io/FinFlow/) | [![CI](https://github.com/A160LKN/FinFlow/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/A160LKN/FinFlow/actions/workflows/ci.yml) |
| [**TaskFlow**](https://github.com/A160LKN/TaskFlow) | Трекер задач на HTML, CSS и JavaScript с атрибутами `data-testid` для автотестов · [демо](https://a160lkn.github.io/TaskFlow/) | 🌐 онлайн |

#### 🎯 Практика

| Проект | Что внутри | CI |
| --- | --- | --- |
| [**sql-trainer**](https://github.com/A160LKN/sql-trainer) | 15 задач по SQL с автопроверкой: от `SELECT` до `JOIN` и подзапросов, поиск ошибок в данных | [![SQL tests](https://github.com/A160LKN/sql-trainer/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/A160LKN/sql-trainer/actions/workflows/tests.yml) |

---

### 🧰 Стек

| Область | Инструменты |
| --- | --- |
| **Тестирование** | ![Jira](https://img.shields.io/badge/Jira-0052CC?style=flat&logo=jira&logoColor=white) ![Confluence](https://img.shields.io/badge/Confluence-172B4D?style=flat&logo=confluence&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white) ![Newman](https://img.shields.io/badge/Newman-FF6C37?style=flat&logo=postman&logoColor=white) ![DevTools](https://img.shields.io/badge/DevTools-4285F4?style=flat&logo=googlechrome&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-003B57?style=flat&logo=sqlite&logoColor=white) |
| **Автоматизация** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white) ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white) ![requests](https://img.shields.io/badge/requests-REST_API-2E7D32?style=flat) ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=pydantic&logoColor=white) ![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=flat&logo=vitest&logoColor=white) ![Allure](https://img.shields.io/badge/Allure-FF6F00?style=flat) ![k6](https://img.shields.io/badge/k6-7D64FF?style=flat&logo=k6&logoColor=white) ![Java](https://img.shields.io/badge/Java-ED8B00?style=flat&logo=openjdk&logoColor=white) ![JUnit5](https://img.shields.io/badge/JUnit_5-25A162?style=flat&logo=junit5&logoColor=white) |
| **Бэкенд** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) ![WebSocket](https://img.shields.io/badge/WebSocket-010101?style=flat&logo=socketdotio&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white) |
| **CI и инструменты** | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black) ![Maven](https://img.shields.io/badge/Maven-C71A36?style=flat&logo=apachemaven&logoColor=white) ![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white) ![Fastify](https://img.shields.io/badge/Fastify-000000?style=flat&logo=fastify&logoColor=white) ![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=flat&logo=pycharm&logoColor=white) ![IntelliJ IDEA](https://img.shields.io/badge/IntelliJ_IDEA-000000?style=flat&logo=intellijidea&logoColor=white) |
| **Веб** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white) ![React](https://img.shields.io/badge/React-149ECA?style=flat&logo=react&logoColor=white) ![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white) ![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white) |
