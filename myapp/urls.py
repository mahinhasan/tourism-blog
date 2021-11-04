from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import*
from .import views
urlpatterns = [
    
    path('',PostLIst.as_view(),name='home'),
    path('blog-post /<int:pk>',RapistDetail.as_view(),name='rapist-detail'),
    path('create_post',AddRppist.as_view(),name='addrapist'),
    path('update/<int:pk>',UpdateRapist.as_view(),name='update'),
    path('delete/<int:pk>/remove',DeleteRapist.as_view(),name='delete'),
    path('register',UserRegister.as_view(),name = 'register'),
    path('visitor',views.index,name='visitor'),
    path('users',views.showthis,name='users'),
    path('blogs',views.allBlog,name='blogs'),
    path('search',views.search,name='search')



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
