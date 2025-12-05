from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'slug', 'content', 'image']
	template_name = 'blog/post_form.html'
	success_url = reverse_lazy('blog:post_list')

	def test_func(self):
		post = self.get_object()
		return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/post_confirm_delete.html'
	success_url = reverse_lazy('blog:post_list')

	def test_func(self):
		post = self.get_object()
		return post.author == self.request.user

from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Post
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request, username=None):
	if username:
		user = get_object_or_404(User, username=username)
	else:
		user = request.user
	return render(request, 'blog/profile.html', {'profile_user': user})

@method_decorator(cache_page(60 * 5), name='dispatch')  # Cache for 5 minutes
class PostListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'
	paginate_by = 5

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'slug', 'content', 'image']
	template_name = 'blog/post_form.html'
	success_url = reverse_lazy('blog:post_list')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

# Create your views here.
