from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from akoikelov.djazz.models import StaticInfo


class StaticInfoSerializer(ModelSerializer):

    field_name = CharField()
    value = CharField()
    info = CharField(read_only=True)

    class Meta:
        model = StaticInfo
        exclude = ()