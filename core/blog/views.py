from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Article


def home(request):

    featured = Article.articlemanager.filter()
    context = {
        'articles': featured
    }

    return render(request, 'index.html', context)

