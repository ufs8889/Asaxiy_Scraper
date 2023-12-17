from django.contrib import admin
from django.urls import include, path
from main.views import *

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]

handler404 = custom_404
handler500 = custom_500