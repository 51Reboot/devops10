https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-USE_TZ

USE_L10N


`A boolean that specifies if localized formatting of data will be enabled by default or not. If this is set to True, e.g. Django will display numbers and dates using the format of the current locale.`

See also LANGUAGE_CODE, USE_I18N and USE_TZ.\
`The default settings.py file created by django-admin startproject includes USE_L10N = True for convenience.` 

在使用django-admin创建的时候默认值为True,会以当前语言环境为基础显示时间和日期,即如果为中文环境会以年月日显示2020年7月9日

如果为false,会以国际化的格式来展示，2020-07-09