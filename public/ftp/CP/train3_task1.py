Python 3.7.3 (default, Apr  3 2019, 19:16:38) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> bool(1)
True
>>> bool(0)
False
>>> int(True)
1
>>> int (False)
0
>>> a=True
>>> not a
False
>>> b=False
>>> a and b
False
>>> a or b
True
>>> a and b or a
True
>>> 5<10
True
>>> a=1
>>> b=1
>>> a==b
True
>>> d=[1,0]
>>> a is b
True
>>> a is d
False
>>> a in d
True
>>> a is not d
True
>>> d is a
False
>>> 
