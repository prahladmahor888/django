from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from sqlalchemy.dialects.mssql.information_schema import views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="home"),
    path('docs', views.docs, name="docs"),
    path('example', views.examples, name="example"),
    path('reset', views.reset_pass, name="reset"),
    path('login', views.user_login, name="login"),
    path('signup', views.user_register, name="Signup"),
    path('logout', views.user_logout, name="logout"),
    path('new_pass', views.new_pass, name="New Password"),
    path('otp', views.otp, name="OTP Veryfication"),
    path('profile', views.profile, name='Profile'),
    path('editProfile', views.editProfile, name='Edit Profile'),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)