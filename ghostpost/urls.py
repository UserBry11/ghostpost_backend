"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from ghostpost import views
from ghostpost.models import BoastRoast
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'boastroast', views.BoastRoastViewSet)

admin.site.register(BoastRoast)

urlpatterns = [
    path('', admin.site.urls),
    # path('', views.index, name="homepage"),
    # path('addform/', views.add_form),
    # path('up/<int:id>/', views.upvote),
    # path('down/<int:id>/', views.downvote),
    path('api/', include(router.urls))
]
