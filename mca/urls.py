


from mca import views
from django.urls import path

from django.contrib.auth.views import LoginView
urlpatterns = [

    path('west/', views.submitform),
    path('login/', views.login),

]
