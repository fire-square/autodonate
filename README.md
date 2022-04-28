# autodonate

[![Build Status](https://github.com/fire-square/autodonate/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/fire-square/autodonate/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/fire-square/autodonate/branch/master/graph/badge.svg)](https://codecov.io/gh/fire-square/autodonate)
[![Documentation Build Status](https://readthedocs.org/projects/autodonate/badge/?version=latest)](https://autodonate.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/autodonate)](https://www.python.org/downloads/)

Бесплатный сайт авто покупок для майнкрафт серверов.

## <img src="https://trello.com/favicon.ico" alt="trello logo" width="20"/> [Trello доска](https://trello.com/b/EMFCYmFS/autodonate)

## Особенности

- ZeroConfig. Всё настраивается в админ панели.
- ZeroPenalties. Разработчики не получают никаких отчислений.
- SelfHost. Вы сами управляете своей системой.
- Free. Сайт полностью бесплатный, разработка поддерживается с помощью ваших [пожертвований](DONATE.md).

## Установка

Установите `git` и `node.js` для вашей платформы.

```bash
git clone --recurse-submodules https://github.com/fire-square/autodonate.git
cd autodonate

cd svelte
npm install
npm run build
cd ..
```

Затем установите `poetry` [рекомендованым путем](https://python-poetry.org/docs/master/#installation).

Если вы на платформе `Linux`, используйте команду:

```bash
curl -sSL https://install.python-poetry.org | python -
```

Если вы на Windows, откройте PowerShell от имени администратора и используйте:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

И наконец установим зависимости:

```bash
poetry install
```

## Спасибо

Этот проект был сгенерирован с помощью [`fire-square-style`](https://github.com/fire-square/fire-square-style).
Текущая версия примера: [165e5d7b77d7a18da096c630ece628c6f5ce91fd](https://github.com/fire-square/fire-square-style/tree/165e5d7b77d7a18da096c630ece628c6f5ce91fd).
Смотрите что [обновилось](https://github.com/fire-square/fire-square-style/compare/165e5d7b77d7a18da096c630ece628c6f5ce91fd...master) с того времени.
