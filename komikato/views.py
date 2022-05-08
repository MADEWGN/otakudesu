from django.shortcuts import render

def index(request):
    return render(request, 'otakudesu2/index.html', context={})

def handle_not_found(request, exception):
    return render(request, '404.html', context={})

# 400 handle
def handle_bad_request(request, exception):
    return render(request, '400.html', context={})

def bookmark(request):
    return render(request, 'bookmark.html', context={})
