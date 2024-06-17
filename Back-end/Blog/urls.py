from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('choose-category/', views.choose_category, name='choose_category'),
    path('choose-type/', views.choose_type, name='choose_type'),
    path('ask-question/', views.ask_question, name='ask_question'),
    path('question-detail/<int:question_id>/',views.question_detail, name='question_detail'),
    path('create-response/<int:question_id>/', views.create_response, name='create_response'),
    path('response-vote/<int:response_id>/<str:vote_type>/', views.response_vote, name='response_vote'),
    path('answers/<int:question_id>/', views.AnswerListByQuestionAPIView.as_view(), name='answer-list-by-question'),
    path('questions/', views.QuestionListAll.as_view(), name='question-list'),
    path('questions/<int:question_id>/', views.QuestionListById.as_view(), name='question-detail'),
    path('questions/author/<int:author_id>/', views.QuestionListByAuthor.as_view(), name='question-list-author'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
