from .serializers import UserSerializer, LotSerializer, BetSerializer, LotAndBetSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from .models import Lot, Bet

class CreateUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class LotListCreate(ListCreateAPIView):
    serializer_class = LotSerializer
    queryset = Lot.objects.all()
    filter_fields = ('status',)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class OneInfoLot(RetrieveAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotAndBetSerializer


class BetOnLot(CreateAPIView):
    serializer_class = BetSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class MyBets(ListAPIView):
    serializer_class = BetSerializer

    def get_queryset(self):
        queryset = Bet.objects.filter(author=self.request.user.id)
        return queryset
