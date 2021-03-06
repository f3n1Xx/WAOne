"""WAOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from WAOne import views
from Page import views as page
from Post import views as post

urlpatterns = [
    # URLs for Main
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login),
    path('logout/', views.logout),

    # URLs for Blog
    path('blog/create', page.create_page),
    path('page/edit', page.edit_page),
    path('page/delete', page.del_page),

    # URLs for Post
    path('post/create', post.create_post),
    path('post/edit', post.edit_post),
    path('post/delete', post.del_post),
]
