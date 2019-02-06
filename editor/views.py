from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
# from .forms import RadioEditForm
from django.contrib.auth.models import User


def home(request):
    context = {
        'post': Post.objects.last(),
    }
    # context = None
    return render(request, 'editor/home.html', context=context)


def upload_img(request):
    if request.method == 'POST' and request.FILES['imgToUpload']:
        print(request.FILES.keys())
        img = request.FILES['imgToUpload']
        post = Post(name=img.name, image=img)
        post.save()
        context = {
            'title': 'Edit',
            'post': post,
        }
        return render(request, 'editor/edit.html', context=context)
    return redirect('/')


def edit(request):
    if request.method == 'POST':
        context = {
            'title': 'Edit',
            'post': Post.objects.last(),
        }

        return render(request, 'editor/edit.html', context=context)
