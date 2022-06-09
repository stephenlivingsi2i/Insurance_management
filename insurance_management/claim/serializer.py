from rest_framework import serializers
from utils.dynamic_serializer import DynamicFieldsModelSerializer

from claim.models import Claim


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'
