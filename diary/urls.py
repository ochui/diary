from django.contrib import admin
from django.urls import path, include
from accounts.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('martor/', include('martor.urls')),
]
