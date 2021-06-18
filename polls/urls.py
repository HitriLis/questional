from .views.simple import PollsView, PollsViewList, QuestionsViewList, ChoicesView
from rest_framework.routers import DefaultRouter

app_name = "polls"
router = DefaultRouter()
router.register(r'polls', PollsView, basename='polls')
router.register(r'list', PollsViewList, basename='polls_list')
router.register(r'questions', QuestionsViewList, basename='questions')
router.register(r'choices', ChoicesView, basename='choices')
# router.register('questions/<int:pk>/highlight/', name='snippet-highlight'),
urlpatterns = router.urls
