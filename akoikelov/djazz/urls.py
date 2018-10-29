from django.conf.urls import url

from akoikelov.djazz.views import UpdateStaticInfoView

urlpatterns = [
    url('^si/update/$', UpdateStaticInfoView.as_view(), name='si_update'),
]