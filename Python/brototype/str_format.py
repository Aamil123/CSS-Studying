age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age)) #the numbers are optional
print('Why is {0} playing with that python?'.format(name))

print("\n",name + ' is ' + str(age) + ' years old')


#We can also name the parameters
print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))

#Python 3.6 introduced a shorter way to do named parameters, called "f-strings"
print(f'{name} was {age} years old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string

print('\n\n{0:_^11}'.format('hello'))

#you can end with a space:
print('a', end=' ')
print('b', end=' ')
print('c')

#indicate the start of a new line. An example is:
print("\nAamil is \nvery good boy in the world\n")