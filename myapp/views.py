from django.shortcuts import render
from django.views import generic
from .models import*
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .forms import RapistForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class RapistDetail(DetailView):
    model = Tourism
    context_object_name = 'post'
    template_name = "myapp/post.html"

class PostLIst(ListView):
    model = Tourism
    form_class = RapistForm
    
    template_name = 'myapp/index.html'
    ordering = ['-id']
    allusers= get_user_model().objects.all()


        

   

            


class AddRppist(CreateView):
    model = Tourism 
    form_class = RapistForm
    template_name='myapp/add_rapist.html'
    success_url = reverse_lazy('home')
    

class UpdateRapist(UpdateView):
    model = Tourism
    template_name = 'myapp/update.html'
    fields = '__all__'


class DeleteRapist(DeleteView):
    model = Tourism
    template_name = 'myapp/delete_rapist.html'
    success_url = reverse_lazy('home')




#User Register part

class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'myapp/register.html'
    success_url = reverse_lazy('login')




def index(request):
    users = User.objects.all()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
    context = {'visitor':num_visits,'users':users}
    return render(request,'myapp/index.html',context=context)



def showthis(request):

    all_users= get_user_model().objects.all().order_by('-id')[0:20]
    object_lists = Tourism.objects.all().order_by('-id')
    
    context= {'allusers': all_users,'object_list':object_lists}
        
    return render(request, 'myapp/index.html', context)

def allBlog(request):

    blogs = Tourism.objects.all()
    context = {'blogs':blogs}
    return  render(request,'myapp/blogs.html',context)

def search(request):
    if request.method=='get':
        sr = request.GET.get('s')
        result = Tourism.objects.filter(place__icontains=sr)
        context = {'resutl':result}
        return render(request,'myapp/search.html',context)


def author(request):
    
    return render(request,'myapp/author.html')




