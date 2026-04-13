from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from django.views import View
from unicodedata import category

from .models import *


class HomeView(View):
    def get(self, request):
        top_articles = Article.objects.order_by("-important", "-views")[:10]
        latest_articles = Article.objects.order_by("-created_at")[:20]
        context = {
            "top_articles": top_articles,
            "latest_articles": latest_articles,
        }
        return render(request, 'index.html', context=context)

class ArticleDetailsView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        like_articles = Article.objects.filter(
            Q(category=article.category) | Q(tags__in=article.tags.all())).exclude(slug=article.slug).distinct().order_by("-created_at")[:6]
        context = {
            "article": article,
            "like_articles":like_articles
        }
        return render(request, 'article-details.html', context=context)

class NewsletterCreate(View):
    def post(self, request):
        Newsletter.objects.create(
            email = request.POST['email'],
        )
        return redirect("home")

class CommentCreateView(View):
    def post(self, request,slug):
        Comment.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            text = request.POST['text'],
            article = get_object_or_404(Article, slug=slug),
        )
        return redirect("article_details", slug=slug)


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')