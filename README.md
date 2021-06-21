<p class="has-line-data" data-line-start="0" data-line-end="2">Запуск docker сборки:<br>
Запустите сборку докер образа.</p>
<pre><code class="has-line-data" data-line-start="4" data-line-end="6" class="language-bash">sudo docker-compose up --build <span class="hljs-operator">-d</span>
</code></pre>

<p class="has-line-data" data-line-start="0" data-line-end="2">
Запуск миграции.</p>
<pre><code class="has-line-data" data-line-start="4" data-line-end="6" class="language-bash">python manage.py migrate</code></pre>

<p class="has-line-data" data-line-start="0" data-line-end="2">
Cоздать суперпользователя.</p>

<pre><code class="has-line-data" data-line-start="4" data-line-end="6" class="language-bash">python manage.py createsuperuser</code></pre>

<p class="has-line-data" data-line-start="7" data-line-end="12"><strong>API</strong><br>
Администрирование:<br>
Опрос CRUD /api/v1/polls<br>
Вопросы CRUD /api/v1/questions/<br>
Варианты ответов CRUD /api/v1/choices/<br>
<p class="has-line-data" data-line-start="13" data-line-end="17">Пользователь:<br>
Актуальные опросы /api/v1/list/<br>
Ответ на вопрос /api/v1/answer/<br>
Ответы пользователя /api/v1/user/?user_id={user_id}
