#need this import in function based view only
# from django.shortcuts import render

#import for class based view
from django.views.generic import TemplateView, DetailView
from .models import Post
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all
        return context

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post