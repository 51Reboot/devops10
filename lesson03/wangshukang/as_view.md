## django中as_view

+ as_view 装饰器

  as_view中有一个view闭包

```python
 def as_view(cls, **initkwargs):
        """Main entry point for a request-response process."""
        for key in initkwargs: #从initkwargs中循环遍历关键字
            if key in cls.http_method_names: #判断关键字是否在预置的请求中，在抛出异常，否则执行view()函数
                raise TypeError("You tried to pass in the %s method name as a "
                                "keyword argument to %s(). Don't do that."
                                % (key, cls.__name__))
            if not hasattr(cls, key): #函数中如果没有对应的请求方法，则抛出异常，否则执行view()函数 
                raise TypeError("%s() received an invalid keyword %r. as_view "
                                "only accepts arguments that are already "
                                "attributes of the class." % (cls.__name__, key))

        def view(request, *args, **kwargs):
            self = cls(**initkwargs) #实例化对象
            if hasattr(self, 'get') and not hasattr(self, 'head'): #函数中若是定义了get方法，没有定义head方法，就head方法就是get方法
                self.head = self.get
            self.setup(request, *args, **kwargs) #初始化函数
            if not hasattr(self, 'request'): #函数中若是没有request方法，抛出异常
                raise AttributeError(
                    "%s instance has no 'request' attribute. Did you override "
                    "setup() and forget to call super()?" % cls.__name__
                )
            return self.dispatch(request, *args, **kwargs) #执行dispatch方法
        view.view_class = cls
        view.view_initkwargs = initkwargs

        # take name and docstring from class
        update_wrapper(view, cls, updated=())

        # and possible attributes set by decorators
        # like csrf_exempt from dispatch
        update_wrapper(view, cls.dispatch, assigned=())
        return view
```

dispatch():

```python
def dispatch(self, request, *args, **kwargs):
    # Try to dispatch to the right method; if a method doesn't exist,
    # defer to the error handler. Also defer to the error handler if the
    # request method isn't on the approved list.
    if request.method.lower() in self.http_method_names: #如果request.method方法在http_method_names中，
        handler = getattr(self, request.method.lower(), self.http_method_not_allowed) # request.method方法存在则将引用传给handler，不存在给执行http_method_not_allowed
    else:
        handler = self.http_method_not_allowed
    return handler(request, *args, **kwargs)#返回对应的方法(get()/post(),put()...)
```





## drf as_view()

```python
def as_view(cls, **initkwargs):
    """
    Store the original class on the view function.

    This allows us to discover information about the view when we do URL
    reverse lookups.  Used for breadcrumb generation.
    """
    if isinstance(getattr(cls, 'queryset', None), models.query.QuerySet):
        def force_evaluation():
            raise RuntimeError(
                'Do not evaluate the `.queryset` attribute directly, '
                'as the result will be cached and reused between requests. '
                'Use `.all()` or call `.get_queryset()` instead.'
            )
        cls.queryset._fetch_all = force_evaluation

    view = super().as_view(**initkwargs)
    view.cls = cls
    view.initkwargs = initkwargs

    # Note: session based authentication is explicitly CSRF validated,
    # all other authentication is CSRF exempt.
    return csrf_exempt(view)
```

