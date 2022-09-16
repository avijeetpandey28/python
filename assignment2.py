Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# ans1
print("\"Learning Python\"")
"Learning Python"


'''
ans
2
'''
'\nans\n2\n'
a = 2
b = 'sonu'
c = 3.0
d = 30
print(a,b,c,d,sep='\n')
2
sonu
3.0
30
#ans 3
g = 35
h = True
i = "MySirG"
j = 5.46
k = 3+4j
print(type(a))
<class 'int'>
KeyboardInterrupt
print(type(g))
<class 'int'>
print(type(h))
<class 'bool'>
print(type(i))
<class 'str'>
print(type(j))
<class 'float'>
print(type(k))
<class 'complex'>

#ans4
a = 10
b = 10
print(id(a),id(b))
1765339693584 1765339693584

#ans5
g = 35
h = True
i = "MySirG"
j = 5.46
k = 3+4j
print(type(a),id(a)
      
SyntaxError: multiple statements found while compiling a single statement
print(type(a),id(a))
      
<class 'int'> 1765339693584
print(type(g),id(g))
      
<class 'int'> 1765339694384
print(type(h),id(h))
      
<class 'bool'> 140706247560040
print(type(i),id(i))
      
<class 'str'> 1765352937712
print(type(j),id(j))
      
<class 'float'> 1765379170416
print(type(k),id(k))
      
<class 'complex'> 1765379173584
#ans6
      
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
 #ans7
help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.

#ans8
import a1
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    import a1
ModuleNotFoundError: No module named 'a1'
import a1
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    import a1
ModuleNotFoundError: No module named 'a1'
import A1
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    import A1
ModuleNotFoundError: No module named 'A1'
import a1
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    import a1
ModuleNotFoundError: No module named 'a1'
import a2
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    import a2
ModuleNotFoundError: No module named 'a2'

========================= RESTART: C:/Users/avije/a2.py ========================

========================= RESTART: C:/Users/avije/a2.py ========================
2
import a2
2
print(a2.x)
2

#ans 9
True
True
False
False
None

#ans 10
from datatime import datetime
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    from datatime import datetime
ModuleNotFoundError: No module named 'datatime'
from datetime import datetime
dt = datetime.today
print(dt)
<built-in method today of type object at 0x00007FF8B9E88CD0>
from datetime import datetime
dt = datetime.today()
print(dt)
SyntaxError: multiple statements found while compiling a single statement
from datetime import datetime
dt = datetime.today()
print(dt)
2022-09-16 16:54:04.199989
d1 = dt.strftime("%d-%m-%Y and #I:%M %p")
print(d1)
16-09-2022 and #I:54 PM
