from django.urls import path
from . import views


# path() 함수 : URL string, View Function, URL Pattern Name
urlpatterns= [    
    path('', views.base, name='base'),                       # 127.0.0.1:8000/app/
    path('hello/', views.greeting, name='hello'),            # 127.0.0.1:8000/app/hello/
    path('member/', views.members, name='member'),           # 127.0.0.1:8000/app/member/
]
