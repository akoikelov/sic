from akoikelov.djazz.models import StaticInfo


def sic(request):
    return {
        'sic_data': StaticInfo.objects.first()
    }