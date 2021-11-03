from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views
from .import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),  
    path('login/',LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]+ static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
