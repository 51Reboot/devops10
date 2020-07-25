# python中hasattr()、getattr()、setattr()函数的使用

## 1.hasattr()函数

+ hasattr() 函数用来判断某个类实例对象是否包含指定名称的属性或方法。该函数的语法格式如下：

```pytho
hasattr(obj, name)
```

其中 obj 指的是某个类的实例对象，name 表示指定的属性名或方法名。同时，该函数会将判断的结果（True 或者 False）作为返回值反馈回来。`需要注意的是name参数是string类型，所以不管是要判断变量还是方法，其名称都以字符串形式传参；`

```python
#hasattr
#判断某个类是否包含某个方法或属性
class A(object):
    def __init__(self):
        self.name = '明天'
        self.age = 19

    def sys(self):
        print('我存在')

a = A()

print(hasattr(a, 'name')) #判断是否有name属性  True
print(hasattr(a, 'age'))  #判断是否有age属性   True
print(hasattr(a, 'sys'))  #判断是否有sys    True
```

显然，无论是属性名还是方法名，都在 hasattr() 函数的匹配范围内。因此，我们只能通过该函数判断实例对象是否包含该名称的属性或方法，但不能精确判断，该名称代表的是属性还是方法。

## 2.getattr() 函数

+ getattr() 函数获取某个类实例对象中指定属性的值。没错，和 hasattr() 函数不同，该函数只会从类对象包含的所有属性中进行查找。

  ```python
  getattr(obj, name[, default])
  ```

+ obj 表示指定的类实例对象，name 表示指定的属性名，而 default  是可选参数，如果存在则返回属性值，如果不存在分为两种情况，一种是没有default参数时，会直接报错；给定了default参数，若对象本身没有name属性，则会返回给定的default值；如果给定的属性name是对象的方法，则返回的是函数对象，需要调用函数对象来获得函数的返回值；调用的话就是函数对象后面加括号，如func之于func();

  ```python
  # 2.getattr() 获取属性的性
  class A(object):
      def __init__(self):
          self.name = '测试'
          self.age = 19
  
      def sys(self):
          return 'ok'
  
  a = A()
  print(getattr(a, 'name')) #获取A属性的值,测试
  print(getattr(a, 'age')) #获取B属性的值,19
  print(getattr(a, 'sex')) #属性值不存在报错
  #Traceback (most recent call last):
  #   File "attr.py", line 29, in <module>
  #     print(getattr(a, 'sex'))
  # AttributeError: 'A' object has no attribute 'sex'
  print(getattr(a, 'sex', 'male')) #当属性不存在的时候，使用默认值，male
  print(getattr(a, 'sys')) #获取到了一个对象，<bound method A.sys of <__main__.A object at 0x7fa511d09668>>
  print(getattr(a, 'sys')()) #调用函数，接收返回值
  ```

## 3.setattr()函数

+ setattr() 函数的功能相对比较复杂，它最基础的功能是修改类实例对象中的属性值。其次，它还可以实现为实例对象动态添加属性或者方法。

  ```python
   setattr(object, name, value)
  ```

  + 给object对象的name属性赋值value，如果对象原本存在给定的属性name，则setattr会更改属性的值为给定的value；如果对象原本不存在属性name，setattr会在对象中创建属性，并赋值为给定的value；

  ```python
  class A(object):
      def __init__(self):
          self.name = '测试'
          self.age = 19
  
      def sys(self):
          return 'ok'
  
  a = A()
  setattr(a, 'name', 'newname')
  print(a.name) #newname
  ```

  一般先判断对象中是否存在某属性，如果存在则返回；如果不存在，则给对象增加属性并赋值；很简单的if-else判断：

  ```python
  if hasattr(a, 'sex'):
      print(a.sex)
  else:
      setattr(a, 'sex', 'male')
      print(a.sex) #属性不存在，给对象增加属性并赋值setattr(a, 'sex', 'male')
  print(a.sex) #属性不存在，给对象增加属性并赋值
  ```

  