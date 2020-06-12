from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',jobs.views.home,name='home'),
] + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
