import json
from json import JSONDecodeError

from akoikelov.djazz.models import StaticInfo


def sic(request):
    info = StaticInfo.objects.first()

    if info is None:
        return None

    try:
        data = json.loads(info.info)
    except JSONDecodeError:
        return None

    return {
        'sic_data': data
    }