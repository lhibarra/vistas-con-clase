"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SocialTravel.views import (index, mostra_otro_template, mostrar_pos, 
    agregar_post, buscar_post, PostList, PostDetail, PostDelete, PostUpdate, PostCreate,
    Login, Logout, SignUp, PostMineList
)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name= "index"),
    path('admin/', admin.site.urls),
    #path('mis-post/', mostra_otro_template, name="mis-post"), 
    path('mis-post/', mostrar_pos, name="mis-post"), #reutilizo la vista llamo a la otra funcion
    path('mis-post/agregar', agregar_post, name="agregar-post"),
    path('mis-post/buscar', buscar_post, name="buscar-post"),
    #urls con clases
    path('post/list',PostList.as_view(), name="post-list"),
    path('post/create', PostCreate.as_view(), name="post-create"),
    path('post/detail/<pk>', PostDetail.as_view(), name="post-detail"),
    path('post/delete/<pk>', PostDelete.as_view(), name="post-delete"),
    path('post/update/<pk>', PostUpdate.as_view(), name="post-update"),
    #url de sistema
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', SignUp.as_view(), name= "signup"),
    path('post/list/mine', PostMineList.as_view(), name="post-mine"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
