### field options
#### Field.null
```
如果设置为 True， 当该字段为空时，Django 会将数据库中该字段设置为 NULL，默认为 False。

避免在基于字符串的字段（例如 CharField 和 TextField）上使用 null。如果字符串字段的 null=True，那意味着对于“无数据”有两个可能的值：NULL 和空字符串。在大多数情况下，对于“无数据”声明两个值是赘余的，Django 的惯例是使用空字符串而不是 NULL。 一个例外是当 CharField 同时具有 unique=True 和 blank=True 时。 在这种情况下，需要设置 null=True，以便在使用空白值保存多个对象时避免唯一的约束违规。
```

#### Field.blank
```
如果设置为 True ，该字段允许为空。默认为 False 。
```

#### Field.choices
```
一种由恰好有两个元素的迭代组成的序列(例如[(A, B)， (A, B)…])，作为字段的选择。如果给定了选项，则通过模型验证强制执行，默认的表单小部件将是一个带有这些选项的选择框，而不是标准的文本字段。
```

#### Field.db_column
```
此字段要使用的数据库列的名称。如果没有给出这个字段，Django将使用字段的名称。
```

#### Field.db_index
```
如果值为true，则创建索引。创建索引使用。
```

#### Field.db_tablespace
```
如果该字段有索引，则用于该字段索引的数据库表空间的名称。默认值是项目的DEFAULT_INDEX_TABLESPACE设置(如果设置)，或者模型的db_tablespace设置(如果有的话)。如果后端不支持表空间作为索引，则忽略此选项。
```
#### Field.default
```
该字段的默认值。可以是一个值或者是个可调用的对象，如果是个可调用对象，每次实例化模型时都会调用该对象。
```

#### Field.editable
```
如果为False，该字段将不会显示在admin或任何其他ModelForm中。在模型验证期间也会跳过它们。默认是Ture。
```

#### Field.error_messages
```
error_messages参数允许覆盖字段将引发的默认消息。传入一个字典，其中的键与要覆盖的错误消息相匹配。
错误消息键包括null、blank、invalid、invalid_choice、unique和unique_for_date。下面的字段类型部分为每个字段指定了附加的错误消息键。
```
#### Field.help_text
```
额外的帮助文本，随表单控件一同显示。即便你的字段未用于表单，它对于生成文档也是很有用的。
```
#### Field.primary_key
```
如果设置为 True ，将该字段设置为该模型的主键。
```

#### Field.unique
```
如果设置为 True，这个字段必须在整个表中保持值唯一。
```

#### Field.unique_for_date
```
将其设置为DateField或DateTimeField的名称，以要求该字段对于日期字段的值是惟一的。
```

#### Field.unique_for_month
```
和 unique_for_date 类似，只是要求字段在指定字段的月份内唯一。
```

#### Field.unique_for_year
```
和 unique_for_date 及 unique_for_month 类似，只是时间范围变成了一年。
```

#### Field.verbose_name
```
除 ForeignKey 、 ManyToManyField 和 OneToOneField 之外的字段都接受一个详细名称作为第一个位置参数。
```

#### Field.validators
```
设置验证器，validator是可调用的，它接受一个值，如果它不满足某些标准，就会发出ValidationError。验证器可以用于在不同类型的字段之间重用验证逻辑。
```

### field types
#### AutoField
```
一个自动递增的整型字段，添加记录时它会自动增长。你通常不需要直接使用这个字段；如果你不指定主键的话，系统会自动添加一个主键字段到你的model。(参阅自动主键字段)，一般设置id字段为autofiled。
```
#### BigAutoField
```
与AutoField相似，但是能支持1-9223372036854775807。
```
#### BigIntegerField
```
一个64位的整数，很像一个IntegerField，只是它保证能够容纳从-9223372036854775808到9223372036854775807的数字。这个字段的默认表单小部件是一个TextInput。
```
#### BinaryField
```
存储原始二进制数据的字段。它可以被分配字节、bytearray或memoryview。
默认情况下，BinaryField将editable设置为False，在这种情况下，它不能包含在ModelForm中。
```
#### BooleanField
```
布尔字段,管理工具里会自动将其描述为checkbox，但是数据库里会以0和1的方式进行存储，查看数据库表该字段，如mysql中显示为int型。
```
#### CharField
```
字符串字段，单行输入，用于较短的字符串，如要保存大量文本, 使用 TextField，CharField有一个必填参数：CharField.max_length：字符的最大长度，django会根据这个参数在数据库层和校验层限制该字段所允许的最大字符数。

```
#### DateField
```
日期字段，admin 用一个文本框 <input type=”text”> 来表示该字段数据(附带一个 JavaScript 日历和一个”Today”快捷按键。有下列额外的可选参数：
auto_now：当对象被保存时,自动将该字段的值设置为当前时间.通常用于表示 “last-modified” 时间戳；
auto_now_add：当对象首次被创建时,自动将该字段的值设置为当前时间.通常用于表示对象创建时间。
注意，该字段将时间存储为date的格式，因此，精度会到day截止，如“2013-08-06 00:00:00”。
```
#### DateTimeField
```
类似 DateField 支持同样的附加选项， 可以存储准确的时间信息， 如“2013-12-12 16:42:27”。
```
#### EmailField
```
使用EmailValidator检查值是否是有效的电子邮件地址的CharField。
```
#### FileField
```
一个文件上传字段。
```
#### FilePathField
```
一种CharField，它的选择仅限于文件系统上某个目录中的文件名。
```
#### FloatField
```
在Python中由浮点实例表示的浮点数。

该字段的默认表单小部件在localalize为False时为NumberInput，否则为TextInput。
```
#### ImageField
```
从FileField继承所有属性和方法，但也验证上传的对象是一个有效的图像。

除了FileField可用的特殊属性外，ImageField还具有高度和宽度属性。
```
#### IntegerField
```
一个整数。在Django支持的所有数据库中，从-2147483648到2147483647的值是安全的。

它使用MinValueValidator和MaxValueValidator根据默认数据库支持的值验证输入。

该字段的默认表单小部件在localalize为False时为NumberInput，否则为TextIn
```
#### GenericIPAddressField
```
字符串格式的IPv4或IPv6地址(例如:192.0.2.30或2a02:42fe::4)。这个字段的默认表单小部件是一个TextInput。
```

#### PositiveIntegerField
```
从0到2147483647的值在Django支持的所有数据库中都是安全的。由于向后兼容性的原因，可以接受值0。
```
#### TextField
```
一个大的文本字段。这个字段的默认表单小部件是一个Textarea。

如果指定max_length属性，它将反映在自动生成的表单字段的Textarea小部件中。但是，它不会在模型或数据库级别强制执行。用CharField来表示。
```
#### TimeField
```
时间，在Python中由日期时间表示。时间的实例。接受与DateField相同的自动填充选项。

这个字段的默认表单小部件是一个TextInput。管理员添加了一些JavaScript快捷方式。
```
#### URLField
```
URL的CharField，由URLValidator验证。

这个字段的默认表单小部件是一个TextInput。

与所有CharField子类一样，URLField使用可选的max_length参数。如果不指定max_length，则使用默认值200。
```
#### UUIDField
```
用于存储全局唯一标识符的字段。使用Python的UUID类。当在PostgreSQL上使用时，它存储为uuid数据类型，否则存储为char(32)。
```
