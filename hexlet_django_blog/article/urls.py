from django.urls import path

from hexlet_django_blog.article.views import IndexView, CustomView

urlpatterns = [
    path("<str:tags>/<int:article_id>/",
         CustomView.as_view(), name='article'),
    path('', IndexView.as_view()),
]
