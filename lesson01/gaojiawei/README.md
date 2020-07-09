#### USE_L10N = False用途
https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-USE_TZ
默认值：False
A boolean that specifies if localized formatting of data will be enabled by default or not. If this is set to True, e.g. Django will display numbers and dates using the format of the current locale.
```
一个布尔值，指定默认情况下是否启用数据的本地化格式。如果设置为True，例如Django将使用当前语言环境的格式显示数字和日期。
```
The default settings.py file created by django-admin startproject includes USE_L10N = True for convenience.
```
为了方便起见，django-admin startproject创建的缺省settings.py文件包括USE_L10N = True。
```
