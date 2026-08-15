from django.urls import path
from .views import (PostDeleteView, 
                    PostListView,
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView,
                    )   

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/crear/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/actualizar/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
]