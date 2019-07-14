from django.urls import path

from . import views


urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path("login/", views.CustomLoginView.as_view(), name="c_login"),
    path("posts", views.PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/new", views.PostCreateView.as_view(), name="post_create"),
    path("posts/edit/<int:pk>", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/delete/<int:pk>", views.PostDeleteView.as_view(), name="post_delete"),
]