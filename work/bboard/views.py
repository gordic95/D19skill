from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForm

from django.urls import reverse_lazy
from .models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    paginate_by = 8

    #Надо обдумать
    # def get_context_data(self, **kwargs):    # добавим переменную к контексту и инициализируем ее пустым списком
    #     context = super().get_context_data(**kwargs)    # вызываем базовый метод
    #     post =self.get_object().id       # получаем объект продукта
    #     comments = Comment.objects.filter(post=post)        # получаем комментарии к продукту
    #     context['comment'] = comments        # записываем их в контекст
    #     return context         # возвращаем контекст


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
# Обратите внимание, в представлении мы также не указываем форму. Вместо неё появляется поле success_url, в которое мы должны указать, куда перенаправить пользователя после успешного удаления товара. Логика работы reverse_lazy точно такая же, как и у функции reverse, которую мы использовали в моделе Product.


class CreateComment(CreateView, LoginRequiredMixin):
    model = Comment
    template_name = 'create_comment.html'
    fields = ['author', 'content']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('posts')