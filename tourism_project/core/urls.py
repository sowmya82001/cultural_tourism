from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('home/', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forget-password/', views.forget_password_view, name='forget_password'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('', views.home, name='home'),
    path('packages/', views.packages, name='packages'),
    path('destination/', views.destination, name='destination'),
    path('reviews/', views.reviews, name='reviews'), 
    path('contact/', views.contact, name='contact'),
    path('guides/', views.guide_list, name='guide_list'),
    path('guides/add/', views.add_guide, name='add_guide'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)