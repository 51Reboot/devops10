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
