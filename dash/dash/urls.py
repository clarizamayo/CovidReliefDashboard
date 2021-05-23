"""dash URL Configuration

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
from django.conf import settings
from django.conf.urls import handler404, handler500, handler403, handler400
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('first_diagram.html', views.first_diagram, name='first_diagram'),
    path('second_diagram.html', views.second_diagram, name='second_diagram'),
    path('third_diagram.html', views.third_diagram, name='third_diagram'),
    path('bokeh.html', views.bokeh, name='bokeh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = views.handler404
handler500 = views.handler500
handler403 = views.handler403
handler400 = views.handler400