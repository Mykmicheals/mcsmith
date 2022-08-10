from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('team', views.team, name='team'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app.views.page_not_found_view'
