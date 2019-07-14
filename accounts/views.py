from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.db.models import Q
from .models import Post
from .forms import PostForm, RegisterForm, LoginForm


class SignUp(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PostListView(LoginRequiredMixin, ListView):

    model = Post
    template_name = "post/post_list.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post/post_details.html"


class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    form_class = PostForm
    template_name = "post/post_create.html"

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class CustomLoginView(LoginView):

    form_class = LoginForm


class DashboardView(ListView, LoginRequiredMixin):

    model = Post
    template_name = "dashboard/dashboard.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(text__icontains=query)
            )
        else:
            return Post.objects.all()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "post/post_create.html"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard')
    template_name = "post/post_check_delete.html"
