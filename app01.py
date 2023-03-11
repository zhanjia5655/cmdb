
import importlib
import json
from cmdb.types123 import get_instance
jsonstr="""
{
"type":"cmdb.types123.Int",
"value":12,
"option":{"max":100,"min":1}  
}
"""
"""
type 类型
value 数值
option 限制条件  
"""
meta={
    "type":"cmdb.types123.IP",
    "value":"192.168.0.1",
    "option":{"prefix":"192.168"}
}


obj=json.loads(jsonstr)
#print(obj["option"],obj["option"].items(),obj["option"].keys(),obj["option"].values())
# {'max': 100, 'min': 1} dict_items([('max', 100), ('min', 1)]) dict_keys(['max', 'min']) dict_values([100, 1])
aaa={(k,v)for k,v in  sorted(obj["option"].items())}
# print("aaa",aaa) #aaa {('max', 100), ('min', 1)}
# print(123,obj)#{'type': 'cmdb.types123.Int', 'value': 12, 'option': {'max': 100, 'min': 1}}
#{'type': 'cmdb.types123.Int', 'value': 300, 'opthon': {'max': 100, 'min': 1}}
# type=obj['type']
# m,c=type.rsplit('.',maxsplit=1)
# print(m,c)  #cmdb.types123 Int type(m) <class 'str'>
# #
# mod=importlib.import_module(m)
#
# cls=getattr(mod,c)
# print(cls)
# Int校验-----------------------
try:
    aaa=get_instance(obj['type'],**obj['option']).stringify(obj['value']) # 返回一个实例，将参数传进去，再调实例的方法
except Exception:
    print('{}'.format(Exception))
#print(12311, type(aaa), aaa) #12311 <class 'str'> 12
#aaa=get_instance(obj['type'],**obj['option']).stringify(obj['value'])
# #IP校验------------------------------------
# try:
#     IP=get_instance(meta.get('type'),**meta.get('option'))
#     print(123123,IP.stringify('192.168.22.1'))
# except Exception:
#     print('123{}'.format(Exception))
