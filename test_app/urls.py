from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from test_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('akoikelov.sic.urls')),
    url(r'^si_constructor/$', StaticInfoConstructorView.as_view(), name='si_constructor'),
]