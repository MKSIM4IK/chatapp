from django.urls import path
from chatapp.views import index

urlpatterns = [
    path('room/<str:room_name>/', index, name='chat'),

]
