from django.urls import path

from hexlet_django_blog.article.views import (
    IndexView,
    CustomView,
    ArticleView,
)

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path("<str:tags>/<int:article_id>/",
         CustomView.as_view(), name='article_with_tag'),
]
