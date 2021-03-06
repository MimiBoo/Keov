from django.urls import path, include
from django.views.generic import ListView, DetailView
from news.models import Post

urlpatterns = [path('', ListView.as_view(queryset=Post.objects.all().order_by("-date"), template_name="news/news.html")),
               path('news/<int:pk>', DetailView.as_view(model=Post, template_name='news/post.html'))
               ]
