from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def index(request):
    posts = Post.objects.filter(completed_date__lte=timezone.now()).order_by('completed_date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index', {'form': form}, {'posts': posts} )
    else:
        form = PostForm()
    return render(request, 'list/index.html', {'form': form}, {'posts': posts})
    #return render(request, 'list/index.html', {'posts': posts})
