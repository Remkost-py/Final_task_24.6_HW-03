from django.views.generic import ListView, DetailView
from .models import Post


class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        queryset = super().get_queryset().filter(type='news')  # Фильтруем только новости
        return queryset.order_by('-created_at')  # Сортируем по убыванию даты публикации


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'
