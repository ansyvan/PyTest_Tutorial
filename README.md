# PyTest_Tutorial

<h1>Проєктне завдання 1</h1>

Створити структуру папок і файлів фреймворка.

1. В склонованому з GiHub репозиторії (це той репозиторій, який ви клонували, виконуючи блок лекцій по GIT) створити наступну ієрархію файлі і папок, що ми будемо вважати початково стуктурою фреймворка:

Структура папок від кореневої директорії проєкта:

/config

/modules

 /modules/common

/modules/ui

/modules/ui/page_objects

/modules/api

/modules/api/clients

/tests

/tests/ui

/tests/api

Структура файлів від кореневої директорії проєкта:

/config/config.py

modules/common/__init__.py

/modules/ui/page_objects/__init__.py

/modules/api/clients/__init__.py

/tests/ui/test_ui.py

/tests/api/test_api.py

2. Всі створені, змінені та видалені файли додати до коміта і відправити на сервер GitHub за допомогою команди git push

<h1>Проєктне завдання 2</h1>

Розробити тести за допомогою модуля pytest, використовуючи фікстури і мітки

В склонованому з GiHub репозиторії (це той репозиторій, який ви клонували, виконуючи блок лекцій по GIT), використовуючи результати попереднього модуля, розробити тести за допомогою модуля pytest, які відповідають наступним вимогам:

1. Мітки check та change зареєстровані в файлі pytest.ini
2. В файлі conftest.py описати клас User:
  - За допомогою конструктора задати поля name та second_name зі значеннями за замовчування None
  - Клас має метод об’єкта “створити” (create). Метод задає полям name та second_name значення вашого імені та прізвища
  - Клас має метод об’єкта “видалити” (remove). Метод задає полям name та second_name значення пустого рядка
  - В файлі conftest.py описати фікстуру user. Ця фікстура:
3. Створює об’єкт класа User
  - Викликає метод об’єкту create
  - Повертає об’єкт після виклику методу об’єкту create в тести
  - Після виконання тесту викликає метод об’єкту remove
4. В файлі /tests/api/test_fixtures.py створити тест test_change_name:
  - Тест має мітку check
  - Використовує фікстуру user
  - Перевіряє, що поле name об’єкту user відповідає очікуваному
5. В файлі /tests/api/test_fixtures.py створити тест test_change_second_name:
  - Тест має мітку check
  - Використовує фікстуру user
  - Перевіряє, що поле second_name об’єкту user відповідає очікуваному
6. В файлі /tests/api/test_api.py створити тест test_remove_name:
  - Тест має мітку change
  - Використовує фікстуру user
  - Першим кроком тест змінює поле name об’єкта user на пустий рядок
  - Другим кромом тест перевіряє, що зміни відбулися і вони правильні
7. В файлі /tests/api/test_api.py створити тест test_name:
  - Тест має мітку check
  - Використовує фікстуру user
  - Перевіряє, що поле name об’єкту user відповідає очікуваному
8. В файлі /tests/api/test_api.py створити тест test_second_name:
  - Тест має мітку check
  - Використовує фікстуру user
  - Перевіряє, що поле second_name об’єкту user відповідає очікуваному

Всі створені, змінені та видалені файли додати до коміта і відправити на сервер GitHub за допомогою команди git push