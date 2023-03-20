from django.shortcuts import render
from SocialTravel.models import Post
from SocialTravel.forms import PostForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
ListView, DetailView, DeleteView, CreateView, UpdateView, FormView, )
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, "SocialTravel/index.html")

def mostra_otro_template(request):
    posts = Post.objects.all()
    return render(request, "SocialTravel/otro_template.html", { "posts":posts})

def mostrar_pos(request):
    contex = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    return render (request,"SocialTravel/admin_post.html", contex)

def agregar_post(request):
    form_post = PostForm(request.POST)
    form_post.save()#Construyo objeto tipo PosForm con los datos carfagos por el usuario
    contex = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    return render (request, "SocialTravel/admin_post.html", contex)

def buscar_post(request):
    criterio = request.GET.get("criterio")
    contex = {
        "posts": Post.objects.filter(carousel_caption_title__icontains = criterio).all(),  
        
    }
    return render(request, "SocialTravel/admin_post.html", contex)

class PostList(ListView):
    model = Post
    context_object_name ="posts"


class PostMineList(LoginRequiredMixin, PostList):

    def get_queryset(self):
        return Post.objects.filter(publisher=self.request.user.id).all()




class PostDetail(DetailView):
    model = Post
    context_object_name = "post"


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")
    def test_func(self):
        user_id = self.request.user.id
        post_id =  self.kwargs.get("pk")
        return Post.objects.filter(publisher=user_id, id=post_id).exists()

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('post-list')
    fields = '__all__'
    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")#kwargs es un atributo dicc de self
        return Post.objects.filter(publisher=user_id, id=post_id).exists()



class PostSearch(ListView):
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Post.objects.filter(
            carousel_caption_title__icontains=criterio).all()
        return result


class Login(LoginView):
    next_page = reverse_lazy("index")

class Logout(LogoutView):

    template_name = "registration/logout.html"


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('post-list')


