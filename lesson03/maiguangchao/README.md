### 1. django-View的as_view()

```python
@classonlymethod
def as_view(cls, **initkwargs):
    """Main entry point for a request-response process.""""
    for key in initkwargs:  # 循环initkwargs里面的关键字参数
        if key in cls.http_method_names:  # 判断参数里面的请求方法是否在http_method_names定义里面的
            # 如果请求方法在http_method_names里，抛出一个TypeError异常，若不在则执行下面定义的view方法
            raise TypeError("You tried to pass in the %s method name as a "
                                "keyword argument to %s(). Don't do that."
                                % (key, cls.__name__))
            # 如果函数里面不存在对应的请求方法，则抛出TypeError异常
            if not hasattr(cls, key):
                raise TypeError("%s() received an invalid keyword %r. as_view "
                                "only accepts arguments that are already "
                                "attributes of the class." % (cls.__name__, key))
                
		# as_view里面定义了view方法：
        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            # 若定义了get方法，没有定义head方法，head方法默认为get方法
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            # 若get与head方法都有定义，则执行setup初始化
            self.setup(request, *args, **kwargs)
            if not hasattr(self, 'request'):  # 若不存在request 则抛出AttributeError错误，若request存在执行dispatch方法，判断请求方法是否正确。
                raise AttributeError(
                    "%s instance has no 'request' attribute. Did you override "
                    "setup() and forget to call super()?" % cls.__name__
                )
            return self.dispatch(request, *args, **kwargs)
        # 定义view类方法的变量
        view.view_class = cls
        view.view_initkwargs = initkwargs

        # take name and docstring from class
        update_wrapper(view, cls, updated=())  # view函数通过更新包装器函数，得到一个新函数

        # and possible attributes set by decorators
        # like csrf_exempt from dispatch
        update_wrapper(view, cls.dispatch, assigned=()) # csrf_exempty也是一样
        return view  # 最终经过处理返回view
           
```

### 2. rest-framwork的as_view()

```python
 @classmethod
    def as_view(cls, **initkwargs):
        """
        Store the original class on the view function.

        This allows us to discover information about the view when we do URL
        reverse lookups.  Used for breadcrumb generation.
        """
        # 判断queryset方法是否存在存，存在则抛错误RuntimeError
        if isinstance(getattr(cls, 'queryset', None), models.query.QuerySet):
            def force_evaluation():
                raise RuntimeError(
                    'Do not evaluate the `.queryset` attribute directly, '
                    'as the result will be cached and reused between requests. '
                    'Use `.all()` or call `.get_queryset()` instead.'
                )
            cls.queryset._fetch_all = force_evaluation
		
        # 调用父类View的as_view方法，实例化得到view
        view = super().as_view(**initkwargs)
        view.cls = cls	# 赋值cls
        view.initkwargs = initkwargs # 赋值关键字参数

        # Note: session based authentication is explicitly CSRF validated,
        # all other authentication is CSRF exempt.
        return csrf_exempt(view)  # 免除csrf保护
```

### 3. Python的hasattr() getattr() setattr() 函数使用方法详解

- hasattr(obj, name) 

  判断对象中是否有name属性或者方法,返回Bool值,存在返回True,否则返回False

  ```python
  In [1]: class A: 
     ...:     def name(): 
     ...:         print(1111) 
     ...:                                                                                     

  In [2]: hasattr(A, 'name')                                                                  
  Out[2]: True

  In [3]: hasattr(A, 'namexx')                    
  Out[3]: False
  ```

- getattr(obj, name[,default])

   获取对象obj的属性或方法,如果存在打印出来,如果不存在,打印出默认值,默认值可选.

  注意: 

  1、如果是返回对象的方法，返回的是内存地址，需要执行这个方法需要加上()

  ```python
  In [33]: class A(): 
      ...:     name = 'Alon' 
      ...:     def run(self): 
      ...:         return "Helloworld" 
      ...:          
      ...:                                                                                    

  In [34]: a = A()                                                                            

  In [35]: getattr(a, "name")                                                                 
  Out[35]: 'Alon'

  In [36]: getattr(a, "run")                                                                  
  Out[36]: <bound method A.run of <__main__.A object at 0x7ffd44c1eac8>>

  In [37]: getattr(a, "run")()                                                                
  Out[37]: 'Helloworld'

  In [38]: getattr(a, "runner")                                                               
  ---------------------------------------------------------------------------
  AttributeError                            Traceback (most recent call last)
  <ipython-input-38-8c4622785b26> in <module>
  ----> 1 getattr(a, "runner")

  AttributeError: 'A' object has no attribute 'runner'

  In [39]: getattr(a, "runner", "18")                                                         
  Out[39]: '18'
  ```

- setattr() 

  setattr(obj, name, values)
  给对象的属性赋值，若属性不存在，先创建再赋值。

  ```python
  In [33]: class A(): 
      ...:     name = 'Alon' 
      ...:     def run(self): 
      ...:         return "Helloworld" 
      ...:          
      ...:   
   
  In [34]: a = A()
      
  In [39]: getattr(a, "runner", "18")                                                         
  Out[39]: '18'

  In [40]: hasattr(a, "runner")                                                               
  Out[40]: False

  In [41]: setattr(a, "runner", "liuxiang")                                                   

  In [42]: hasattr(a, "runner")                                                               
  Out[42]: True
  ```

  ### 综合用法

  判断一个对象的属性是否存在，若不存在就添加该属性。

  ```python
  In [46]: class A(): 
      ...:     name = 'Alon' 
      ...:     def run(self): 
      ...:         return "Helloworld" 
      ...:          
      ...:                                                                                    

  In [47]: a = A()                                                                            

  In [48]: getattr(a, "age")                                                                  
  ---------------------------------------------------------------------------
  AttributeError                            Traceback (most recent call last)
  <ipython-input-48-228343c23051> in <module>
  ----> 1 getattr(a, "age")

  AttributeError: 'A' object has no attribute 'age'

  In [50]: getattr(a, "age", setattr(a, "age", "18"))                                         
  Out[50]: '18'

  In [51]: getattr(a, "age")                                                                  
  Out[51]: '18'
  ```

  ​