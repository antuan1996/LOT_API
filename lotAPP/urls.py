from django.conf.urls import url
from .views import \
    (CreateUser,
     LotListCreate,
     OneInfoLot,
     BetOnLot,
     MyBets,
     )
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^mybets/$', MyBets.as_view(), name='MyBets'),
    url(r'^bet-create/$', BetOnLot.as_view(), name='betOnLot'),
    url(r'^lot/(?P<pk>\d+)/$', OneInfoLot.as_view(), name='info-lot'),
    url(r'^lots/$', LotListCreate.as_view(), name='all lots'),
    url(r'^get-token/$', views.obtain_auth_token, name='auth'),
    url(r'^create-user/$', CreateUser.as_view(), name='register'),
]
