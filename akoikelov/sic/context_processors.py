import json
from json import JSONDecodeError

from akoikelov.sic.models import StaticInfo


def sic(request):
    info = StaticInfo.objects.first()

    if info is None:
        return {}

    try:
        data = json.loads(info.info)
    except JSONDecodeError:
        return {}

    return {
        'sic_data': data
    }