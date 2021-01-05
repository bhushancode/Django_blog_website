from django.shortcuts import render

# Create your views here.
def generate_(request):
    context= {
        "variable1": "variable1"
    }
    return render(request, 'index.html', context)

def profile(request):
    return render(request, 'profile.html')

def blog(request):
    return render(request, 'post.html')

def login(request):
    return render(request, 'login.html')