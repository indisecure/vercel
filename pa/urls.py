from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from toy.views import index,contact,course,alumni,c,java,python,web,leads,sitemap,robot
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('contact/',contact,name='contact'),
    path('course/',course,name='course'),
    path('alumni/',alumni,name='alumni'),
    path('c/',c,name='c'),
    path('python/',python,name='python'),
    path('java/',java,name='java'),
    path('web/',web,name='web'),
    path('leads/',leads,name='leads'),
    path('sitemap.xml/',sitemap,name='sitemap.xml'),
    path('robots.txt/',robot,name='robots.txt'),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)