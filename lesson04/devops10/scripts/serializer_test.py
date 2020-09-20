import os
import sys


# 初始化
def setup():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    # print(BASEDIR)
    # print(os.path.abspath(os.path.join(BASEDIR, '..')))
    sys.path.insert(0, BASEDIR)
    sys.path.insert(0, os.path.abspath(os.path.join(BASEDIR, '..')))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops10.settings")

    import django
    django.setup()


# 业务逻辑
def logic():
    create_pub_1()

def test():
    from datetime import datetime
    from rest_framework import serializers


    class Comment(object):
        def __init__(self, email, content, created=None):
            self.email = email
            self.content = content
            self.created = created or datetime.now()

    comment = Comment(email='leila@example.com', content='foo bar')
    # print(comment)

    class CommentSerializer(serializers.Serializer):
        email = serializers.EmailField()
        content = serializers.CharField()
        created = serializers.DateTimeField()

    serializer = CommentSerializer(comment)
    print(serializer.data)





def create_pub_1():
    from book.models import Publisher
    from rest_framework import serializers
    from rest_framework.exceptions import ValidationError

    class PublisherSerializer(serializers.Serializer):
        name = serializers.CharField()
        address = serializers.CharField()

        # 字段验证
        def validate_name(self, value):
            if not (isinstance(value, str) and value.isupper()):
                raise ValidationError('必须小写')
            return value

        # 多字段全局验证
        def validate(self, data):
            """
            Check that start is before finish.
            """
            if data['name'].startswith('河南') and data['address'] == "河南":
                raise ValidationError("finish must occur after start")
            return data

        def create(self, validated_data):
            # send_mail ****
            return Publisher.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.address = validated_data.get('address', instance.address)
            instance.save()
            return instance



    p = Publisher(name='大家好', address='北京')
    # s = PublisherSerializer(p)
    # print(s.data)

    # Create
    # p = Publisher(name='大家好', address='北京')
    data = {'name': '211', 'address': '222'}
    # data = {'name': '2111'}
    s = PublisherSerializer(data=data)
    if s.is_valid():
        s.save()
    else:
        # print(s.error_messages)
        print(s.errors)
    # print(s.error_messages)

    #
    # # Update
    # p1 = Publisher.objects.get(pk=41)
    # data = {'name' : '11', 'address' : '2'}
    # s = PublisherSerializer(instance=p1, data=data)
    # print(s.is_valid())
    # print(s.save())

# 入口函数
def main():
    setup()

    logic()


if __name__ == '__main__':
    main()