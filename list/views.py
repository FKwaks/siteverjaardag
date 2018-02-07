from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def index(request):
    posts = Post.objects.all()

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.completed_date = timezone.now()
            post.save()
            return redirect('index', form)
    else:
        form = PostForm()

    data = {
        'posts': posts,
        'form': form
    }
    return render(request, 'list/index.html', data)
    #return render(request, 'list/index.html', {'posts': posts})
