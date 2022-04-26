# История изменений

Мы следуем стандартному стилю [Semantic Versions](https://semver.org/).

## Еще не выпущено

- Изменили способ генерации API на полностью автоматический. ([#91](https://github.com/fire-square/autodonate/pull/91))
- Добавили несколько новых зависимостей для лучшего управления проектом. ([#80](https://github.com/fire-square/autodonate/pull/80))
- Вернулись на [Django](https://pypi.org/project/Django) и изменили концепцию сайта. ([8651e4d](https://github.com/fire-square/autodonate/commit/8651e4d31b798ef44acbf1d8a9f99b4a082197f2))

## Версия 0.2.0 (не выпущено)

- Переписали все на фреймворк [aiohttp](https://pypi.org/project/aiohttp) вместо [Django](https://pypi.org/project/Django). ([aiohttp ветвь](https://github.com/fire-squad/autodonate/tree/aiohttp))
- Убрали поддержку Python 3.11-dev. ([#36](https://github.com/fire-squad/autodonate/pull/36))

## Версия 0.1.2

- Добавили поддержку Python 3.8 и выше. ([40bb312](https://github.com/fire-squad/autodonate/commit/40bb3123b1db0a7591025a34757e21724acc40fd))
- Сделали новое API для платежных систем. ([#16](https://github.com/fire-squad/autodonate/pull/16))
- Переместили RCON в плагин [autodonate-rcon-api](https://github.com/fire-squad/autodonate-rcon-api). ([#21](https://github.com/fire-squad/autodonate/pull/21))
- Переименовали секцию lint в style в файле Makefile. ([6e64703](https://github.com/fire-squad/autodonate/commit/6e647036901a1c4b3e214a45ab3ccf14731fb53d))
- Убрали с документации папку с файлами миграций. ([fe4560a](https://github.com/fire-squad/autodonate/commit/fe4560ac336f76d898e141ff66019ce189473571))
- Добавили форматер [isort](https://pypi.org/project/isort). ([#20](https://github.com/fire-squad/autodonate/pull/20))
- Изменили бейдж с версией Python'а чтобы бралось значение с PIP ([b868f14](https://github.com/fire-squad/autodonate/commit/b868f142075ab2540bdea627fb60ff37ab324338))

## Версия 0.1.1

- Первая минимально рабочая версия. Все еще не готова к постоянному использованию.
- Базовый API для плагинов (RCON, CRON, модели).
- Докер контейнер.
- Сброшена поддержка всех версий Python кроме 3.10.
- Конфиг переведен в YAML формат (раньше TOML).

## Версия 0.1.0

- Репозиторий инициализирован
