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
    url(r'^mybets/$', MyBets.as_view(), name='MyBets'),  # just 'bets'
    url(r'^bet-create/$', BetOnLot.as_view(), name='betOnLot'),  # POST on 'lots/<lot_id>/bets'
    url(r'^lot/(?P<pk>\d+)/$', OneInfoLot.as_view(), name='info-lot'),  # prefer 'lots',
    url(r'^lots/$', LotListCreate.as_view(), name='all lots'),
    url(r'^get-token/$', views.obtain_auth_token, name='auth'),
    url(r'^create-user/$', CreateUser.as_view(), name='register'),
]

# Do not user 'create', 'update' or 'delete' in URLs. Use different request types for it