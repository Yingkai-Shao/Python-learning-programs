Python (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3>7
False
>>> 3<7
True
>>> mood=happy
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    mood=happy
NameError: name 'happy' is not defined
>>> mood='happy'
>>> print(mood)
happy
>>> 4>=3
True
>>> 3>=3
True
>>> 1>=3
False
>>> 3<=3
True
>>> <4=5
SyntaxError: invalid syntax
>>> 4<=5
True
>>> 10 = 10
SyntaxError: cannot assign to literal
>>> 10=10
SyntaxError: cannot assign to literal
>>> 10==10
True
>>> 10=='10'
False
>>> 'five'!=5
True
>>> 10!=11
True
>>> pizzaHasPepperoni = True
>>> pizzaHasMushrooms = False
>>> pizzaHasPepperoni and pizzaHasMuchrooms
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    pizzaHasPepperoni and pizzaHasMuchrooms
NameError: name 'pizzaHasMuchrooms' is not defined
>>> pizzaHasPepperoni and pizzaHasMuchrooms True
SyntaxError: invalid syntax
>>> age = 100/10+1
>>> print(f'Hi, my name is Yingkai Shao. I am {age} years old.')
Hi, my name is Yingkai Shao. I am 11.0 years old.
>>> magicNum = 10**2*15%6
>>> print(magicNum)
0
>>> print(15%6)
3
>>> magicNum=10**2*(15%6)
>>> print(magicNum)
300
>>> magicNum=10**2*(15%6)+3*(35%12)
>>> print(magicNum)
333
>>>dolores_chocolte_chips = 13
teddy_chocolate_chips = 9
teddy_chocolate_chips > dolores_chocolte_chips
print(teddy_chocolate_chips > dolores_chocolte_chips)
