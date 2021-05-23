from django.shortcuts import render
import datetime

def home_page_view(request):
    lista = ["HTML", "CSS", "Python", "Django"]
    context = {
        'agora': datetime.datetime.now(),
        'lista': lista,
    }
    return render(request, 'website/home.html', context)


def coment_page_view(request):
    return render(request,'website/Comentaries.html')
def images_page_view(request):
    return render(request,'website/images.html')
def Media_page_view(request):
    return render(request,'website/Media.html')