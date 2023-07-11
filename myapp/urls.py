from django.urls import path
from . import views


# path() 함수 : URL string, View Function, URL Pattern Name
urlpatterns= [    
    path('', views.main, name='main'),                                      # 127.0.0.1:8000/
    path('hello/', views.greeting, name='hello'),                           # 127.0.0.1:8000/hello/
    path('members/', views.members, name='members'),                        # 127.0.0.1:8000/members/
    path('members/details/<int:id>', views.details, name='details'),        # 127.0.0.1:8000/details/5
]
