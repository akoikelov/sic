import json

from django.test import TestCase
from django.urls import reverse

from akoikelov.sic.models import StaticInfo


class TestUpdateStaticInfoView(TestCase):

    def test_view(self):
        self.client.post(reverse('si_update'), data={
            'field_name': 'phone',
            'value': '777777777'
        })

        info = StaticInfo.objects.first()
        self.assertIsNotNone(info)

        info_json = json.loads(info.info)

        self.assertTrue('phone' in info_json)
        self.assertEqual(info_json['phone'], '777777777')

