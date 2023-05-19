API YATUBE
Описание:
Учебный проект социальной сети.

Как запустить проект:
Клонировать репозиторий: git@github.com:Adolgova/api_final_yatube.git

Cоздать и активировать виртуальное окружение:

py -m venv env

source env/bin/activate

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Выполнить миграции:

py manage.py migrate

Запустить проект:

py manage.py runserver

Примеры запросов и ответов.
Получение GET запроса .../api/v1/posts/
Пример ответа:

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
Выполнение POST запроса постов .../api/v1/posts/

{
  "text": "string",
  "image": "string",
  "group": 0
}
Пример ответа:

{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
Получение всех комментариев к публикации через GET запрос .../api/v1/posts/{post_id}/comments/
Пример ответа:

[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
Добавление нового комментария к публикации через POST .../api/v1/posts/{post_id}/comments/
Пример ответа:

{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
} 
Получение информации о сообществе по id через GET запрос .../api/v1/groups/id/
Пример ответа:

{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
GET-запрос возвращает все подписки пользователя, сделавшего запрос GET .../api/v1/follow/
Пример ответа:

[
  {
    "user": "string",
    "following": "string"
  }
]
Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса POST .../api/v1/posts/{post_id}/comments/
Пример ответа:

{
  "user": "string",
  "following": "string"
}