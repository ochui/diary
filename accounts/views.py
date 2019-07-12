from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from .forms import PostForm


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PostListView(LoginRequiredMixin, ListView):

    model = Post
    template_name = "post/post_list.html"

    def get_queryset(self):
        return Post.objects.all()
    

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

