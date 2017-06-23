from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^charter/', include('charter.urls')),
    url(r'^admin/', admin.site.urls),
]