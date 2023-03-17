"""applytracker URL Configuration

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
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from applytrackerapi.views import register_user, login_user
from rest_framework import routers
from applytrackerapi.views import JobView
from applytrackerapi.views import ResumeView
from applytrackerapi.views import Cover_LetterView
from applytrackerapi.views import CompanyView
from applytrackerapi.views import ContactView
from applytrackerapi.views import RoleView
from applytrackerapi.views import Job_ServiceView
from applytrackerapi.views import InterviewView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'jobs', JobView, 'job')
router.register(r'resumes', ResumeView, 'resume')
router.register(r'cover_letters', Cover_LetterView, 'cover_letter')
router.register(r'companies', CompanyView, 'company')
router.register(r'contacts', ContactView, 'contact')
router.register(r'roles', RoleView, 'role')
router.register(r'interviews', InterviewView, 'interview')
router.register(r'job_services', Job_ServiceView, 'job_service')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
