from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

# from django.contrib.auth.forms import UserCreationForm
from Insta.forms import CustomUserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from Insta.models import Post

# Create your views here.

class PostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    login_url = 'login'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
	model = Post
	template_name = 'make_post.html'
	fields = '__all__'

class PostUpdateView(UpdateView):
	model = Post
	template_name = "update_post.html"
	fields = ('title',)

class PostDeleteView(DeleteView):
	model = Post
	template_name = "delete_post.html"
	success_url = reverse_lazy('home')

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('home')
	template_name = 'registration/signup.html'

		
		
