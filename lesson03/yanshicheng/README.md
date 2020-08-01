# 分析as_view类方法

## DRF的as_view

* view.view 赋值 给 view 
* 用csrf_exempt()方法去掉了csrf的认证

## Django中的as_view

* 一个闭包函数
* 初始化一个实例对象并增加 request args kwargs 对象
* 增加属性后调用 dispatch 方法
* 返回view



# 反射的用法

* getattr  返回对象的属性值
* hasattr 判断对象的属性值
* setattr  设置对象的属性值