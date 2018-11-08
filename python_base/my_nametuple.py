from collections import namedtuple

User = namedtuple('User', ['name', 'sex', 'age'])

a = User(name='sqy', sex='boy', age='19')

print(a)

assert a.name == 'sqy' , 'name is not sqy'

# a.name = 'ghn'

a._replace(age=20)
print(a)

print(a._asdict())
print(list(a))