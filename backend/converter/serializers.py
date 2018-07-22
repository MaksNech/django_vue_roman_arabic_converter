from rest_framework import serializers

from .models import Numeral


class NumeralSerializer(serializers.ModelSerializer):

    class Meta:
        model = Numeral
        fields = ('id', 'num_value', 'num_type', 'parent_textarea_id')
