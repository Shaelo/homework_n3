from django.urls import path, include

from post.views import *

urlpatterns = [
    path('list/', PostListView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('update/', PostCreateView.as_view()),
    path('delete/', PostDeleteView.as_view()),

]