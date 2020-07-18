### 一、字段选项

#### 以下参数对所以字段类型均有效，且是可选的。

##### null 

数据库级别为空，默认为`False`  数据库不允许为null存储数据，

设置为`True`   该字段为空，Django 会将数据库中该字段设置为 `NULL`。



##### blank

admin form表单为空，默认为 `False`

设置为 `True` 则说明 该字段允许提交为空。



##### choices

有两个元素的迭代组成的序列(例如[(A, B)， (A, B)…])，作为字段的选择。如果给定了选项，则通过模型验证强制执行，默认的表单小部件将是一个带有这些选项的选择框，而不是标准的文本字段。

```python
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)
```

使用 [`get_FOO_display()`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#django.db.models.Model.get_FOO_display)  可以查看选择的元组人类可读值

```python
>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```

**每当 choices 的顺序变动时将会创建新的迁移。



##### db_column

此字段是指定数据库字段名。如果没有给出这个字段，Django将使用字段的名称。



##### db_index

数据库索引，默认为`False`

如果设置为`True` 则会创建该字段为索引字段



##### db_tablespace

为字段列索引指定可选的表空间。若此列没有索引，会忽略该选项。

若未指定 [`db_tablespace`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.db_tablespace) 和 [`DEFAULT_INDEX_TABLESPACE`](https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-DEFAULT_INDEX_TABLESPACE)，索引会在与数据表相同的表空间中创建。



##### default

该字段的默认值。可以是一个值或者是个可调用的对象。

如果是个可调用对象，每次实例化模型时都会调

```python
def contact_default():
    return {"email": "to1@example.com"}

contact_info = JSONField("ContactInfo", default=contact_default)

```

当创建新的模型实例并且没有为字段提供值时，将使用默认值。当字段是主键时，当该字段设置为None时也使用默认值。



##### editable

默认为 `True`

如果设置为 `False`  该字段将不会显示在admin或任何其他ModelForm中。在模型验证的时候会跳过该字段



##### error_messages

error messages参数自定义错误消息，覆盖字段将引发的默认消息。传入一个字典，其中的键与要覆盖的错误消息相匹配。（也就是：NON_FIELD_ERRORS要和错误消息相匹配）

错误消息键包括null、blank、invalid、invalid choice、unique和unique for date。



error_message 的注意事项：

在 [`表单字段`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/fields/#django.forms.Field.error_messages) 级别或者 [表单 Meta](https://docs.djangoproject.com/zh-hans/2.2/topics/forms/modelforms/#modelforms-overriding-default-fields) 级别定义的错误信息优先级总是高于在 [`模型字段`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.error_messages) 级别定义的。

在 [`模型字段`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.error_messages) 上定义的错误信息只有在 [模型验证](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#validating-objects) 步骤引发 `ValidationError` 时才会使用，并且没有在表单级定义相应的错误信息。



可以通过添加 [`NON_FIELD_ERRORS`](https://docs.djangoproject.com/zh-hans/2.2/ref/exceptions/#django.core.exceptions.NON_FIELD_ERRORS) 键到 `ModelForm` 内部的 `Meta` 类的 `error_messages` 中来覆盖模型验证引发的 `NON_FIELD_ERRORS` 错误信息。

```python
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
```



##### help_text 

额外的帮助文本，随表单控件一同显示。对生成文档也是很有作用



##### primary_key

默认为`False`

设置为`True` 表示该字段被设置为主键

primary key=True 意味着 null=False 和 unique=True。对象上只允许有一个主键。

注意：如果设置的模型中没有设置主键，django会自动设置一个自增字段（id）为主键



##### unique

默认为`False`

设置为`True` 这个字段必须在整个表中保持值唯一

此选项对除 ManyToManyField 和 OneToOneField 之外的所有字段类型有效。

注意：当 unique为True 时，不需要指定db索引，因为unique意味着创建索引。



##### unique_for_data

其设置为DateField或DateTimeField的名称，要求该字段对于日期字段的值是惟一的。



##### unique_for_month

跟 unique_for_date 类似，这里要求日期的月份唯一



##### unique_for_year

跟 unique_for_date 类似，这里要求日期的年份唯一



##### verbose_name

字段可读的名称。如果没有给出详细名称，Django将使用字段的属性名称自动创建它，将下划线转换为空格。



##### validators

要为该字段运行的验证器列表。admin 级别验证字段

1、定义validate规则：

```python
from django.core.exceptions import ValidationError

# admin 级别验证字段
def validate_publisher_state(value):
    if value not in [1, 2]:
        raise ValidationError("{} is not a true number!!!".format(value))
```

2、模型内引用

```python
class Book(models.Model):
    """
        图书
        foreginkey放在多的一边
    """

    PUBLISHER_STATE = (
        # 发布状态：数组，数字（数据库），文字：前端显示
        (1, '发行中'),
        (2, '已发行')
    )
    publisher_state = models.IntegerField(
        validators=[validate_publisher_state],
        choices=PUBLISHER_STATE,
        default=1,
        verbose_name='发行状态')
```



##### Registering and fetching lookups

字段实现查找注册API。该API可用于定制哪些查找可用于字段类，以及如何从字段获取查找。



### 二、字段类型

##### AutoFiled  自增字段

ID自动增长，django自动设置，也是主键



##### BigAutoField  大整数（自动增长）

64位整数，非常类似于AutoField，不同之处在于它保证可以容纳1到9223372036854775807之间的数字。



##### BigIntegerField 大整数

一个64位整数，非常类似于IntegerField，不同之处在于它保证可以容纳从-922337203685477575808到9223372036854775807的数字。此字段的默认表单窗口小部件是TextInput。



##### BinaryField 二进制

存储原始二进制数据的字段。

默认情况下，BinaryField 将 editable 设置为 False ，在这种情况下，它不能包含在 ModelForm 中。

注意：2.1版本之前，Older versions don't allow setting `editable` to `True`。



BinaryField 有一个额外可选的参数：

 `BinaryField.max_length` 字段的最大长度(以字符为单位) 如果超出了最大长度的话，会抛出ValidationError。



##### BooleanField 布尔值

当 Field.default 未定义时，BooleanField 的默认值为None。



##### CharField 字符串 类型

A string field, for small- to large-sized strings.



CharField有一个额外的参数：

`CharField.max_length`  字段的最大长度(以字符为单位) 如果超出了最大长度的话，会抛出ValidationError。



##### TextField 文本字符串

一个大的文本字段。这个字段的默认表单小部件是一个Textarea。



##### DateField  时间类型（年月日）

`DateField.auto_now`  每次保存对象时自动将字段设置为现在。用于“last-modified”时间戳。

设置：`auto_now=True`



`DateField.auto_now_add  ` 第一次创建时自动将字段设置为现在。用于创建时间戳。

设置：`auto_now_add=True`

auto now add、auto now和default选项是互斥的。三选一，不能组合。

注意：设置 auto now 或 auto now add 为 True 将导致该字段的 editable=False 和 blank=True 。



##### DateTimeField 时间类型（年月日时分秒）

日期和时间，在Python中由日期时间表示。datetime实例。

其他用法与DateField类似



注意：使用自定义时间格式 需要在django项目的setting配置

USE_L10N = False 

DATETIME_FORMAT = 'Y-m-d H:i:s' 



##### DecimalField 十进制数

一个固定精度的十进制数，在Python中由十进制实例表示。



`DecimalField.max_digits`

该数字中允许的最大位数。注意，这个数字必须大于或等于小数位数。

`DecimalField.decimal_places` 与该数字存储在一起的小数位数。

例子1：存储分辨率为2位小数的999以内的数字

```python
models.DecimalField(..., max_digits=5, decimal_places=2)
```

例子2：存储大约10亿的数字，其分辨率为小数点后10位

```python
models.DecimalField(..., max_digits=19, decimal_places=10)
```



##### DurationField 时间周期

用于存储时间周期的字段——在Python中按时间增量建模。



##### EmailField 邮箱类型

使用EmailValidator检查值是否是有效的电子邮件地址的CharField。



##### FileFiled 文件上传

文件上传字段

两个可选参数：

`FileField.upload_to`

这个属性提供了一种设置上传目录和文件名的方法，可以通过两种方式进行设置。在这两种情况下，值都传递给Storage.save()方法。

如果指定字符串值，则它可能包含 strftime() 格式，该格式将被文件上载的日期/时间替换（以使上载的文件不会填满给定目录）。

例如：

```python
class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
```



upload_to也可以接收调用一个函数。 这将被调用以获得上载路径，包括文件名。 该可调用对象必须接受两个参数，并返回要传递给存储系统的Unix样式的路径（带有正斜杠）。 这两个参数是：

参数一：instance：

定义FileField的模型实例。 更具体地说，这是附加当前文件的特定实例。



参数二：filename

最初给文件的文件名。

```python
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
```



如果使用FileFiled和Imange 需要注意一下几点：

1、在你的 setting 文件中，你需要定义：setting: MEDIA_ROOT 作为 Django 存储上传文件目录的完整路径。

2、将FileField或ImageField添加到模型中，定义upload to选项，以指定 MEDIA_ROOT 的子目录，用于上载文件。

3、将存储在数据库中的所有文件都是该文件的路径（相对于MEDIA_ROOT）。很可能想使用Django提供的便捷url属性。



##### FilePathField

一个CharField，其选择仅限于文件系统上某个目录中的文件名。 具有三个特殊参数，其中第一个是必需的：

`FilePathField.path` 必须的参数，目录的绝对文件系统路径，应从中选择此FilePathField

`FilePathField.match` 可选参数，FilePathField将用于过滤文件名的正则表达式（作为字符串）。 请注意，正则表达式将应用于基本文件名，而不是完整路径

```python
FilePathField(path="/home/images", match="foo.*", recursive=True)
```



##### FloatField 浮点类型

在Python中由浮点实例表示的浮点数。



##### FloadField 与 DecimalField的区别

虽然它们都表示实数，但它们表示的数字不同。FloatField在内部使用Python的float类型，而DecimalField使用Python的Decimal类型。



##### ImageField 图像类型

从FileField继承所有属性和方法，但还验证上载的对象是有效的图像。

两个参数：

height_field：每次保存模型实例时，模型字段的名称都会自动填充图像的高度。

width_field：每次保存模型实例时，模型字段的名称都会自动填充图像的宽度。

ImageField实例在数据库中创建为varchar列，默认最大长度为100个字符。 与其他字段一样，您可以使用max_length参数更改最大长度。



##### IntegerField  整数类型

一个整数。在Django支持的所有数据库中，从-2147483648到2147483647的值是安全的。



##### GenericIPAddressField  字符串格式 IPv4或IPv6地址

字符串格式的IPv4或IPv6地址（例如192.0.2.30或2a02：42fe :: 4）

参数：

protocol：可接受的值为“ both”（默认），“ IPv4”或“ IPv6”

unpack_ipv4：解压缩IPv4映射的地址，例如:: ffff：192.0.2.1。 如果启用此选项，则该地址将解压缩为192.0.2.1。 默认设置为禁用。 只能在协议设置为 “ both” 时使用。



##### NullBooleanField  和Bool一样

像BooleanField一样为null = True。 使用该字段代替该字段，因为在将来的Django版本中可能会不推荐使用该字段。



##### PositiveIntegerField  可以从0开始的正整数

类似于IntegerField，但必须为正数或零（0）。 在Django支持的所有数据库中，0到2147483647之间的值都是安全的。可以接受值0。



##### PositiveSmallIntegerField  类似于PositiveIntegerField

类似于PositiveIntegerField，但仅允许在特定点（与数据库有关）下的值。 在Django支持的所有数据库中，0到32767的值都是安全的。



##### SmallIntegerField 小整数

类似于IntegerField，但只允许特定(数据库依赖)点下的值。在Django支持的所有数据库中，-32768到32767的值是安全的。



##### SlugField 设置接受unicode字母

slug是某物的短标签，只包含字母、数字、下划线或连字符。它们通常在url中使用。可以指定max length，默认长度是50

意味着将Field.db_index设置为True。

allow_unicode参数：如果为真，则该字段除了接受ASCII字母外，还接受Unicode字母



##### TextField 大文本字段

一个大的文本字段。



##### TimeField 时间类型字段

在Python中由datetime.time实例表示。 接受与DateField相同的自动填充选项。



##### URLField url字段类型

URL的CharField，由URLValidator验证。

URLField使用可选的 max_length 参数。如果不指定最大长度，则使用默认值200。



##### UUIDField uuid类型

存储为uuid数据类型，否则存储为char(32)。

通用唯一标识符是primary_key的自动字段的很好替代。 数据库不会为您生成UUID，因此建议使用default：

```python
import uuid
from django.db import models

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other fields
```



### 三、关系关系字段

##### ForeignKey  外键

多对一的关系。需要两个位置参数：被关联的类和 [`on_delete`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete) 选项

```python
from django.db import models

class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
    )
    # ...

class Manufacturer(models.Model):
    # ...
    pass
```

参数：on_delete

CASCADE 默认的选项，级联删除

PROTECT 保护模式。删除的时候会抛出ProtectedError 错误。

SET_NULL 置空模式。删除的时候，外键字段被设置为空，前提是blank=True, null=True,定义该字段的时候，允许为空。

SET_DEFAULT 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候需要加上一个默认值。

SET() 自定义一个值，该值当然只能是对应的实体的

DO_NOTHING 不操作。



##### 抽象基类

抽象基类在你要将公共信息放入很多模型时会很有用。编写你的基类，并在 [Meta](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#meta-options) 类中填入 `abstract=True`。该模型将不会创建任何数据表。当其用作其它模型类的基类时，它的字段会自动添加至子类。



##### ManyToManyField 多对多

多对多关系。 需要一个位置参数：与模型相关的类，其作用与对ForeignKey完全相同，包括递归和惰性关系。



##### OneToOneField 一对一

多表继承是通过从子模型到父模型添加隐式一对一关系来实现的。















