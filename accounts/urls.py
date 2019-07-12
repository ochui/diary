from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path("posts", views.PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/new", views.PostCreateView.as_view(), name="post_create"),
]