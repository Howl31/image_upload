from django.shortcuts import render
from .models import User
# Create your views here.


def index(request):
    users = User.objects.all()
    pic_data = users[len(users)-1].pic
    # print(pic_data.url)
    return render(request, 'index.html', {'pic': pic_data.url})


def upload_image(request):
    img_name = request.FILES['image']
    user = User(pic=img_name)
    user.save()
    return render(request, 'index.html')
