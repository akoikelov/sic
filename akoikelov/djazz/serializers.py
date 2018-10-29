from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class StaticInfoSerializer(Serializer):

    field_name = CharField(required=True)
    value = CharField(required=True)