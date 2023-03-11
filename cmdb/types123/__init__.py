#第一版
# import  ipaddress
# import importlib
#
# class BaseType:
#     def __init__(self,**option):
#         self.option=option
#     def __getattr__(self, item):
#         return self.option.get(item)
#     def stringify(self,value):
#         raise NotImplementedError()
#     def destringify(self,value):
#         raise NotImplementedError()
#
# class Int(BaseType):
#     def stringify(self,value):
#         try:
#             val=int(value)
#             # max=self.option.get('max')
#             max=self.max #self.max 本类没有 到父类中找， 实际调用 __getattr__魔术方法 在属性中找不到  触发 __getattr__魔术方法
#             if max and val>max:
#                 raise ValueError('too big')
#             min=self.option.get('min')
#             if min and val< min:
#                 raise ValueError('too small')
#             return str(val)  #存数据，为字符串
#         except Exception as e:
#             print('{}'.format(e))
#         # val=int(value)
#         # # max=self.option.get('max')
#         # max=self.max #self.max 本类没有 到父类中找， 实际调用 __getattr__魔术方法 在属性中找不到  触发 __getattr__魔术方法
#         # if max and val>max:
#         #     raise ValueError('too big')
#         # min=self.option.get('min')
#         # if min and val< min:
#         #     raise ValueError('too small')
#         # return str(val)  #存数据，为字符串
#     def destringify(self,value):
#         raise NotImplementedError()
# class IP(BaseType):
#     def stringify(self,value):
#         # prefix=self.prefix ##self.prefix 本类没有 到父类中找， 实际调用 __getattr__魔术方法 在属性中找不到  触发 __geta# ttr__魔术方法
#         # if prefix and not str(value).startswith(prefix):
#         #     raise ValueError('Must start with{}'.format(prefix))
#         #
#         # return str(ipaddress.ip_address(value))
#         try:
#             prefix=self.prefix ##self.prefix 本类没有 到父类中找， 实际调用 __getattr__魔术方法 在属性中找不到  触发 __geta# ttr__魔术方法
#             if prefix and not str(value).startswith(prefix):
#                 raise ValueError('Must start with{}'.format(prefix))
#             return str(ipaddress.ip_address(value))
#         except Exception as e:
#             print('测试{}'.format(e))
#
#     def destringify(self,value):
#         return value
# #aaa=get_instance(obj['type'],**obj['option']).stringify(obj['value'])
# #{'type': 'cmdb.types123.Int', 'value': 300, 'opthon': {'max': 100, 'min': 1}}
# '''
# mata={
#     "type":"cmdb.types123.IP",
#     "value":"192.168.0.1"
#     "option":{"prefix":"192.168"}
# }
# IP=get_instance(mata.get('type'),**meta.get('option'))
# print(IP.stringify('192.168.0.1'))
# '''
# def get_class(type:str):
#     m,c=type.rsplit('.',maxsplit=1)
#     mod=importlib.import_module(m)
#     cls=getattr(mod,c)
#     if issubclass(cls,BaseType):
#         return cls
#     raise TypeError('wrong type!{} is not sub class of basetype'.format(cls))
# def get_instance(type:str,**option:dict):
#     cls=get_class(type)
#     obj=cls(**option)
#     return obj#返回实例
#第二版
import  ipaddress
import importlib
class BaseType:
    def __init__(self,**option):
        self.option=option
    def __getattr__(self, item):
        return self.option.get(item)
    def stringify(self,value):
        raise NotImplementedError()
    def destringify(self,value):
        raise NotImplementedError()

class Int(BaseType):
    def stringify(self,value):
        try:
            val=int(value)
            # max=self.option.get('max')
            max=self.max #self.max 本类没有 到父类中找， 实际调用 __getattr__魔术方法 在属性中找不到  触发 __getattr__魔术方法
            if max and val>max:
                raise ValueError('too big')
            min=self.option.get('min')
            if min and val< min:
                raise ValueError('too small')
            return str(val)  #存数据，为字符串
        except Exception as e:
            print('{}'.format(e))
        # val=int(value)
        # # max=self.option.get('max')
        # max=self.max #self.max 本类没有 到父类中找， 实际调用 __getattr__魔术方法 在属性中找不到  触发 __getattr__魔术方法
        # if max and val>max:
        #     raise ValueError('too big')
        # min=self.option.get('min')
        # if min and val< min:
        #     raise ValueError('too small')
        # return str(val)  #存数据，为字符串
    def destringify(self,value):
        raise NotImplementedError()
