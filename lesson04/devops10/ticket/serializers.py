from rest_framework.serializers import ModelSerializer

from .models import Classify
from .models import TplInfo


class ClassifyModelSerializer(ModelSerializer):

    class Meta:
        model = Classify
        fields = "__all__"


class TplInfoModelSerializer(ModelSerializer):

    class Meta:
        model = TplInfo
        fields = "__all__"