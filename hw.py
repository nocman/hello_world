#!/usr/bin/python
def hello(who=None):
  '''Hello-jello world. Nothing to see here, move along!'''

  if who is not None:
    hellostring = 'Hello ' + str(who) + '!'
  else:
    hellostring = 'Who\'s your daddy?!'

  print("%s" % hellostring)

if __name__ == '__main__':
  hello()
