#!/usr/bin/python
def hello(who=None):
  '''Hello-jello world. Nothing to see here, move along!'''

  if who is not None:
    message = 'Hello ' + str(who) + '!'
  else:
    message = 'Who\'s your daddy?!'

  print("%s" % message)

if __name__ == '__main__':
  hello()
