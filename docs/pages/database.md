# База данных

В модуле :doc:`database.py </modules/autodonate.database>` используется паттерн [Singleton](https://refactoring.guru/ru/design-patterns/singleton).
Если вкратце, может существовать только один объект этого класса, все остальное - ссылки.
Так что вам не нужно беспокоиться о большом количестве соединений, откуда вы бы не вызвали класс - 
вернеться один и тот же объект:

```py
>>> from autodonate.database import Database
>>> db1 = Database.get_instance()
>>> db2 = Database.get_instance()
>>> db1 == db2
True
```

Мы используем фреймворк [sqlalchemy](https://www.sqlalchemy.org) с [API v2.0](https://docs.sqlalchemy.org/en/14/tutorial/index.html)
для управления базой данных, и поддержкой сразу нескольких СУБД. В основном это SQLite, MySQL и PostGreSQL.

## Как добавить таблицу

Таблицу нужно зарегистрировать в объекте `metadata`, в нашем случае он храниться в `db.mapper_registry.metadata`.
Мы рекомендуем использовать один из стилей объявления - "Полу-полу ORM" и/или "Full ORM".

### Стиль "Full ORM"

Название означает что мы объявляем класс и сразу описываем реализацию внутри. Большой и критичный минус из-за которого мы
используем другой стиль, это то что класс нужно наследовать от переменной [base](https://docs.sqlalchemy.org/en/14/tutorial/metadata.html#setting-up-the-registry).
А её нельзя создать без доступа к `metadata` объекту, который нельзя создать без инициализации базы данных.

Получается при импорте, нужно объявить переменную `base` и инициализировать БД. Стиль "Полу-полу ORM" лишен данного недостатка.

Примеры вы можете найти на [официальной документации SQLAlchemy](https://docs.sqlalchemy.org/en/14/tutorial/metadata.html#declaring-mapped-classes),
там же и подробное объяснение вместе с API. Класс :doc:`Database </modules/autodonate.database>` предоставляет только
инициализацию и хранение данных.

### Стиль "Полу-полу ORM"

В документации `sqlalchemy` это называется `imperative style`. По сути, мы создаем объект таблицы через интерфейс
SQLAlchemy Core и привязываем его к общедоступному классу.

Например, у нас пустые классы хранятся в :doc:`tables.py </modules/autodonate.tables>` и объявляются в
:doc:`database.py </modules/autodonate.database>`. Таким образом мы можем обойти недостаток стиля "Full ORM" и
предоставить удобный способ управления через ORM стиль.

Привязка объекта `Table` происходит через метод `db.mapper_registry.map_imperatively(class, Table)` ([API](https://docs.sqlalchemy.org/en/14/orm/mapping_api.html#sqlalchemy.orm.registry.map_imperatively)).

### Другие стили

Подробнее про стили, и остальные несколько можете узнать на [официальном API SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html).
