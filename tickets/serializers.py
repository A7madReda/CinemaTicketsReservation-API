from rest_framework import serializers
from tickets.models import Guest, Movie, Reservition


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class ReservitionSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Reservition
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields = [
            'pk', 'reservation', 'name', 'mobile' 
            ]