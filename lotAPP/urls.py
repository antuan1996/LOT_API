from django.conf.urls import url

from .views import \
    (CreateUserView,
     CreateLot,
     ListLots,
     ListActiveLots,
     ListDeactiveLots,
     OneInfoLot,
     BetOnLot,
     MyBets,
     )

from rest_framework.authtoken import views

urlpatterns = [
    url(r'^mybets/$', MyBets.as_view(), name='MyBets'),
    url(r'^bet/$',BetOnLot.as_view(),name='betOnLot'),
    url(r'^lot/(?P<pk>\d+)/$', OneInfoLot.as_view(), name='info-lot'),
    url(r'^deactive/$', ListDeactiveLots.as_view(), name='deactiveLots'),
    url(r'^active/$', ListActiveLots.as_view(), name='activeLots'),
    url(r'^createLot/$', CreateLot.as_view(), name='createLOT'),
    url(r'^register/$', CreateUserView.as_view(), name='register'),
    url(r'^all/$', ListLots.as_view(), name='all lots'),
    url(r'^$', views.obtain_auth_token, name='auth'),
]
