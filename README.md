# autodonate

[![Build Status](https://github.com/fire-square/autodonate/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/fire-square/autodonate/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/fire-square/autodonate/branch/master/graph/badge.svg)](https://codecov.io/gh/fire-square/autodonate)
[![Documentation Build Status](https://readthedocs.org/projects/autodonate/badge/?version=latest)](https://autodonate.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Project roadmap](https://img.shields.io/badge/Road-map-2ddd27.svg)](https://github.com/orgs/fire-square/projects/1)

Бесплатный сайт авто продаж для майнкрафт серверов.

## Особенности

- ZeroConfig. Всё настраивается в админ панели.
- ZeroPenalties. Разработчики не получают никаких отчислений.
- SelfHost. Вы сами управляете своей системой.
- Free. Сайт полностью бесплатный, разработка поддерживается с помощью ваших [пожертвований](DONATE.md).

## Установка

```bash
git clone https://github.com/fire-square/autodonate.git
cd autodonate
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
