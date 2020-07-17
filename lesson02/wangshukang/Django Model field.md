### 2. Django Model field



> 含义翻译成中文，写成Markdown提交到作业目录中.

### 2.1 字段选项

- ####  NUll

  - #####  Field.null 

  -  如果设置为 `True`， 当该字段为空时，Django 会将数据库中该字段设置为 `NULL`，默认为 `False`。

  避免在基于字符串的字段（例如 [`CharField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField) 和 [`TextField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.TextField)）上使用 [`null`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.null)。如果字符串字段的 `null=True`，那意味着对于“无数据”有两个可能的值：`NULL` 和空字符串。在大多数情况下，对于“无数据”声明两个值是赘余的，Django 的惯例是使用空字符串而不是 `NULL`。 一个例外是当 [`CharField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField) 同时具有 `unique=True` 和 `blank=True` 时。 在这种情况下，需要设置 `null=True`，以便在使用空白值保存多个对象时避免唯一的约束违规。

  - 对于基于字符串的字段和基于非字符串的字段，如果希望允许表单中的空值，则还需要设置blank = True，因为null参数仅影响数据库存储（请参见空白）。 

    ```bash
    注意：使用Oracle数据库后端时，无论此属性如何，都将存储值NULL表示空字符串 
    ```

- ### Blank

  - #####  Field.blank 

  -  如果设置为 `True` ，该字段允许为空。默认为 `False` 。 

    ```bash
    请注意，这不同于null。 null纯粹是与数据库有关的，而blank是与验证有关的。如果字段的blank为True，则表单验证将允许输入一个空值。如果字段的blank为False，则需要该字段。
    ```

- ### choices

  - #####  Field.choices

  - 一个由恰好两个项目（例如）的可迭代项组成 的[序列](https://docs.python.org/3/glossary.html#term-sequence)，用作此字段的选择。如果给出了选择，则[模型验证](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#validating-objects)将强制执行这些选择，并且默认表单小部件将是具有这些选择的选择框，而不是标准文本字段。`[(A, B), (A, B) ...]`
  
    每个元组中的第一个元素是要在模型上设置的实际值，第二个元素是可阅读的名称。例如：
  
    ```python
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    ]
    ```
  
     通常，最好在模型类中定义选择，并为每个值定义一个适当命名的常量： 
  
    ```python
    from django.db import models
    
    class Student(models.Model):
        FRESHMAN = 'FR'
        SOPHOMORE = 'SO'
        JUNIOR = 'JR'
        SENIOR = 'SR'
        YEAR_IN_SCHOOL_CHOICES = [
            (FRESHMAN, 'Freshman'),
            (SOPHOMORE, 'Sophomore'),
            (JUNIOR, 'Junior'),
            (SENIOR, 'Senior'),
        ]
        year_in_school = models.CharField(
            max_length=2,
            choices=YEAR_IN_SCHOOL_CHOICES,
            default=FRESHMAN,
        )
    
        def is_upperclass(self):
            return self.year_in_school in (self.JUNIOR, self.SENIOR)
    ```
  
    尽管您可以在模型类外部定义一个选择列表，然后再引用它，但在模型类内部定义每个选择的选择和名称，会将所有信息保留在使用它的类中，并使选择易于参考（例如，`Student.SOPHOMORE` 将`Student`在导入模型的任何地方工作）。
  
    您还可以将可用选项收集到命名组中，以用于组织目的：
  
    ```python
    MEDIA_CHOICES = [
        ('Audio', (
                ('vinyl', 'Vinyl'),
                ('cd', 'CD'),
            )
        ),
        ('Video', (
                ('vhs', 'VHS Tape'),
                ('dvd', 'DVD'),
            )
        ),
        ('unknown', 'Unknown'),
    ]
    ```
  
    
  
    每个元组中的第一个元素是应用于组的名称。第二个元素是2元组的可迭代对象，每个2元组包含一个值和一个选项的易于理解的名称。可以在单个列表中将分组的选项与未分组的选项组合在一起（例如本示例中的 unknown选项）。
  
    对于已[`choices`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.choices)设置的每个模型字段，Django将添加一个方法来检索该字段的当前值的可读名称。请参见 [`get_FOO_display()`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#django.db.models.Model.get_FOO_display)数据库API文档。
  
    请注意，选择可以是任何序列对象-不一定是列表或元组。这使您可以动态构造选择。但是，如果您发现黑客攻击[`choices`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.choices)是动态的，那么最好使用带有的适当数据库表[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)。[`choices`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.choices)用于静态数据，该静态数据不会发生太大变化。
  
    ```python
    初步choices的顺序变动时将会创造新的迁移。
    ```
  
     除非[`blank=False`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.blank)在字段中与一起设置， 否则[`default`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.default)包含的标签`"---------"`将与选择框一起呈现。要覆盖此行为，添加一个元组`choices` 包含`None`; 例如。或者，您可以使用空字符串代替有意义的位置-例如在上。`(None, 'Your String For Display')``None`[`CharField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField) 
  
    
  
- #### db_column

  +  ##### Field.db_column 

    用于此字段的数据库列的名称。如果未指定，Django将使用该字段的名称。

    如果您的数据库列名称是SQL保留字，或者包含Python变量名称中不允许使用的字符（尤其是连字符），那可以。Django在幕后引用列名和表名。



+ ### db_index

  +  ##### Field.db_index

     如果为`True`，将为此字段创建数据库索引。 



