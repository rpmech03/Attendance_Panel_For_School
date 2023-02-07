from django.urls import path,include
from . import views

urlpatterns = [
    # path('', views.signup,name='signup'),
    # path('signin/', views.signin,name='signin'),
    path('', views.home,name='home'),
]