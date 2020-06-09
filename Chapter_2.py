Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Print('I'm so happy to learn to code')
      
SyntaxError: invalid syntax
>>> print("I'm so happy to be learning how to code in Python!!
      
SyntaxError: EOL while scanning string literal
>>> print("I'm so happy to be learning how to code in Python!!")
I'm so happy to be learning how to code in Python!!
>>> print('I\'m so happy to be learning how to code in Python!!')
I'm so happy to be learning how to code in Python!!
>>> print('\"Kumusta\" is \"Hello\" in Tagalog!')
"Kumusta" is "Hello" in Tagalog!
>>> print("Here is \na sentence \nsplit up \non different lines!")
Here is 
a sentence 
split up 
on different lines!
>>> reader = Yingkai
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    reader = Yingkai
NameError: name 'Yingkai' is not defined
>>> reader = "Yingkai"
>>> print(reader)
Yingkai
>>> favorite_number = 3
>>> type(facorite_number)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    type(facorite_number)
NameError: name 'facorite_number' is not defined
>>> favorite_number = 3
>>> type(favorite_number)
<class 'int'>
>>> favorite_number= '3'
>>> type(favorite_number)
<class 'str'>
>>> foods = 'pasta'
>>> f"I like {food}"
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f"I like {food}"
NameError: name 'food' is not defined
>>> food = pasta
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    food = pasta
NameError: name 'pasta' is not defined
>>> food = pasta
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    food = pasta
NameError: name 'pasta' is not defined
>>> 
>>> 
>>> food = "pasta"
>>> f"I like {food}"
'I like pasta'
>>> feeling = happy
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    feeling = happy
NameError: name 'happy' is not defined
>>> feeling = "happy"
>>> print(f"I'm so {feeling} to learn how to code!!")
I'm so happy to learn how to code!!
>>> meltiline_sentence = """
	A Sentence
	On many
	Different
	Lines!!
"""
>>> print(f"{multiline_sentence}")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(f"{multiline_sentence}")
NameError: name 'multiline_sentence' is not defined
>>> print(f"{meltiline_sentence}")

	A Sentence
	On many
	Different
	Lines!!

>>> print("Hi, I am Yingkai")
Hi, I am Yingkai
>>> print("\"live as if you were to die tomorrow.\"-Unknown")
"live as if you were to die tomorrow."-Unknown
>>> mood = happy
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    mood = happy
NameError: name 'happy' is not defined
>>> mood = "happy"
>>> print(f"Today I am feeling {mood}!!")
Today I am feeling happy!!
>>> multilineSentence = """
	Memes are the the cure to
	Everything, including
	Coronavirus.
"""
>>> print("f{multilineSentence}")
f{multilineSentence}
>>> print(f"{multilineSentence}")

	Memes are the the cure to
	Everything, including
	Coronavirus.

>>> 