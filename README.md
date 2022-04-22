# autodonate

[![Build Status](https://github.com/fire-square/autodonate/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/fire-square/autodonate/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/fire-square/autodonate/branch/master/graph/badge.svg)](https://codecov.io/gh/fire-square/autodonate)
[![Documentation Build Status](https://readthedocs.org/projects/autodonate/badge/?version=latest)](https://autodonate.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/autodonate)](https://www.python.org/downloads/)

Бесплатный сайт авто покупок для майнкрафт серверов.

## Особенности

- ZeroConfig. Всё настраивается в админ панели.
- ZeroPenalties. Разработчики не получают никаких отчислений.
- SelfHost. Вы сами управляете своей системой.
- Free. Сайт полностью бесплатный, разработка поддерживается с помощью ваших [пожертвованиях](DONATE.md).

## Установка

```bash
pip install autodonate
```

## Установка для локальной разработки

```bash
git clone https://https://github.com/fire-square/autodonate.git
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

Внимание: На момент написания текста (03.3.2022), существует баг, который вызывает предупреждение при использовании любой команды. 
Если вы с таким столкнулись, можете установить poetry другим путем:

```bash
pip install poetry
```

Но учитывайте что это не рекомендованый путь, вы возможно не сможете использовать некоторые функции (например `poetry self update`).

И наконец установим зависимости:

```bash
poetry install
```

## Спасибо

Этот проект был сгенерирован с помощью [`fire-square-style`](https://github.com/fire-square/fire-square-style).
Текущая версия примера: [25d747b](https://github.com/fire-square/fire-square-style/tree/25d747b6697fd0afa3cce24e4dc5b066c12d805d).
Смотрите что [обновилось](https://github.com/fire-square/fire-square-style/compare/25d747b6697fd0afa3cce24e4dc5b066c12d805d...master) с того времени.
