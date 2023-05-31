from django.urls import path, include
from django.contrib import admin

from adminplus.sites import AdminSitePlus


admin.site = AdminSitePlus()
admin.autodiscover()

urlpatterns = [
    path('admin/', include(admin.site.urls)),
]