class IP(BaseType):
    def stringify(self,value):
        # prefix=self.prefix ##self.prefix 本类没有 到父类中找， 实际调用 __getattr__魔术方法 在属性中找不到  触发 __geta# ttr__魔术方法
        # if prefix and not str(value).startswith(prefix):
        #     raise ValueError('Must start with{}'.format(prefix))
        #
        # return str(ipaddress.ip_address(value))
        try:
            prefix=self.prefix ##self.prefix 本类没有 到父类中找， 实际调用 __getattr__魔术方法 在属性中找不到  触发 __geta# ttr__魔术方法
            if prefix and not str(value).startswith(prefix):
                raise ValueError('Must start with{}'.format(prefix))
            return str(ipaddress.ip_address(value))
        except Exception as e:
            print('测试{}'.format(e))

    def destringify(self,value):
        return value
#aaa=get_instance(obj['type'],**obj['option']).stringify(obj['value'])
#{'type': 'cmdb.types123.Int', 'value': 300, 'opthon': {'max': 100, 'min': 1}}
'''
mata={
    "type":"cmdb.types123.IP",
    "value":"192.168.0.1"
    "option":{"prefix":"192.168"}
}
IP=get_instance(mata.get('type'),**meta.get('option'))
print(IP.stringify('192.168.0.1'))
'''
classes_cache={}
def get_class(type:str):
    cls=classes_cache.get(type)
    if cls:
        return cls
    # m,c=type.rsplit('.',maxsplit=1)
    # mod=importlib.import_module(m)
    # cls=getattr(mod,c)
    # classes_cache[type]=cls
    # if issubclass(cls,BaseType):
    #     return cls
    raise TypeError('wrong type!{} is not sub class of basetype'.format(cls))
instances_cache={}
def get_instance(type:str,**option:dict):
    key=",".join("{}={}".format(k,v) for k,v in sorted(option.items()))  #opton.items() dict_items([('prefix', '192.168')]) dict_items([('max', 100), ('min', 1)])
    key="{}|{}".format(type,key) #cmdb.types123.Int|max=100,min=1
    obj=instances_cache.get(type)
    if obj:
        return obj
    obj=get_class(type)(**option)
    instances_cache[key]=obj
    return obj#返回实例

def inject():
    mod=globals().get('__package__')
    print("mod",mod)

    for k,v in globals().items(): #'Int': <class '__main__.Int'>, 'IP': <class '__main__.IP'>,
        if type(v)==type and issubclass(v,BaseType) and k!="BaseType":
            print(k, type(v))  # Int <class 'type'> ,IP <class 'type'>
            classes_cache[k]=v
            classes_cache[".".join((mod,k))] =v
    print(classes_cache)

inject()



"""
print(globals())
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000000FD364AC2B0>,
 '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Users/zhanjia/PycharmProjects/cmdb/cmdb/types123/__init__.py',
  '__cached__': None, 'ipaddress': <module 'ipaddress' from 'C:\\Users\\zhanjia\\AppData\\Local\\Programs\\Python\\Python36\\lib\\ipaddress.py'>, 
  'importlib': <module 'importlib' from 'C:\\Users\\zhanjia\\AppData\\Local\\Programs\\Python\\Python36\\lib\\importlib\\__init__.py'>, 'BaseType': <class '__main__.BaseType'>,
   'Int': <class '__main__.Int'>, 'IP': <class '__main__.IP'>, 'classes_cache': {}, 
   'get_class': <function get_class at 0x000000FD36756598>, 'instances_cache': {},
    'get_instance': <function get_instance at 0x000000FD36793BF8>, 'inject': <function inject at 0x000000FD36793C80>}"""
