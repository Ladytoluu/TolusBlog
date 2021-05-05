# from django.views.generic import TemplateView

# class HomePageView(TemplateView):
#     template_name = 'index.html'


from django.views import generic
from .models import Post
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'