"""
Turn dict into class object
 dictionary = {
     "name": "Steve",
     "age": 18,
     "dob": "08/23/2000",
     0: {
         "name": "April",
         "age": 23,
         "hi-how-are-you": "good",
         "steve joe": "o"
         }
     }
 }
as you can see the it supports nested dictionarys also ints as keys

object = Object(dictionary)
object.name -> Steve
object['name'] -> Steve
object._0.name -> April
object[0].name -> April
object[0].hi_how_are_you -> good
object[0]['hi-how-you'] > good
object[0]['steve joe'] ->
object[0].steve_joe -> o
"""


from typing import Any


class Objectify:
    def __init__(self, d: dict = {}, objectify:bool=True) -> None:
        if objectify: self.toObject(d)
    

    def get(self, key, defaults=None) -> Any:
        if type(key) == type(2):
                key = "_" + str(key)
        key=str(key).replace(" ", "_").replace("-", "_")
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return defaults
    
    def set(self, key:Any, value:Any) -> None:
        key=str(key).replace(" ", "_").replace("-", "_")
        if type(key) == type(2):
                key = "_" + str(key)
        if type(value) == type({}):
            setattr(self, key, Objectify(value))
        else:   
            setattr(self, key, value)
    
    def toObject(self, d: dict) -> None:
        for key, value in iter(d.items()):
            if type(key) == type(2):
                key = "_" + str(key)
            key=key.replace(" ", "_").replace("-", "_")
            if type(value) == type({}):
                setattr(self, key, Objectify(value))
            else:
                setattr(self, key, value)
    
    def toDict(self) -> dict:
        dict = {}
        for key, value in iter(self.__dict__.items()):
            if type(value) == type(self):
                dict[key] = value.toDict()
            else:
                dict[key] = value
        return dict


    def __getitem__(self, name: Any) -> Any:
        name=str(name).replace(" ", "_").replace("-", "_")
        if type(name) == type(2):
            name = "_" + name
        if hasattr(self, name):
            return getattr(self, name)
    
    def __setitem__(self, name: Any, value: Any) -> None:
        if type(value) == type({}):
            value = Objectify(value)
        self.set(name, value)
    
    def __repr__(self):
        return str(self.toDict())
