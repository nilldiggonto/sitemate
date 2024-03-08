
from django.contrib import admin
from django.urls import path,include
from frontend.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('api/', include('tasks.urls')),
]
