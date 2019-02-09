import os

from PIL import Image
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Post


def home(request):
    return render(request, 'editor/home.html')


def upload_img(request):
    if request.method == 'POST' and request.FILES['imgToUpload']:
        img = request.FILES['imgToUpload']
        post = Post(name=img.name, image=img)
        request.session['new_post'] = post
        post.save()
        context = {
            'title': 'Edit',
            'post': request.session['new_post'],
        }
        return render(request, 'editor/edit.html', context=context)
    return redirect('/')


def edit(request):
    if request.method == 'POST':
        post = request.session['new_post']
        im = Image.open(os.path.join(settings.MEDIA_ROOT, post.name))
        new_im = None
        if request.POST.get('crop'):
            print('crop')
            box = (int(request.POST["crop-left"]), int(request.POST["crop-upper"]),
                   int(request.POST["crop-right"]), int(request.POST["crop-lower"]))
            new_im = crop(im, box)
        elif request.POST.get('resize'):
            print('resize')
            size = (int(request.POST["resize-height"]), int(request.POST["resize-width"]))
            new_im = resize(im, size)
        elif request.POST.get('rotate'):
            print('rotate')
            new_im = rotate(im, int(request.POST["rotate-angle"]))
        elif request.POST.get('BAW'):
            print('BAW')
            new_im = black_and_white(im)
        elif request.POST.get('done'):
            post.delete()
            return redirect('/')
        elif request.POST.get('share'):
            post.is_share = True
            return render(request, 'editor/share.html', context={'title': 'Shared Photos', 'posts': Post.objects.all()})
        new_im.save(post.image.path, format='PNG')
        request.session['new_post'] = post
        context = {
            'title': 'Edit',
            'post': post,
        }
        return render(request, 'editor/edit.html', context=context)


def crop(im, box):
    return im.crop(box)


def resize(im, size):
    return im.resize(size)


def rotate(im, angle):
    return im.rotate(angle)


def black_and_white(im):
    return im.convert('1')
