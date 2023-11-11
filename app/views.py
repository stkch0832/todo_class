from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'app/post_list.html'
    ordering = '-updated_at'

    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id).order_by('-updated_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'app/post_detail.html'


class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app/post_form.html'
    success_message = "新規投稿が完了しました"

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('app:list')


class PostUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'app/post_form.html'
    model = Post
    form_class = PostForm
    success_message = "更新が完了しました"

    def get_success_url(self):
        return reverse('app:detail', kwargs={'pk': self.kwargs['pk']})

class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('app:list')

    def get_success_message(self, cleaned_data):
        return f'{self.object.title} を削除しました'
