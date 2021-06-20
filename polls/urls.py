from .views.simple import PollsView, PollsViewList, QuestionsViewList, ChoicesView, AnswerView, AnswerUserView
from rest_framework.routers import DefaultRouter

app_name = "polls"
router = DefaultRouter()
router.register(r'polls', PollsView, basename='polls')
router.register(r'list', PollsViewList, basename='polls_list')
router.register(r'questions', QuestionsViewList, basename='questions')
router.register(r'choices', ChoicesView, basename='choices')
router.register(r'answer', AnswerView, basename='answer')
router.register(r'user', AnswerUserView, basename='user')
urlpatterns = router.urls
