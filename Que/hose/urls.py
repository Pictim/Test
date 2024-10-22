from django.urls import path
from . import views
from hose.views import HoseAPIView

urlpatterns = [
    path('', views.glavnpage, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('api/v1/hoselist', HoseAPIView.as_view()),
]