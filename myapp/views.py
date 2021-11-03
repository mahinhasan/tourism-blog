from django.shortcuts import render
from django.views import generic
from .models import*
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .forms import RapistForm
from django.urls import reverse_lazy

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
    paginate_by = 2


class AddRppist(CreateView):
    model = Tourism 
    form_class = RapistForm
    template_name='myapp/add_rapist.html'
    success_url = reverse_lazy('home')
    

class UpdateRapist(UpdateView):
    model = Tourism
    template_name = 'myapp/update.html'
    fields = '__all__'


class DeleteRapist(DetailView):
    model = Tourism
    template_name = 'myapp/delete_rapist.html'
    success_url = reverse_lazy('home')




#User Register part

class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'myapp/register.html'
    success_url = reverse_lazy('login')




def index(request):

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
    context = {'visitor':num_visits}
    return render(request,'myapp/home.html',context=context)







