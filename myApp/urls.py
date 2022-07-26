from django.urls import path
from myApp import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('question/<slug:slug>',
         login_required(views.Question.as_view()), name='question')
]
