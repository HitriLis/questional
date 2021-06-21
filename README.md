<p class="has-line-data" data-line-start="0" data-line-end="2">Запуск docker сборки:<br>
Запустите сборку докер образа.</p>
<pre><code class="has-line-data" data-line-start="4" data-line-end="6" class="language-bash">sudo docker-compose up --build <span class="hljs-operator">-d</span>
</code></pre>

<p class="has-line-data" data-line-start="0" data-line-end="2">
Запуск миграции.</p>
<pre><code class="has-line-data" data-line-start="4" data-line-end="6" class="language-bash">
python manage.py migrate
<span class="hljs-operator">-d</span>
</code></pre>

<p class="has-line-data" data-line-start="7" data-line-end="12"><strong>API</strong><br>
Администрирование:<br>
Опрос CRUD /api/v1/polls
Вопросы CRUD /api/v1/questions/
Варианты ответов CRUD /api/v1/choices/
<p class="has-line-data" data-line-start="13" data-line-end="17">Пользователь:<br>
Актуальные опросы /api/v1/list/
Ответ на вопрос /api/v1/answer/
Ответы пользователя /api/v1/user/?user_id={user_id}
