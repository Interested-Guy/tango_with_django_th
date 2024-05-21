"""tango_with_django_project URL Configuration

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
from registration.backends.simple.views import RegistrationView
from django.contrib import admin
from django.urls import path, include
from rango import views
from predict_score import views as pviews
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/rango/register_profile'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^rango/', include('rango.urls')),
    re_path(r'^accounts/register/$',MyRegistrationView.as_view(),name='registration_register'),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    re_path(r'^dummy/', views.dummy, name='dummy'),
    re_path(r'^clear/', views.clear, name='clear'),
    re_path(r'^graph/', views.graph, name='graph'),
    re_path(r'^fetch_data/', views.fetch_data, name='fetch_data'),
    re_path(r'^score_prediction/', include('predict_score.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
