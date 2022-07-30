from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
import cafe
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cafe.urls'))
]
