from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
    posts = Post.objects.filter(completed_date__lte=timezone.now()).order_by('completed_date')
    return render(request, 'list/index.html', {'posts': posts})
    
