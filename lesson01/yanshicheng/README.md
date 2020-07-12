# 作业

## USE_L10N

本地格式化配置, Django 内置的格式化时间, 开启之后由Django进行配置日期格式决本地的语言环境.

关闭选项之后默认是英文时间日期格式.可以自定义字段使用的失去格式.

例如:

```python
DATETIME_FORMAT = 'Y-m-d H:i:s'		# DateTimeField
```

## Model.DateTimeField

* DateTimeField

  日期时间字段，格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]，相当于Python中的datetime.datetime()实例。

* DateFuekd

  日期字段，日期格式  YYYY-MM-DD，相当于Python中的datetime.date()实例。



