from django.db.models import Model, TextField


class StaticInfo(Model):

    info = TextField(null=False)