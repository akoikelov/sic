import json

from rest_framework.generics import UpdateAPIView

from akoikelov.djazz.models import StaticInfo
from akoikelov.djazz.serializers import StaticInfoSerializer


class UpdateStaticInfoView(UpdateAPIView):
    serializer_class = StaticInfoSerializer
    permission_classes = ()
    authentication_classes = ()

    def perform_update(self, serializer):
        data = serializer.validated_data

        field_name = data['field_name']
        value = data['value']
        current_value = serializer.instance.info

        if isinstance(current_value, str):
            current_value = json.loads(current_value)

        current_value[field_name] = value

        serializer.save(info=json.dumps(current_value))

    def get_object(self):
        info = StaticInfo.objects.first()

        if info is None:
            info = StaticInfo.objects.create(info={})

        return info

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)