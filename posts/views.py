from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    # If the method is post
    if request.method == 'POST':
        form = PostForm(request.POST)
        # if the mrthod is valid
        if form.is_valid():
            #Yes, Save
            form.save()

            # Redirect to home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts,limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    # Show
    return render(request, 'posts.html', {'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
