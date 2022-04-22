# what-a-dict
[![Downloads](https://static.pepy.tech/personalized-badge/what-a-dict?period=total&units=abbreviation&left_color=black&right_color=brightgreen&left_text=downloads)](https://pepy.tech/project/what-a-dict)
Dictionary class with advanced functionality

## Installation
Make sure your are using the up-to-date version of pip
```shell
pip install --upgrade pip
```

Then install the package
```shell
pip install what-a-dict
```

## Usage

import the class first
```python
from wad import Dict
```
### Instance Creation
Use it as a dictionary class with string keyword arguments:
```python
# style1
members=Dict(name="SYHuang",
             discriptions="Please Subscribe")
# style2
d={"name":"SYHuang",
    "discriptions":"Please Subscribe"}
members=Dict(**d)
```

It is also allowed to create instance of Dict which value of traditional dict or Dict
```python
# style1
members=Dict(
    friends={
        "ge62":"computer",
        "iphone":"phone"})
# style2
members=Dict(
    friends=Dict(
        ge62="computer",
        iphone="phone"))
```

### Usage
Items can be get as in a dict
```python
members["friend"]
```

The keys are also the attribute of this object
```python
members.friend
```

other functions like iteration, update are the same as in dict:
```python
# update (you can put in a hybrid with "dict"s and "Dict"s)
members.update({"friends":Dict(ge62="good computer")})

# iteration
for k,v in members.items():
    pass

# concatenation
members_new=Dict(members,**{"friends":Dict(ge62="good computer")})
###
```



I provided a way of pretty print FYI:
```python
members.repr_()
# print out:
```
```
- layer1 key1: value
- layer1 key2(if it is a list/tuple): value[0] * (lenth of the list/tuple)
- layer1 key3(if it is a Dict):
    - layer2 ke1{a Dict}:
        - layer3 ke1: value
```

(Example showing for iterable objects can be further extend to numpy array or other tensors, to be discussed)