from . import views
from django.urls import path
from django.urls import path


app_name='credentials'
urlpatterns = [ 
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('application',views.application,name='application'),

    path('applicationform/', views.applicationform, name='applicationform'),
    
    # path('get-cities/', views.get_cities, name='get-cities'),
    
]


