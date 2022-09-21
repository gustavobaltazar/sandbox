from dataclasses import fields
from decimal import Decimal
from rest_framework import serializers
from listpage.models import Bosses

class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bosses
        fields = ['id', 'name', 'location', 'boss_image', 'loot']