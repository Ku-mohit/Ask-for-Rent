"""askForRent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import indexController
from . import loginController
from . import signupController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',indexController.Index),
    path('login/',loginController.login),
    path('signup/',signupController.signup),
    path('submituser',signupController.Submit_User),
    path('checkuserlogin',loginController.CheckUserLogin),
    # path('adminlogout/',Admin_Controller.AdminLogout),
    
]
