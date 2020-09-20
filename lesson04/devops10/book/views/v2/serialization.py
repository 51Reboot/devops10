from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.validators import UniqueTogetherValidator


from book.models import Publisher
from book.models import Book


class PublisherSerializer(serializers.ModelSerializer):


    def validate_name(self, attrs):
        print("validate_name 局部验证", attrs)
        if 'G' in attrs:
            raise exceptions.ValidationError('不合法 不能出现G')
        return attrs

    def validate(self, attrs):
        print("validate 全局验证", attrs)
        if attrs['address'] not in attrs['name']:
            raise exceptions.ValidationError('不合法 {}地址必须在名称中出现'.format(attrs['address']))
        return attrs

    class Meta:
        model = Publisher
        fields = "__all__"
        # fields = ('pk', 'name', 'address')  # 序列化返回的字段

        extra_kwargs = {
            "address": {
                # 'write_only': True  # 反序列化可传可不传
                'required': True  # 反序列化可传可不传
            },
            "name": {
                "max_length": 10,
                # "min_length": 10,
                "error_messages": {
                    'max_length': "长度只能10",
                }
            },
        }

        validators = [
            UniqueTogetherValidator(
                queryset=Publisher.objects.all(),
                fields=['name']
            )
        ]


class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        depth = 1