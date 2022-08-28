from django.contrib import admin
from django.urls import path
from django.urls import re_path
from rango import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category, name='show_category'),
    re_path(r'^add_category/$', views.add_category, name='add_category'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    re_path(r'^register_profile/$', views.register_profile, name='register_profile'),
    #re_path(r'^register/$',views.register,name='register'),
    #re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^restricted/', views.restricted, name='restricted'),
    #re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    re_path(r'^profiles/$', views.list_profiles, name='list_profiles'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)