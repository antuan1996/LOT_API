from .serializers import UserSerializer, LotSerializer, BetSerializer, LotAndBetSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Lot, Bet
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status



class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)

    serializer_class = UserSerializer

class CreateLot(CreateAPIView):
    model = Lot
    permission_classes = (IsAuthenticated, )

    serializer_class = LotSerializer


    def perform_create(self, serializer):
        return serializer.save(lot_author = self.request.user.id)


class ListLots(ListAPIView):
    model = Lot
    permission_classes = (IsAuthenticated,)

    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class ListActiveLots(ListAPIView):
    model = Lot
    permission_classes = (IsAuthenticated,)

    serializer_class = LotSerializer

    def get_queryset(self):
        queryset = Lot.objects.filter(lot_status=True)

        return queryset

class ListDeactiveLots(ListAPIView):
    model = Lot
    permission_classes = (IsAuthenticated,)

    serializer_class = LotSerializer

    def get_queryset(self):
        queryset = Lot.objects.filter(lot_status=False)

        return queryset


class OneInfoLot(RetrieveAPIView):

    model = Lot
    permission_classes = (IsAuthenticated, )
    queryset = Lot.objects.all()

    serializer_class = LotAndBetSerializer


class BetOnLot(CreateAPIView):

    model = Bet
    permission_classes = (IsAuthenticated,)

    serializer_class = BetSerializer

    def create(self, request, *args, **kwargs):

        id_num = request.data.get('bet_on_lot')

        if self.request.user.id == Lot.objects.get(id=id_num).lot_author.id:
            return Response({'Error': 'Вы не можете сделать ставку так как являетесь хозяином этого лота.'})


        else:

            try:

                bet_sum = int(request.data.get('bet_sum'))
                obj = Lot.objects.get(id=id_num)

                if obj.lot_status == True:

                    if (bet_sum>obj.lot_price) and ((bet_sum-obj.lot_price) == obj.lot_price_step):

                        bet = Bet()
                        bet.bet_author = User.objects.get(id=request.user.id)
                        bet.bet_on_lot = obj
                        bet.bet_sum = bet_sum

                        obj.lot_price = bet_sum

                        obj.save()
                        bet.save()


                        serializer = BetSerializer(bet)

                        return Response(serializer.data, status=status.HTTP_201_CREATED)

                    else:
                        return Response({'Error':'Сумма ставки меньше существующей цены или сумма ставки не соответсвует шагу цены'}, status=status.HTTP_400_BAD_REQUEST)


                else:
                    return Response({'lot_status':'Завершенный лот, нельзя сделать ставку.'},status=status.HTTP_400_BAD_REQUEST)


            except ValueError:
                return Response({'error': 'Неправильно введена сумма ставки'}, status = status.HTTP_400_BAD_REQUEST)


class MyBets(ListAPIView):
    model = Lot
    permission_classes = (IsAuthenticated,)

    serializer_class = BetSerializer


    def get_queryset(self):
        queryset = Bet.objects.filter(bet_author=self.request.user.id)

        return queryset

