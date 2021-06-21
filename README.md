<p class="has-line-data" data-line-start="0" data-line-end="2">Запуск docker сборки:<br>
Запустите сборку докер образа.</p>
<pre><code class="has-line-data" data-line-start="4" data-line-end="6" class="language-bash">sudo docker-compose up --build <span class="hljs-operator">-d</span>
</code></pre>
<p class="has-line-data" data-line-start="7" data-line-end="12"><strong>API</strong><br>
Администрирование:<br>
Опрос CRUD <a href="http://localhost:8000/api/v1/polls/">http://localhost:8000/api/v1/polls/</a><br>
Вопросы CRUD <a href="http://localhost:8000/api/v1/questions/">http://localhost:8000/api/v1/questions/</a><br>
Варианты ответов CRUD <a href="http://localhost:8000/api/v1/choices/">http://localhost:8000/api/v1/choices/</a></p>
<p class="has-line-data" data-line-start="13" data-line-end="17">Пользователь:<br>
Актуальные опросы <a href="http://localhost:8000/api/v1/list/">http://localhost:8000/api/v1/list/</a><br>
Ответ на вопрос <a href="http://localhost:8000/api/v1/answer/">http://localhost:8000/api/v1/answer/</a><br>
Ответы пользователя <a href="http://localhost:8000/api/v1/user/?user_id=%7Buser_id%7D">http://localhost:8000/api/v1/user/?user_id={user_id}</a></p>
