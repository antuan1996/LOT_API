from rest_framework import serializers
from django.contrib.auth import get_user_model
from lotAPP.models import Lot, Bet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, allow_blank=False, style={'input_type':'password'})
    email = serializers.EmailField(allow_blank=False)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )

        user.set_password(validated_data['password'])


        user.save()

        return user


    class Meta():
        model = get_user_model()
        fields = ('username', 'password', 'email')


class LotSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        lot = Lot.objects.create(
            lot_name = validated_data['lot_name'],
            lot_price = validated_data['lot_price'],
            lot_price_step = validated_data['lot_price_step'],
            lot_text = validated_data['lot_text'],
            lot_author = User.objects.get(id=validated_data['lot_author'])
        )

        lot.save()

        return lot


    class Meta():
        model = Lot
        fields = ('id','lot_name', 'lot_price', 'lot_price_step', 'lot_text', 'lot_status')


class BetSerializer(serializers.ModelSerializer):

    class Meta():
        model = Bet
        fields = ('bet_on_lot', 'bet_sum', )

class LotAndBetSerializer(serializers.ModelSerializer):

    bets = BetSerializer(many=True, read_only=True)

    class Meta():
        model = Lot
        fields = ('id','lot_name', 'lot_price', 'lot_price_step', 'lot_text', 'lot_status', 'bets', )