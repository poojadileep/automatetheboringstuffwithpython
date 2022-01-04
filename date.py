import re
Date = re.compile(r'\d{2}/\d{2}/\d{4}')
date = input("enter the date:")
mnth = Date.search(date)
if mnth != 00:
    day, month, year = date.split("/")
    day, month, year = int(day), int(month), int(year) 

    
    if (year%4 == 0 ) or (year%100==0 and year%400==0) :
       feb = 29
    else:
      feb=28
    
    jan = 31
    mar =31
    apr=30
    may=31
    jun=30
    july=31
    aug=31
    sep=30
    oct=31
    nov=30
    dec=31
    months =[jan,feb,mar,apr,may,jun,july,aug,sep,oct,nov,dec]
    if month>=12:
      print('not valid')
    elif day>months[month-1]:
      print('not valid')
else:
  print('valid date')   
         