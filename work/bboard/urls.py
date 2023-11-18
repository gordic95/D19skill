from django.urls import path
from .views import PostListView,  PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,  CreateComment


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/create_comment', CreateComment.as_view(), name='create_comment'),
]