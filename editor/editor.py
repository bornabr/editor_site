from PIL import Image
import os
from .models import Post
from django.conf import settings

# EDIT_CHOICES = {
#     'crop': crop,
#     'resize':
# }


def edit(request):
    post = request.session['new_post']
    im = Image.open(os.path.join(settings.MEDIA_ROOT, post.name))
    im.show()
    # im = Image.open(post.image)
    new_im = None
    if request.POST.get('crop'):
        box = (request.POST["crop-left"], request.POST["crop-upper"],
               request.POST["crop-right"], request.POST["crop-lower"])
        new_im = crop(im, box)
        request.POST['crop'] = None
    elif request.POST.get('resize'):
        size = (request.POST["resize-height"], request.POST["resize-width"])
        new_im = resize(im, size)
        request.POST['resize'] = None
    elif request.POST.get('rotate'):
        new_im = rotate(im, request.POST["rotate-angle"])
        request.POST['rotate'] = None
    elif request.POST.get('BAW'):
        new_im = black_and_white(im)
        request.POST['BAW'] = None
    new_post = Post(name=post.name, image=new_im)

    return new_post if new_post is not None else post


def crop(im, box):
    return im.crop(box)


def resize(im, size):
    return im.thumbnails(size)


def rotate(im, angle):
    return im.rotate(angle)


def black_and_white(im):
    return im.convert('1')
