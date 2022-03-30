# autodonate

[![Build Status](https://github.com/fire-squad/autodonate/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/fire-squad/autodonate/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/fire-squad/autodonate/branch/master/graph/badge.svg)](https://codecov.io/gh/fire-squad/autodonate)
[![Documentation Build Status](https://readthedocs.org/projects/autodonate/badge/?version=latest)](https://autodonate.firesquare.ru/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/autodonate)](https://www.python.org/downloads/)
[![GitLab mirror](https://badgen.net/badge/mirror/GitLab/yellow)](https://git.averyan.ru/mirrors/minecraft/autodonate)

Бесплатный и модульный сайт авто-доната для майнкрафт серверов.

# Проект в очень сырой стадии, не используйте его, пока что.


## Особенности

- Полностью сделано с аннотациями и проверено с помощью mypy, [используется PEP561](https://www.python.org/dev/peps/pep-0561/).
- Модульный сайт! Вы можете отключить любой компонент этого проекта, и все будет отлично работать!
- Бесплатно! Мы не попросим ни копейки за использование!


## Установка

Мы используем `poetry` для управления зависимостями.
Обратите внимание что он автоматически создает и настраивает виртуальное окружение.

### Сначала установим poetry [рекомендованым путем](https://python-poetry.org/docs/master/#installation).

Если вы на платформе Linux, используйте команду:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Если вы на Windows, откройте PowerShell от имени администратора и используйте:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Внимание: На момент написания текста (03.3.2022), существует баг, который вызывает предупреждение при использовании любой команды. Если вы с таким столкнулись, можете установить poetry другим путем:

```bash
pip install poetry
```

Но учитывайте что это не рекомендованый путь, вы возможно не сможете использовать некоторые функции (например `poetry self update`).

### Установим все зависимости в виртуальное окружение:

```bash
poetry install
```
