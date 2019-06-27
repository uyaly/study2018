import json
src_str = '{"a":{"b":[{"c":"C"},{"d":"D"},{"e":"E"}]}}'
jdict = json.loads(src_str)
class FoundException(Exception): pass
global flag
flag =False
def check_key_value(jdict,key,value):
    global flag
    #import pdb;pdb.set_trace()
    if isinstance(jdict, list):
        for element in jdict:
            check_key_value(element,key,value)
    elif isinstance(jdict, dict):
        if key in jdict.keys():
            if jdict[key] == value:
                # try :
                #     raise FoundException
                # except FoundException, e:
                flag = True
            else:
                return False
        else:
            for x in jdict.keys():
                check_key_value(jdict[x],key,value)
check_key_value(jdict,"d","D")

print(flag)