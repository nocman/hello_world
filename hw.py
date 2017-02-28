#!/usr/bin/python
def hello(who=None):
  '''Hello-jello world. Nothing to see here, move along!'''

  if who is not None:
    message = 'Hello ' + str(who) + '!'
  else:
    message = 'Who\'s your daddy?!'

  print("%s" % message)

def add_two(a,b):
  '''It adds two arguments.'''

  if type(a) is int and type(b) is int:
    print(a+b)
  else:
    print('We\'re doomed!')

if __name__ == '__main__':
  hello()
  add_two(2,1)
