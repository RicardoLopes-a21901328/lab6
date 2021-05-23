from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page_view, name='home'),
    path('image',views.images_page_view, name='image'),
    path('Coment', views.coment_page_view, name='Coment'),
    path('Media', views.Media_page_view, name='Media')

]