+ ### db_tablespace

  +  ##### Field.db_tablespace

     如果此字段已建立索引，则用于该字段的索引的[数据库表空间](https://docs.djangoproject.com/zh-hans/2.2/topics/db/tablespaces/)的名称。默认值是项目的 [`DEFAULT_INDEX_TABLESPACE`](https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-DEFAULT_INDEX_TABLESPACE)设置（如果已设置）或 [`db_tablespace`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/options/#django.db.models.Options.db_tablespace)模型的设置（如果有）。如果后端不支持索引的表空间，则忽略此选项。 



+ ### default

  +  Field.default

    该变量的值。可以是一个值或者是一个可调用的对象，如果是个可调用对象，每次实例化模型时都会调用该对象。

    默认不能是可变对象（模型实例，`list`，`set`等），作为该对象的相同实例的引用将被用作在所有新的模型实例的默认值。而是将所需的默认值包装在可调用中。例如，如果要指定一个默认`dict`的 [`JSONField`](https://docs.djangoproject.com/zh-hans/2.2/ref/contrib/postgres/fields/#django.contrib.postgres.fields.JSONField)，使用函数：

    ```python
    def contact_default():
        return {"email": "to1@example.com"}
    
    contact_info = JSONField("ContactInfo", default=contact_default)
    ```

    `lambda`不能用于字段选项，`default`因为它们不能通过[迁移序列化](https://docs.djangoproject.com/zh-hans/2.2/topics/migrations/#migration-serializing)。有关其他注意事项，请参阅该文档。

    对于[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)此类映射到模型实例的字段，默认值应为它们引用的字段的值（`pk`除非 [`to_field`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.to_field)已设置），而不是模型实例。

    创建新模型实例且未为该字段提供值时，将使用默认值。如果该字段是主键，则当该字段设置为时，也会使用默认值`None`。



+ ### editable

  +  ##### Field.editable

     如果是`False`，则该字段将不会显示在管理员或其他任何人中 [`ModelForm`](https://docs.djangoproject.com/zh-hans/2.2/topics/forms/modelforms/#django.forms.ModelForm)。在[模型验证](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#validating-objects)期间也将跳过它们。默认值为`True`。 



+ ### error_messages

  +  ##### Field.error_messages

    该`error_messages`参数使您可以覆盖该字段将引发的默认消息。输入具有与您要覆盖的错误消息匹配的键的字典。

    错误消息键包括`null`，`blank`，`invalid`，`invalid_choice`， `unique`，和`unique_for_date`。在下面的“ [字段类型”](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#field-types)部分中为每个字段指定了其他错误消息键。

    这些错误消息通常不会传播到表单。请参见 [有关模型的error_messages的注意事项](https://docs.djangoproject.com/zh-hans/2.2/topics/forms/modelforms/#considerations-regarding-model-errormessages)。



+ ### help_text

  +  ##### Field.help_text

    额外的“帮助”文本，随便表单控件一起显示。甚至你的以外的未使用表单，它对于生成文档也是很有用的。

    请注意，此值*不会*以自动生成的形式转义为HTML。如果需要，可以将HTML包含在内[`help_text`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.help_text)。例如：

    ```python
    help_text="Please use the following format: <em>YYYY-MM-DD</em>."
    ```

     或者，您可以使用纯文本并 [`django.utils.html.escape()`](https://docs.djangoproject.com/zh-hans/2.2/ref/utils/#django.utils.html.escape)转义任何HTML特殊字符。确保避免转义来自不受信任用户的任何帮助文本，以避免跨站点脚本攻击。 



+ ### primary_key

  +  ##### Field.primary_key

    如果设置为`True`，则初始设置为该模型的主键。

    如果您未`primary_key=True`在模型中指定任何字段，则Django会自动添加一个[`AutoField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.AutoField)来保留主键，因此您无需`primary_key=True`在任何字段上进行设置，除非您想覆盖默认的主键行为。有关更多信息，请参见 [自动设置主键](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#automatic-primary-key-fields)。

    `primary_key=True`暗示[`null=False`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.null)和 [`unique=True`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.unique)。一个对象只允许使用一个主键。

    主键字段是只读的。如果更改现有对象上的主键的值然后保存，则将在旧对象的旁边创建一个新对象。

 

+ ### unique

  + #####  Field.unique

    如果设置为`True`，这个部分必须在整个表中保持值唯一。

    这是在数据库级别并通过模型验证强制执行的。如果您尝试在[`unique`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.unique) 字段中保存具有重复值[`django.db.IntegrityError`](https://docs.djangoproject.com/zh-hans/2.2/ref/exceptions/#django.db.IntegrityError)的模型，则模型的[`save()`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#django.db.models.Model.save)方法将引发 a 。

    此选项对[`ManyToManyField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField)和 以外的所有字段类型均有效[`OneToOneField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.OneToOneField)。

    请注意，当`unique`为is时`True`，您无需指定 [`db_index`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.db_index)，因为这`unique`意味着创建了索引。



+ ### unique_for_date

  + #####  Field.unique_for_date

    将此设置为的名称，[`DateField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateField)或[`DateTimeField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateTimeField)要求该字段对于日期字段的值是唯一的。

    举例来说，如果你有一个字段`title`有 `unique_for_date="pub_date"`，那么Django的不允许的两个记录具有相同的入口`title`和`pub_date`。

    请注意，如果将其设置为指向[`DateTimeField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateTimeField)，则仅考虑字段的日期部分。此外，当[`USE_TZ`](https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-USE_TZ)是 `True`时，支票将在执行[当前时区](https://docs.djangoproject.com/zh-hans/2.2/topics/i18n/timezones/#default-current-time-zone)的对象被保存的时间。

    这是[`Model.validate_unique()`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#django.db.models.Model.validate_unique)在模型验证期间强制实施的，而不是在数据库级别实施的。如果任何[`unique_for_date`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.unique_for_date)约束涉及不属于的字段[`ModelForm`](https://docs.djangoproject.com/zh-hans/2.2/topics/forms/modelforms/#django.forms.ModelForm)（例如，如果其中一个字段已列出`exclude`或具有 [`editable=False`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.editable)），[`Model.validate_unique()`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#django.db.models.Model.validate_unique)则将跳过对该特定约束的验证。



+ ### unique_for_month

  + #####  Field.unique_for_month

     类似于[`unique_for_date`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.unique_for_date)，但要求该字段相对于月份是唯一的。 



+ ### unique_for_year

  + #####  Field.unique_for_year

     和 [`unique_for_date`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.unique_for_date) and [`unique_for_month`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.unique_for_month).一样



+ ### verbose_name

  + #####  Field.verbose_name

     该字段的可读名称。如果未提供详细名称，则Django将使用字段的属性名称自动创建，将下划线转换为空格。请参阅[详细字段名称](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#verbose-field-names)。 



+ ### validators

  + #####  Field.validators

     要为此字段运行的验证器列表。有关更多信息，请参见[验证程序文档](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/)。 



### 2.2 字段类型

+ ### AutoField

  + #####  *class*`AutoField`（*** options*） 

     [`IntegerField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.IntegerField)根据可用ID自动递增。您通常不需要直接使用它；如果没有另外指定，主键字段将自动添加到模型中。请参阅[自动设置主键](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#automatic-primary-key-fields) 



+ ### BigAutoField

  + #####  *class*`BigAutoField`（*** options*）

     一个64位整数，非常类似于，[`AutoField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.AutoField)不同之处在于它保证可以匹配从`1`到的数字`9223372036854775807` 

    

+ ### BigIntegerField

  +  *class*`BigIntegerField`（*** options*） 

     一个64位整数，非常类似于，[`IntegerField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.IntegerField)不同之处在于它保证可以匹配从`-9223372036854775808`到的 数字`9223372036854775807`。此字段的默认表单小部件是 [`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)。 

    

+ ### BinaryField

  + ##### class `BinaryField`（*max_length = None*，*** options*） 

    一个用于存储原始二进制数据的字段。它可以分配[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)， [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray)或[`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview)。

    默认情况下，`BinaryField`设置[`editable`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.editable)为`False`，在这种情况下，它不能包含在中[`ModelForm`](https://docs.djangoproject.com/zh-hans/2.2/topics/forms/modelforms/#django.forms.ModelForm)。

    `BinaryField` 有一个额外的可选参数：

    - `BinaryField.``max_length`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.BinaryField.max_length)

      字段的最大长度（以字符为单位）。最大长度在Django的验证中使用强制执行 [`MaxLengthValidator`](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/#django.core.validators.MaxLengthValidator)。

    ```python
    尽管您可能考虑过将文件存储在数据库中，但在99％的情况下，都认为这是错误的设计。此字段不能代替适当的静态文件处理。
    ```

    

+ ### BooleanField

  + #####  *class*`BooleanField`（*** options*） 

    正确/错误字段。

    窗口小部件此字段的默认形式[`CheckboxInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.CheckboxInput)，或者[`NullBooleanSelect`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.NullBooleanSelect)如果[`null=True`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.null)。

    默认值`BooleanField`是`None`当[`Field.default`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.default) 没有定义。

    

+ ### CharField

  + #####  `CharField`（*max_length = None*，*** options*） 

    字符串字段，从小到大的字符串。

    对于大量文本，请使用[`TextField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.TextField)。

    此字段的默认表单小部件是[`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)。

    [`CharField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField) 有一个额外的必需参数：

    - `CharField.``max_length`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField.max_length)

      字段的最大长度（以字符为单位）。max_length在数据库级别和Django的验证中使用强制执行 [`MaxLengthValidator`](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/#django.core.validators.MaxLengthValidator)。

      ```python
      如果编写的应用程序必须可移植到多个数据库后端，则应注意max_length某些后端存在限制 。有关详细信息，请参考数据库后端说明。
      ```

      

+ ### DateField

  + ##### class `DateField`（*auto_now = False*，*auto_now_add = False*，*** options*） 

    日期，在Python中由`datetime.date`实例表示。有一些额外的可选参数：

    - `DateField.``auto_now`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateField.auto_now)

      每次保存对象时自动将字段设置为现在。对于“最后修改的”时间戳有用。请注意，*始终* 使用当前日期。它不仅是您可以覆盖的默认值。该字段仅在调用时自动更新[`Model.save()`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#django.db.models.Model.save)。以其他方式（例如）对其他字段进行更新时，该字段不会更新[`QuerySet.update()`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#django.db.models.query.QuerySet.update)，尽管您可以在更新中为该字段指定自定义值。

    - `DateField.``auto_now_add`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateField.auto_now_add)

      首次创建对象时，将字段自动设置为现在。对于创建时间戳很有用。请注意，*始终*使用当前日期。它不仅是您可以覆盖的默认值。因此，即使您在创建对象时为此字段设置了一个值，也会将其忽略。如果您希望能够修改此字段，请设置以下内容，而不是 `auto_now_add=True`：于[`DateField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateField)：`default=date.today`-从 [`datetime.date.today()`](https://docs.python.org/3/library/datetime.html#datetime.date.today)于[`DateTimeField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateTimeField)：`default=timezone.now`-从 [`django.utils.timezone.now()`](https://docs.djangoproject.com/zh-hans/2.2/ref/utils/#django.utils.timezone.now)

    此字段的默认表单小部件是 [`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)。管理员添加了JavaScript日历和“今天”的快捷方式。包括一个附加的`invalid_date`错误消息键。

    选项`auto_now_add`，`auto_now`和`default`是互斥的。这些选项的任何组合都将导致错误。

    ```python
    当前实现，设置auto_now或auto_now_add以 True会导致该领域拥有editable=False和blank=True 集。
    ```

    ```python
    在auto_now和auto_now_add选项将始终使用的日期默认时区在创建或更新的时刻。如果您需要不同的内容，则可能需要考虑使用您自己的可调用默认值或替代值，save() 而不是使用; auto_now或auto_now_add; 或使用a DateTimeField代替a DateField并决定如何处理显示时从datetime到date的转换。
    ```



+ ### DateTimeField

  + ##### *class DateTimeField`（*auto_now = False*，*auto_now_add = False*，*** options*）

  ​     日期和时间，在Python中由`datetime.datetime`实例表示。接受与相同的额外参数[`DateField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateField)。

  此字段的默认表单窗口小部件为单个 [`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)。管理员使用[`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)带有JavaScript快捷方式的两个单独的 小部件。



+ ### DecimalField

  + *类*`DecimalField`（*max_digits =无*，*decimal_places =无*，***选项*）

  固定精度的十进制数字，在Python中由 [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal)实例表示。它使用验证输入 [`DecimalValidator`](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/#django.core.validators.DecimalValidator)。

  有两个**必需的**参数：

  - `DecimalField.``max_digits`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DecimalField.max_digits)

    数字中允许的最大位数。请注意，此数字必须大于或等于`decimal_places`。

  - `DecimalField.``decimal_places`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DecimalField.decimal_places)

    与数字一起存储的小数位数。

  例如，要存储最大`999`分辨率为小数点后2位的数字，请使用：

  ```python
  models.DecimalField(..., max_digits=5, decimal_places=2)
  ```

   并以十位小数位的分辨率存储最多约十亿的数字： 

  ```python
  models.DecimalField(..., max_digits=19, decimal_places=10)
  ```



+ ### DurationField

  + #####  *class*`DurationField`（*** options*） 

     一个存储时间段的字段-用Python在Python中建模 [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta)。在PostgreSQL上使用时，使用的数据类型为`interval`，在Oracle上使用为INTERVAL DAY(9) TO SECOND(6) ,否则将使用微秒的bigint。



+ ### EmailField

  + #####  *class`EmailField`（*max_length = 254*，*** options*） 	

     使用[`CharField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField)来检查该值是否是有效的电子邮件地址的 [`EmailValidator`](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/#django.core.validators.EmailValidator)。 



+ ### FileField

  + #####  *class*`FileField`（*upload_to = None*，*max_length = 100*，*** options*） 

     文件上传字段。 

    ```python
    primary_key不支持该参数，如果使用该参数将引发错误。
    ```

    有两个可选参数：

    - `FileField.``upload_to`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField.upload_to)

      此属性提供了一种设置上传目录和文件名的方法，并且可以通过两种方式进行设置。在两种情况下，该值都将传递给该 [`Storage.save()`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.Storage.save)方法。如果您指定一个字符串值，则它可能包含[`strftime()`](https://docs.python.org/3/library/time.html#time.strftime) 格式，该格式将被文件上载的日期/时间替换（以使上载的文件不会填满给定的目录）。例如：

      ```python
      class MyModel(models.Model):
          # file will be uploaded to MEDIA_ROOT/uploads
          upload = models.FileField(upload_to='uploads/')
          # or...
          # file will be saved to MEDIA_ROOT/uploads/2015/01/30
          upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
      ```



+ 如果使用默认值 [`FileSystemStorage`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.FileSystemStorage)，则将字符串值添加到[`MEDIA_ROOT`](https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-MEDIA_ROOT)路径中，以形成本地文件系统上将存储上传文件的位置。如果您使用其他存储，请查看该存储的文档以了解其处理方式`upload_to`。

  `upload_to`也可以是可调用的，例如函数。这将被调用以获得上载路径，包括文件名。该可调用对象必须接受两个参数，并返回要传递给存储系统的Unix样式的路径（带有正斜杠）。这两个参数是：

  | **论据**     | **描述**                                                     |
  | ------------ | ------------------------------------------------------------ |
  | **instance** | `FileField`定义的模型实例 。更具体地说，这是附加当前文件的特定实例。                       在大多数情况下，这个对象将不会被保存到数据库中还，所以如果使用默认的`AutoField`，*它可能还没有为它的主键字段的值*。 |
  | **filename** | 最初提供给文件的文件名。确定最终目标路径时，可以考虑也可以不考虑。 |

   例子： 

  ```python
  def user_directory_path(instance, filename):
      # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
      return 'user_{0}/{1}'.format(instance.user.id, filename)
  
  class MyModel(models.Model):
      upload = models.FileField(upload_to=user_directory_path)
  ```

  + ##### FileField.storage

    此字段的默认表单小部件是 [`ClearableFileInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.ClearableFileInput)。

    在模型中使用[`FileField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField)或[`ImageField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ImageField)（请参见下文）需要执行几个步骤：

    1. 在您的设置文件中，您需要定义：设置：MEDIA_ROOT作为Django存储上传文件目录的完整路径。（为了提高性能，这些文件不会存储在数据库中）定义：设置：MEDIA_URL作为该目录的基本公共URL ，确保该目录能够被Web服务器的是用户写入。
    2. 将[`FileField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField)或添加[`ImageField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ImageField)到模型中，定义[`upload_to`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField.upload_to)用于指定[`MEDIA_ROOT`](https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-MEDIA_ROOT)要用于上载文件的子目录的选项 。
    3. 将存储在数据库中的所有文件都是该文件的路径（相对于[`MEDIA_ROOT`](https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-MEDIA_ROOT)）。您很可能想使用[`url`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.fields.files.FieldFile.url)Django提供的便捷属性。例如，如果[`ImageField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ImageField)调用了 your，则`mug_shot`可以使用来获取模板中图像的绝对路径 。`{{ object.mug_shot.url }}`

    例如，假设您[`MEDIA_ROOT`](https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-MEDIA_ROOT)设置为`'/home/media'`，并且 [`upload_to`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField.upload_to)设置为`'photos/%Y/%m/%d'`。所述`'%Y/%m/%d'` 的部分[`upload_to`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField.upload_to)就是[`strftime()`](https://docs.python.org/3/library/time.html#time.strftime)格式化; `'%Y'`是四位数的年份，`'%m'`是两位数的月份，`'%d'`是两位数的日期。如果您在2007年1月15日上传文件，该文件将保存在目录中`/home/media/photos/2007/01/15`。

    如果要检索上载的文件在磁盘上的文件名或文件的大小，可以分别使用[`name`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/file/#django.core.files.File.name)和 [`size`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/file/#django.core.files.File.size)属性。有关可用属性和方法的更多信息，请参见 [`File`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/file/#django.core.files.File)类参考和[管理文件](https://docs.djangoproject.com/zh-hans/2.2/topics/files/) 主题指南。

    ```python
    文件在数据库中作为保存模型的一部分，因此在模型被保存之前，不能依赖磁盘上使用的实际文件名。
    ```

    可以使用[`url`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.fields.files.FieldFile.url)属性获取上载文件的相对URL 。在内部，这将调用[`url()`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.Storage.url)基础[`Storage`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.Storage)类的方法。

    请注意，无论何时处理上传的文件，都应密切注意上传文件的位置以及文件的类型，以避免安全漏洞。*验证所有上载的文件，*以确保文件符合您的想法。例如，如果您盲目地让某人未经验证将文件上传到Web服务器文档根目录中的目录，那么某人可以上传CGI或PHP脚本并通过访问您站点上的URL来执行该脚本。不要这样

    还要注意，即使上传的HTML文件也可以由浏览器执行（尽管不能由服务器执行），它也可能构成等同于XSS或CSRF攻击的安全威胁。

    [`FileField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField)实例在数据库中创建为`varchar` 列，默认最大长度为100个字符。与其他字段一样，您可以使用[`max_length`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField.max_length)参数更改最大长度。

+ #### FileField``和``FieldFile

  + ##### class  **FieldFile** 

    当您[`FileField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField)在模型上访问时，系统会为您提供实例[`FieldFile`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.fields.files.FieldFile)作为代理，用于访问基础文件。

    的API [`FieldFile`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.fields.files.FieldFile)反映了的API [`File`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/file/#django.core.files.File)，但有一个主要区别：*类包装的对象不一定是Python内置文件对象的包装。*相反，它是[`Storage.open()`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.Storage.open) 方法结果的包装，它可以是[`File`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/file/#django.core.files.File)对象，也可以是[`File`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/file/#django.core.files.File)API 的自定义存储的实现。

    除了从[`File`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/file/#django.core.files.File)诸如 `read()`和继承的API之外`write()`，[`FieldFile`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.fields.files.FieldFile)还包括几种可用于与基础文件进行交互的方法：

    ```python
    此类save()和的 两种方法delete()默认将关联的模型对象保存FieldFile在数据库中。
    ```

    +  `FieldFile.``name`

     文件名，包括从[`Storage`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.Storage)关联 根目录到根目录的相对路径 [`FileField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField)。

    - `FieldFile.``size`

      

    基础[`Storage.size()`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.Storage.size)方法的结果。

    - `FieldFile.``url`

      

    一个只读属性，通过调用[`url()`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.Storage.url)基础[`Storage`](https://docs.djangoproject.com/zh-hans/2.2/ref/files/storage/#django.core.files.storage.Storage)类的方法 来访问文件的相对URL 。

    - `FieldFile.``open`（*mode ='rb'*）

      

    在指定的中打开或重新打开与此实例关联的文件 `mode`。与标准的Python `open()`方法不同，它不返回文件描述符。

    由于在访问基础文件时会隐式打开基础文件，因此可能无需调用此方法，除非将指针重置为基础文件或更改`mode`。

    - `FieldFile.``close`（）

    行为类似于标准的Python `file.close()`方法，并关闭与此实例关联的文件。

    - `FieldFile.``save`（*name*，*content*，*save = True*）

      

    此方法采用文件名和文件内容，并将它们传递到该字段的存储类，然后将存储的文件与model字段关联。如果要手动将文件数据与[`FileField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField)模型上的实例关联 ，`save()` 则使用该方法来保留该文件数据。

    接受两个必需的参数：`name`这是文件的名称，和 `content`是包含文件内容的对象。可选`save`参数控制在更改与该字段关联的文件之后是否保存模型实例。默认为 `True`。

    请注意，该`content`参数应该是的实例 django.core.files.File`而不是Python的内置文件对象。您可以File像这样从现有的Python文件对象构造一个：

    ```python
    from django.core.files import File
    # Open an existing file using Python's built-in open()
    f = open('/path/to/hello.world')
    myfile = File(f)
    ```

     或者，您可以像这样从Python字符串构造一个： 

    ```python
    from django.core.files.base import ContentFile
    myfile = ContentFile("hello world")
    ```

    + `FieldFile.``delete`（*save = True*） 

      删除与此实例关联的文件，并清除字段上的所有属性。注意：如果在`delete()`调用时碰巧打开了文件，此方法将关闭文件 。

      可选`save`参数控制在删除与该字段关联的文件之后是否保存模型实例。默认为 `True`。

      请注意，删除模型时，不会删除相关文件。如果需要清理孤立的文件，则需要自己处理（例如，使用可手动运行或计划通过cron定期运行的自定义管理命令）。



+ ### FilePathField

  + ##### class  `FilePathField`（*path = None*，*match = None*，*递归= False*，*max_length = 100*，*** options*） 

    [`CharField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField)的选择仅限于文件系统上某个目录中的文件名。具有三个特殊参数，其中第一个是 **必需的**：

    - `FilePathField.``path`

      需要。目录的绝对文件系统路径，从中可以[`FilePathField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FilePathField)选择该目录 。范例：`"/home/images"`。

    - `FilePathField.``match`

      可选的。作为字符串的正则表达式，[`FilePathField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FilePathField) 将用于过滤文件名。请注意，正则表达式将应用于基本文件名，而不是完整路径。示例：`"foo.*\.txt$"`，它将与名为，`foo23.txt`但不匹配`bar.txt`或的文件匹配`foo23.png`。

    - `FilePathField.``recursive`

      可选的。无论是`True`或`False`。默认值为`False`。指定是否[`path`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FilePathField.path)应包含的所有子目录

    - `FilePathField.``allow_files`

      可选的。无论是`True`或`False`。默认值为`True`。指定是否应包含指定位置的文件。要么是，要么 [`allow_folders`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FilePathField.allow_folders)必须是`True`。

    - `FilePathField.``allow_folders`[¶]

      可选的。无论是`True`或`False`。默认值为`False`。指定是否应包含指定位置的文件夹。要么是，要么[`allow_files`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FilePathField.allow_files)必须是`True`。

    当然，这些参数能够同时使用。

    一个潜在的陷阱是[`match`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FilePathField.match)适用于基本文件名，而不是完整路径。因此，此示例：

             ```python
FilePathField(path="/home/images", match="foo.*", recursive=True)
             ```

...将匹配，`/home/images/foo.png`但不匹配，`/home/images/foo/bar.png` 因为[`match`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FilePathField.match)应用于基本文件名（`foo.png`和`bar.png`）。

[`FilePathField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FilePathField)实例在数据库中创建为`varchar` 列，默认最大长度为100个字符。与其他字段一样，您可以使用[`max_length`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField.max_length)参数更改最大长度。



+ ### FloatField

  + #####  *class*`FloatField`（*** options*） 

    在Python中由`float`实例表示的浮点数。

    此字段的默认表单窗口小部件为[`NumberInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.NumberInput) when [`localize`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/fields/#django.forms.Field.localize)is `False`或 [`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)其他方式。

    ```python
    FloatField 与 DecimalField
    
    该FloatField班有时夹杂了 DecimalField阶级。尽管它们都代表实数，但它们代表的数字却有所不同。FloatField在float 内部使用Python的类型，而在内部DecimalField使用Python的Decimal类型。有关两者之间区别的信息，请参见该decimal模块的Python文档。
    ```



+ ### ImageField

  + ##### class  `ImageField`（*upload_to = None*，*height_field = None*，*width_field = None*，*max_length = 100*，*** options*） 

    从继承所有属性和方法[`FileField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField)，还验证上载的对象是有效的图像。

    除了可用于特殊属性[`FileField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.FileField)，一个[`ImageField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ImageField)也具有`height`和`width`属性。

    为了便于查询这些属性，[`ImageField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ImageField)有两个额外的可选参数：

    - `ImageField.``height_field`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ImageField.height_field)

      每次保存模型实例时，模型字段的名称都会自动填充图像的高度。

    - `ImageField.``width_field`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ImageField.width_field)

      每次保存模型实例时，模型字段的名称都会自动填充图像的宽度。

    需要[枕头](https://pillow.readthedocs.io/en/latest/)库。

    [`ImageField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ImageField)实例在数据库中创建为`varchar` 列，默认最大长度为100个字符。与其他字段一样，您可以使用[`max_length`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField.max_length)参数更改最大长度。

    此字段的默认表单小部件是 [`ClearableFileInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.ClearableFileInput)。



+ ### IntegerField

  + #####  *class*`IntegerField`（*** options*） 

    一个整数。从`-2147483648`到的值`2147483647`在Django支持的所有数据库中都是安全的。

    它使用[`MinValueValidator`](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/#django.core.validators.MinValueValidator)并 [`MaxValueValidator`](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/#django.core.validators.MaxValueValidator)基于默认数据库支持的值来验证输入。

    此字段的默认表单窗口小部件为[`NumberInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.NumberInput) when [`localize`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/fields/#django.forms.Field.localize)is `False`或 [`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)其他方式。



+ ### GenericIPAddressField

  +  *class*`GenericIPAddressField`（*protocol ='both'*，*unpack_ipv4 = False*，*** options*） 

    字符串格式的IPv4或IPv6地址（例如`192.0.2.30`或 `2a02:42fe::4`）。此字段的默认表单小部件是 [`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)。

    IPv6地址规范化如下 [**RFC 4291＃section-2.2**](https://tools.ietf.org/html/rfc4291.html#section-2.2)第[ **2.2**](https://tools.ietf.org/html/rfc4291.html#section-2.2)节，包括使用该节第3段中建议的IPv4格式，例如 `::ffff:192.0.2.0`。例如，`2001:0::0:01`将被标准化为 `2001::1`，并`::ffff:0a0a:0a0a`到`::ffff:10.10.10.10`。所有字符都将转换为小写。

    - `GenericIPAddressField.``protocol`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.GenericIPAddressField.protocol)

      将有效输入限制为指定的协议。可接受的值为`'both'`（默认值）`'IPv4'` 或`'IPv6'`。匹配不区分大小写。

    - `GenericIPAddressField.``unpack_ipv4`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.GenericIPAddressField.unpack_ipv4)

      解压缩IPv4映射的地址，例如`::ffff:192.0.2.1`。如果启用此选项，则该地址将被解压缩到 `192.0.2.1`。默认设置为禁用。只能在`protocol`设为时使用`'both'`。

    如果允许空白值，则必须允许空值，因为空白值存储为空值。



+ ### NullBooleanField

  + #####  *class*`NullBooleanField`（*** options*） 

     就像[`BooleanField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.BooleanField)用`null=True`。使用该字段代替该字段，因为在将来的Django版本中可能会不推荐使用该字段。 



+ ### PositiveIntegerField

  + #####  *class*`PositiveIntegerField`（*** options*） 

     类似于[`IntegerField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.IntegerField)，但必须为正数或零（`0`）。从`0`到的值`2147483647`在Django支持的所有数据库中都是安全的。`0`出于向后兼容的原因，接受该值。 



+ ### PositiveSmallIntegerField

  + #####  *class*`PositiveSmallIntegerField`（*** options*） 

     类似于[`PositiveIntegerField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.PositiveIntegerField)，但仅允许在特定点（与数据库有关）下的值。从`0`到的值`32767`在Django支持的所有数据库中都是安全的。 



+ ### SlugField

  + ##### class `SlugField`（*max_length = 50*，*** options*） 

    [Slug](https://docs.djangoproject.com/zh-hans/2.2/glossary/#term-slug)是一个报纸术语。子弹是某事物的简短标签，仅包含字母，数字，下划线或连字符。它们通常在URL中使用。

    像CharField一样，您可以指定[`max_length`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField.max_length)（也请阅读该[`max_length`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField.max_length)部分中有关数据库可移植性的说明）。如果[`max_length`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField.max_length)未指定，则Django将使用默认长度50。

    表示设置[`Field.db_index`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.db_index)为`True`。

    根据一些其他值自动预填充SlugField通常很有用。您可以使用在管理员中自动执行此操作 [`prepopulated_fields`](https://docs.djangoproject.com/zh-hans/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields)。

    它使用[`validate_slug`](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/#django.core.validators.validate_slug)或 [`validate_unicode_slug`](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/#django.core.validators.validate_unicode_slug)进行验证。

    - `SlugField.``allow_unicode`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.SlugField.allow_unicode)

      如果为`True`，则该字段除了接受ASCII字母外，还接受Unicode字母。默认为`False`。



+ ### SmallIntegerField

  + #####  *class*`SmallIntegerField`（*** options*） 

     类似于[`IntegerField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.IntegerField)，但仅允许在特定点（与数据库有关）下的值。从`-32768`到的值`32767`在Django支持的所有数据库中都是安全的。 



+ ### TextField

  + #####  *class*`TextField`（*** options*） 

    大文本字段。此字段的默认表单小部件是 [`Textarea`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.Textarea)。

    如果指定`max_length`属性，它将反映在[`Textarea`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.Textarea)自动生成的表单字段的 小部件中。但是，它不是在模型或数据库级别强制执行的。使用 [`CharField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField)了点。



+ ### TimeField

  + ##### class  `TimeField`（*auto_now = False*，*auto_now_add = False*，*** options*） 

    时间，在Python中以`datetime.time`实例表示。接受与相同的自动填充选项[`DateField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DateField)。

    此字段的默认表单小部件是[`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)。管理员添加了一些JavaScript快捷方式。



+ ### URLField

  + #####  `URLField`（*max_length = 200*，*** options*） 

    一个[`CharField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField)一个URL，通过验证 [`URLValidator`](https://docs.djangoproject.com/zh-hans/2.2/ref/validators/#django.core.validators.URLValidator)。

    此字段的默认表单小部件是[`TextInput`](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/widgets/#django.forms.TextInput)。

    像所有[`CharField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField)子类一样，[`URLField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.URLField)采用可选 [`max_length`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField.max_length)参数。如果未指定 [`max_length`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CharField.max_length)，则使用默认值200。



+ ### UUIDField

  + *class*`UUIDField`（*** options*）[[源代码\]](https://docs.djangoproject.com/zh-hans/2.2/_modules/django/db/models/fields/#UUIDField)[ ¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.UUIDField)

    

  用于存储通用唯一标识符的字段。使用Python的 [`UUID`](https://docs.python.org/3/library/uuid.html#uuid.UUID)类。在PostgreSQL上使用时，它存储在`uuid`数据类型中，否则存储在 中`char(32)`。

  通用的唯一标识符是[`AutoField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.AutoField)for 的很好替代[`primary_key`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.primary_key)。该数据库不会为您生成UUID，因此建议使用[`default`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.default)：

  ```python
  import uuid
  from django.db import models
  
  class MyUUIDModel(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      # other fields
  ```

   请注意，会将的可调用项（省略了括号）传递给`default`，而不是的实例`UUID`。 

  在PostgreSQL上查找

  使用[`iexact`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#std:fieldlookup-iexact)，[`contains`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#std:fieldlookup-contains)，[`icontains`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#std:fieldlookup-icontains)， [`startswith`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#std:fieldlookup-startswith)，[`istartswith`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#std:fieldlookup-istartswith)，[`endswith`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#std:fieldlookup-endswith)，或 [`iendswith`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#std:fieldlookup-iendswith)在PostgreSQL上查找不为值工作不带连字符，因为PostgreSQL将它们存储在一个连字符的UUID数据类型类型。

​	

+ ### ForeignKey

  + ##### class `ForeignKey`（*to*，*on_delete*，*** options*） 

    多对一的关系。需要两个位置参数：被关联的类和[`on_delete`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete)选项

    如果要创建一个递归关系-一个自身本身有多对一关系的对象-则使用。`models.ForeignKey('self', on_delete=models.CASCADE)`

    如果需要在尚未定义的模型上创建关系，则可以使用模型的名称，而不是模型对象本身：

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

   当模型被子类化为具体模型并且与抽象模型的关系不相关时，可以解决在[抽象模型上](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#abstract-base-classes)以这种方式定义的关系`app_label`： 

  ```python
  from django.db import models
  
  class AbstractCar(models.Model):
      manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
  
      class Meta:
          abstract = True
  ```

  ```python
  from django.db import models
  from products.models import AbstractCar
  
  class Manufacturer(models.Model):
      pass
  
  class Car(AbstractCar):
      pass
  
  # Car.manufacturer will point to `production.Manufacturer` here.
  ```

   要引用在另一个应用程序中定义的模型，可以显式指定带有完整应用程序标签的模型。例如，如果上述`Manufacturer` 模型是在另一个名为的应用程序中定义的，则`production`需要使用： 

  ```python
  class Car(models.Model):
      manufacturer = models.ForeignKey(
          'production.Manufacturer',
          on_delete=models.CASCADE,
      )
  ```

  在解决两个应用程序之间的循环导入依赖关系时，这种称为惰性关系的引用可能会很有用。

  在上自动创建数据库索引`ForeignKey`。您可以通过设置[`db_index`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.db_index)为禁用此功能`False`。如果您要创建外键以保持一致性而不是联接，或者要创建替代索引（例如部分或多列索引），则可能要避免索引的开销。

  + ##### 数据库表现

     在后台，Django追加`"_id"`到字段名称以创建其数据库列名称。在上面的示例中，`Car` 模型的数据库表将具有一`manufacturer_id`列。（您可以通过指定明确地更改此内容。[`db_column`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.db_column)）但是，除非编写自定义SQL，否则您的代码永远不必处理数据库列名。您将始终处理模型对象的字段名称。 

  + #### 参数

    [`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey) 接受其他参数，这些参数定义关系的详细信息。

    - `ForeignKey.``on_delete`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete)

      当[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)删除由a引用的对象时，Django将模拟[`on_delete`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete)参数指定的SQL约束的行为 。例如，如果您有一个可为空的字段， [`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)并且希望在删除引用的对象时将其设置为空：

      ```python
      user = models.ForeignKey(
          User,
          models.SET_NULL,
          blank=True,
          null=True,
      )
      ```

      

      的可能值[`on_delete`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete)位于 [`django.db.models`](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#module-django.db.models)：

      - `CASCADE`[[源代码\]](https://docs.djangoproject.com/zh-hans/2.2/_modules/django/db/models/deletion/#CASCADE)[ ¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.CASCADE)

        级联删除。Django模拟ON DELETE CASCADE上SQL约束的行为，并删除包含ForeignKey的对象。[`Model.delete()`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/instances/#django.db.models.Model.delete)不会在相关模型上调用，但 会为所有已删除对象发送[`pre_delete`](https://docs.djangoproject.com/zh-hans/2.2/ref/signals/#django.db.models.signals.pre_delete)和 [`post_delete`](https://docs.djangoproject.com/zh-hans/2.2/ref/signals/#django.db.models.signals.post_delete)信号。

      - `PROTECT`[[源代码\]](https://docs.djangoproject.com/zh-hans/2.2/_modules/django/db/models/deletion/#PROTECT)[ ¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.PROTECT)

        通过引发[`ProtectedError`](https://docs.djangoproject.com/zh-hans/2.2/ref/exceptions/#django.db.models.ProtectedError)的子类来 防止删除引用的对象 [`django.db.IntegrityError`](https://docs.djangoproject.com/zh-hans/2.2/ref/exceptions/#django.db.IntegrityError)。

      - `SET_NULL`[[源代码\]](https://docs.djangoproject.com/zh-hans/2.2/_modules/django/db/models/deletion/#SET_NULL)[ ¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.SET_NULL)

        设置为[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)null；仅当[`null`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.null)是时才有可能 `True`。

      - `SET_DEFAULT`[[源代码\]](https://docs.djangoproject.com/zh-hans/2.2/_modules/django/db/models/deletion/#SET_DEFAULT)[ ¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.SET_DEFAULT)

        将[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)其设置为默认值；[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)必须设置默认值 。

      - `SET`（）[[源代码\]](https://docs.djangoproject.com/zh-hans/2.2/_modules/django/db/models/deletion/#SET)[ ¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.SET)

        将设置为[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)传递给的值 [`SET()`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.SET)，或者如果传递了callable，则调用它的结果。在大多数情况下，有必要传递一个callable，以避免在导入models.py时执行查询：

        ```python
        from django.contrib.auth import get_user_model
        from django.db import models
        
        def get_sentinel_user():
            return get_user_model().objects.get_or_create(username='deleted')[0]
        
        class MyModel(models.Model):
            user = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.SET(get_sentinel_user),
            )
        ```

      - `DO_NOTHING`[[源代码\]](https://docs.djangoproject.com/zh-hans/2.2/_modules/django/db/models/deletion/#DO_NOTHING)[ ¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.DO_NOTHING)

        不采取行动。如果您的数据库后端强制执行参照完整性，则[`IntegrityError`](https://docs.djangoproject.com/zh-hans/2.2/ref/exceptions/#django.db.IntegrityError)除非您手动将SQL 约束添加到数据库字段，否则这将导致。`ON DELETE`

    +  `ForeignKey.``limit_choices_to` 

      使用a `ModelForm`或admin 呈现此字段时，为该字段的可用选项设置限制（默认情况下，可以选择queryset中的所有对象）。可以使用字典， [`Q`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#django.db.models.Q)对象或返回字典或[`Q`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#django.db.models.Q)对象的可调用对象。

      例子：

      ```python
          User,
          on_delete=models.CASCADE,
          limit_choices_to={'is_staff': True},
      )
      ```

      导致上的相应字段`ModelForm`仅列出`Users` 具有的字段`is_staff=True`。这在Django管理员中可能会有所帮助。

      例如，当与Python `datetime`模块结合使用以限制日期范围内的选择时，可调用形式可能会有所帮助。例如：

      ```python
      def limit_pub_date_choices():
          return {'pub_date__lte': datetime.date.utcnow()}
      
      limit_choices_to = limit_pub_date_choices
      ```

       如果`limit_choices_to`是或返回，这是很有用[复杂的查询](https://docs.djangoproject.com/zh-hans/2.2/topics/db/queries/#complex-lookups-with-q)，那么将只有当字段中没有列出对管理员可用的选项的效果 在 为模型。[`Q object`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/querysets/#django.db.models.Q)[`raw_id_fields`](https://docs.djangoproject.com/zh-hans/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.raw_id_fields)`ModelAdmin` 

      ```python
      如果将callable用于limit_choices_to，则每次实例化新表单时都会调用它。当验证模型时也可以调用它，例如通过管理命令或管理员。管理员构造查询集以多次验证其在各种极端情况下的表单输入，因此您的可调用对象有可能被多次调用。
      ```

    + `ForeignKey.``related_name`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_name)

      用于从相关对象到此对象的关系的名称。它也是[`related_query_name`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name)（用于目标模型的反向过滤器名称的名称）的默认值。有关完整的解释和示例，请参见[相关的对象文档](https://docs.djangoproject.com/zh-hans/2.2/topics/db/queries/#backwards-related-objects)。请注意，在[抽象模型](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#abstract-base-classes)上定义关系时必须设置此值 ；并且当您这样做时，可以使用 [一些特殊的语法](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#abstract-related-name)。

      如果您希望Django不要创建反向关系，请将设置 `related_name`为`'+'`或以结束`'+'`。例如，这将确保该`User`模型不会与此模型具有向后关系：

      ```python
      user = models.ForeignKey(
          User,
          on_delete=models.CASCADE,
          related_name='+',
      )
      ```

    + `ForeignKey.``related_query_name`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name)

      用于目标模型的反向过滤器名称的名称。默认为[`related_name`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_name)或 的值[`default_related_name`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/options/#django.db.models.Options.default_related_name)，否则默认为模型的名称：

      ```python
      # Declare the ForeignKey with related_query_name
      class Tag(models.Model):
          article = models.ForeignKey(
              Article,
              on_delete=models.CASCADE,
              related_name="tags",
              related_query_name="tag",
          )
          name = models.CharField(max_length=255)
      
      # That's now the name of the reverse filter
      Article.objects.filter(tag__name="important")
      ```

      像 [`related_name`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_name)，`related_query_name`通过[一些特殊的语法](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#abstract-related-name)支持应用程序标签和类插值。 

    + `ForeignKey.``to_field`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.to_field)

      关系所关联的相关对象上的字段。默认情况下，Django使用相关对象的主键。如果您引用其他字段，则该字段必须具有`unique=True`。

    + `ForeignKey.``db_constraint`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.db_constraint)

      值是“ True”，而且这几乎确定就是你需要的功能。将这个伪会损坏的数据的替代。甚至如此，一下场景一可能需要这样做你有无效的冗余数据你正在共享你的数据库如果将其设置为`False`，则访问不存在的相关对象将引发其`DoesNotExist`异常。

    + `ForeignKey.``swappable`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.swappable)

      如果它[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey) 指向可交换模型，则控制迁移框架的反应。如果它是`True`默认值，[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)则指向与当前值`settings.AUTH_USER_MODEL`（或另一个可交换模型设置）匹配的模型，该关系将使用对设置的引用（而不是直接指向模型）存储在迁移中。仅`False`当您确定模型始终指向交换的模型时（例如，如果它是专门为自定义用户模型设计的配置文件模型），才需要覆盖此设置。将其设置为`False`并不意味着即使已交换掉它也可以引用可交换模型- `False`只是意味着使用此ForeignKey进行的迁移将始终引用您指定的确切模型（因此，如果用户尝试使用可移植模型运行它将很难失败。例如，您不支持的用户模型）。如果不确定，就保留它在默认为“ True”的状态。

### `ManyToManyField`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#manytomanyfield)

- *class*`ManyToManyField`（*to*，*** options*）[[源代码\]](https://docs.djangoproject.com/zh-hans/2.2/_modules/django/db/models/fields/related/#ManyToManyField)[ ¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField)

  

多对多关系。需要一个位置参数：与模型相关的类，其工作原理与之完全相同 [`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)，包括[递归](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#recursive-relationships)和 [惰性](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#lazy-relationships)关系。

通过这个字段的类别：〜django.db.models.fields.related.RelatedManager，关联的对象可以被添加，删除，或者创建。



#### 数据库表现[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#id1)

在幕后，Django创建了一个中间联接表来表示多对多关系。默认情况下，该表名是使用“多对多”字段的名称和包含该表的模型的表名生成的。由于某些数据库不支持超过一定长度的表名，因此这些表名将被自动截断并使用唯一性哈希，例如`author_books_9cdf`。您可以使用该[`db_table`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.db_table)选项手动提供联接表的名称。



#### 参数[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#manytomany-arguments)

[`ManyToManyField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField) 接受一组额外的参数-全部可选-控制关系如何运行。

- `ManyToManyField.``related_name`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.related_name)

  与相同[`ForeignKey.related_name`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_name)。

- `ManyToManyField.``related_query_name`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.related_query_name)

  与相同[`ForeignKey.related_query_name`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name)。

- `ManyToManyField.``limit_choices_to`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.limit_choices_to)

  与相同[`ForeignKey.limit_choices_to`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.limit_choices_to)。`limit_choices_to`在`ManyToManyField`与使用[`through`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.through)参数指定的自定义中间表一起使用 时不起作用。

- `ManyToManyField.``symmetrical`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.symmetrical)

  仅在定义自身为多对多细分关系时。考虑以下这个模型：

  ```python
  from django.db import models
  
  class Person(models.Model):
      friends = models.ManyToManyField("self")
  ```

  当django处理这个模型时，它会做如此定义，它对本身有一个：class：[`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#id1) ManyToManyField`的关系，并且作为结果，它没有添加一个“ person_set”属性到person这个类中。对多分裂关系被认为是对称的-即，如果我是你的朋友，那么你也是我的朋友。

  如果您不希望与保持多对多关系的对称性`self`，请将设置 [`symmetrical`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.symmetrical)为`False`。这将迫使Django为反向关系添加描述符，从而允许 [`ManyToManyField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField)关系非对称。

- `ManyToManyField.``through`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.through)

  Django会自动生成一个表来管理多对多关系。但是，如果要手动指定中间表，则可以使用该[`through`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.through)选项来指定表示要使用的中间表的Django模型。此选项最常见的用法是当您要将[多余的数据与多对多](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#intermediary-manytomany)关联相关联时 。如果未指定显式`through`模型，则仍然`through`可以使用隐式模型类直接访问为保存关联而创建的表。它具有三个用于链接模型的字段。如果源和目标模型不同，下面的细分会生成：`id`：关系的主键。`_id`：`id`声明的模型的 `ManyToManyField`。`_id`：指向`id`的模型的 `ManyToManyField`。如果``ManyToManyField''指向的来源和目标是相同的模型，下面的细分会生成：`id`：关系的主键。`from__id`：`id`指向模型的实例（即源实例）的。`to__id`：`id`关系所指向的实例的实例（即目标模型实例）。这个类可以用来查询联接称为模型实例的记录，使用方式和普通模型类似。

- `ManyToManyField.``through_fields`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.through_fields)

  django将会正常地的决定使用中间模型的那些分段来自动地建立一个多对多的关系。然而，考虑下面的模型。

  ```python
  from django.db import models
  
  class Person(models.Model):
      name = models.CharField(max_length=50)
  
  class Group(models.Model):
      name = models.CharField(max_length=128)
      members = models.ManyToManyField(
          Person,
          through='Membership',
          through_fields=('group', 'person'),
      )
  
  class Membership(models.Model):
      group = models.ForeignKey(Group, on_delete=models.CASCADE)
      person = models.ForeignKey(Person, on_delete=models.CASCADE)
      inviter = models.ForeignKey(
          Person,
          on_delete=models.CASCADE,
          related_name="membership_invites",
      )
      invite_reason = models.CharField(max_length=64)
  ```

  

- `ManyToManyField.``db_table`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.db_table)

  为存储多对多数据而创建的表的名称。如果未提供，则Django将基于以下名称采用默认名称：定义关系的模型表和字段本身的名称。

- `ManyToManyField.``db_constraint`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.db_constraint)

  值是True，而且这几乎确定就是你需要的功能。将这个错误会议损坏的数据的替代。甚至如此，一下场景一可能需要这项：你有无效的冗余数据你正在共享你的数据库同时传递“ db_constraint”和“ through”会引发错误。

- `ManyToManyField.``swappable`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField.swappable)

  如果它[`ManyToManyField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField) 指向可交换模型，则控制迁移框架的反应。如果它是`True`默认值，[`ManyToManyField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField)则指向与当前值`settings.AUTH_USER_MODEL`（或另一个可交换模型设置）匹配的模型，该关系将使用对设置的引用（而不是直接指向模型）存储在迁移中。仅`False`当您确定模型始终指向交换的模型时（例如，如果它是专门为自定义用户模型设计的配置文件模型），才需要覆盖此设置。如果不确定，就保留它在默认为“ True”的状态。

  [`ManyToManyField`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ManyToManyField)不支持[`validators`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.validators)。

  [`null`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.null) 没有作用，因为没有办法在数据库级别上要求关联。



+ ### `OneToOneField`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#onetoonefield)

  - *class`OneToOneField`（*to*，*on_delete*，*parent_link = False*，*** options*）[[源代码\]](https://docs.djangoproject.com/zh-hans/2.2/_modules/django/db/models/fields/related/#OneToOneField)[ ¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.OneToOneField)

    

  一对一的关系。从概念上讲，这与[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)with 相似 [`unique=True`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.Field.unique)，但是关系的“反向”侧将直接返回单个对象。

  这对于作为以某种方式“扩展”另一个模型的模型的主键最有用；例如，[多表继承](https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#multi-table-inheritance)是通过从子模型到父模型添加隐式一对一关系来实现的。

  需要一个位置参数：与模型相关的类。它的工作原理与之完全相同[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)，包括有关[递归](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#recursive-relationships) 和[惰性](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#lazy-relationships)关系的所有选项。

  如果您未指定的[`related_name`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey.related_name)参数，则 `OneToOneField`Django将使用当前模型的小写名称作为默认值。

  通过以下示例：

  ```python
  from django.conf import settings
  from django.db import models
  
  class MySpecialUser(models.Model):
      user = models.OneToOneField(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE,
      )
      supervisor = models.OneToOneField(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE,
          related_name='supervisor_of',
      )
  ```

   您得到的`User`模型将具有以下属性： 

  ```python
  >>> user = User.objects.get(pk=1)
  >>> hasattr(user, 'myspecialuser')
  True
  >>> hasattr(user, 'supervisor_of')
  True
  ```

   一个`DoesNotExist`访问反向关系时，如果在相关表中的条目不存在异常。例如，如果用户没有由指定的主管`MySpecialUser`： 

  ```python
  >>> user.supervisor_of
  Traceback (most recent call last):
      ...
  DoesNotExist: User matching query does not exist.
  ```

  此外，`OneToOneField`接受接受的所有其他参数[`ForeignKey`](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.ForeignKey)，再加上一个参数：

  - `OneToOneField.``parent_link`[¶](https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#django.db.models.OneToOneField.parent_link)

    当`True`在从另一个[具体模型](https://docs.djangoproject.com/zh-hans/2.2/glossary/#term-concrete-model)继承的 [模型中使用时](https://docs.djangoproject.com/zh-hans/2.2/glossary/#term-concrete-model)，指示该字段应该用作返回父类的链接，而不是`OneToOneField`通常由子类隐式创建的多余 部分。

  有关的用法示例，请参见[一对一关系](https://docs.djangoproject.com/zh-hans/2.2/topics/db/examples/one_to_one/)`OneToOneField`。