Запуск docker сборки:
Запустите сборку докер образа.

```bash
sudo docker-compose up --build -d
```

**API**
Администрирование:
  Опрос CRUD http://localhost:8000/api/v1/polls/
  Вопросы CRUD http://localhost:8000/api/v1/questions/
  Варианты ответов CRUD http://localhost:8000/api/v1/choices/

Пользователь:
  Актуальные опросы http://localhost:8000/api/v1/list/
  Ответ на вопрос http://localhost:8000/api/v1/answer/
  Ответы пользователя http://localhost:8000/api/v1/user/?user_id={user_id}
