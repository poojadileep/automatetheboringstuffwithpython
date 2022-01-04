def returnstring(list):
  a=''
  if len(list)==0 :
    print('oops! List is empty')
  else :
    a = ''
    a += ",".join(list[0:-1])
    a += " " + "and" + " " + list[-1]
    print(a)

spam = ['apples', 'bananas', 'tofu', 'cats']
returnstring(spam)
