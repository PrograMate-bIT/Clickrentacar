"""Clickrentacar URL Configuration

The `urlpatterns` list routes URLs to frontViews. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function frontViews
    1. Add an import:  from my_app import frontViews
    2. Add a URL to urlpatterns:  path('', frontViews.home, name='home')
Class-based frontViews
    1. Add an import:  from other_app.frontViews import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('cracAPP.urls')),
    path('admin/', admin.site.urls),
]
