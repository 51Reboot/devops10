### 1. 分析as_view类方法

1. Django CBV as_view方法

   ```python
   请求处理由view启用dispatch分发给具体的方法后返回结果
   1. 先对initkwargs中的key进行判断
     1) 是否是支持的http method
     2) 类中是否有对应的http method的处理函数 
   2. 定义view函数
     1) view函数中生成View对象
     2) 如果没有head方法，设置head方法等于get方法
     3) request和args,kwargs参数设置为View对象的属性
     4) 通过dispatch分发请求，并返回结果
   3. 设置view函数的属性
     1) 设置view_cls和initkwargs
     2) 将view函数的'__module__', '__name__', '__qualname__', '__doc__', '__annotations__'为cls相对应的属性
     3) 将view函数的'__dict__'设置为cls.dispatch的'__dict__' 
     
   ```

   ```python
   
     @classonlymethod
       def as_view(cls, **initkwargs):
           """Main entry point for a request-response process."""
           for key in initkwargs:
               if key in cls.http_method_names:
                   raise TypeError("You tried to pass in the %s method name as a "
                                   "keyword argument to %s(). Don't do that."
                                   % (key, cls.__name__))
               if not hasattr(cls, key):
                   raise TypeError("%s() received an invalid keyword %r. as_view "
                                   "only accepts arguments that are already "
                                   "attributes of the class." % (cls.__name__, key))
   
           def view(request, *args, **kwargs):
               self = cls(**initkwargs)
               if hasattr(self, 'get') and not hasattr(self, 'head'):
                   self.head = self.get
               self.setup(request, *args, **kwargs)
               if not hasattr(self, 'request'):
                   raise AttributeError(
                       "%s instance has no 'request' attribute. Did you override "
                       "setup() and forget to call super()?" % cls.__name__
                   )
               return self.dispatch(request, *args, **kwargs)
           view.view_class = cls
           view.view_initkwargs = initkwargs
   
           # take name and docstring from class
           update_wrapper(view, cls, updated=())
   
           # and possible attributes set by decorators
           # like csrf_exempt from dispatch
           update_wrapper(view, cls.dispatch, assigned=())
           return view
         
         
       def setup(self, request, *args, **kwargs):
           """Initialize attributes shared by all view methods."""
           self.request = request
           self.args = args
           self.kwargs = kwargs
   
       def dispatch(self, request, *args, **kwargs):
           # Try to dispatch to the right method; if a method doesn't exist,
           # defer to the error handler. Also defer to the error handler if the
           # request method isn't on the approved list.
           if request.method.lower() in self.http_method_names:
               handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
           else:
               handler = self.http_method_not_allowed
           return handler(request, *args, **kwargs)
         
   WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                          '__annotations__')
   WRAPPER_UPDATES = ('__dict__',)
   def update_wrapper(wrapper,
                      wrapped,
                      assigned = WRAPPER_ASSIGNMENTS,
                      updated = WRAPPER_UPDATES):
       """Update a wrapper function to look like the wrapped function
   
          wrapper is the function to be updated
          wrapped is the original function
          assigned is a tuple naming the attributes assigned directly
          from the wrapped function to the wrapper function (defaults to
          functools.WRAPPER_ASSIGNMENTS)
          updated is a tuple naming the attributes of the wrapper that
          are updated with the corresponding attribute from the wrapped
          function (defaults to functools.WRAPPER_UPDATES)
       """
       for attr in assigned:
           try:
               value = getattr(wrapped, attr)
           except AttributeError:
               pass
           else:
               setattr(wrapper, attr, value)
       for attr in updated:
           getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
       # Issue #17482: set __wrapped__ last so we don't inadvertently copy it
       # from the wrapped function when updating __dict__
       wrapper.__wrapped__ = wrapped
       # Return the wrapper so this can be used as a decorator via partial()
       return wrapper
     
   
   ```

   

2. Drf  as_view 方法

   Drf as_view调用Django的as_view，然后在这个基础,免除了csrf保护

   ```python
   
   @classmethod
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

   

### 2. 反射的用法

#### getattr

获取对象的属性的值, 用法为`getattr(obj, fieldname, default)`,如果没有指定默认值。当属性不存在时，会抛出`AttributeError`

```python
class A:
  a = 1
  
  def __init__(self):
    self.b = 1
    self.c = 2
    
  def __str__(self):
    print(self.b, self.c)
    
    
In [5]: getattr(A, 'a')
Out[5]: 1

In [6]: a = A()

In [7]: getattr(a, 'a')
Out[7]: 1

In [8]: getattr(a, 'b')
Out[8]: 1

In [9]: getattr(a, 'c')
Out[9]: 2

In [10]: getattr(a, 'd')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-10-493d917bb6b0> in <module>
----> 1 getattr(a, 'd')

AttributeError: 'A' object has no attribute 'd'

In [11]: getattr(a, 'd', 'default')
Out[11]: 'default'

# 调用__str__函数
In [51]: getattr(a, '__str__')()
1 2
```

#### hasattr

用法为`hasattr(obj, fieldname)`如果`field`不存在返回`False`, 否则返回`True`

```python
if hasattr(self, 'get') and not hasattr(self, 'head'):
    self.head = self.get
```

#### setattr

给对象**动态**的设置一个属性, 用法`setattr(obj, key, value)`

```python
class A:
  pass

In [25]: a = A()

In [26]: setattr(a, 'status', 'ok')

In [27]: a.status
Out[27]: 'ok'
  
In [41]: def print_status(self):
    ...:     print(self.status)
    ...:

In [42]:
# 设置方法
In [42]: bound_method = print_status.__get__(a, a.__class__)

In [43]: setattr(a, 'get_status', bound_method)

In [44]: a.get_status()
ok

```



