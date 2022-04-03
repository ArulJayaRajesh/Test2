#pip --version
#pip install python-dateutil --upgrade
"""
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
"""
# 03-JAN-2022
# 03/01/22
# JAN:Monday:2022
# 2022:01:03

# JAN:03
# 2022

# 24:min:sec
"""
import datetime

x=datetime.datetime.now()

dd=str(x.strftime("%d"))
mm=str(x.strftime("%b"))
yy=str(x.strftime("%Y"))
print(dd+"-"+mm+"-"+yy)

dd=str(x.strftime("%d"))
mm=str(x.strftime("%m"))
yy=str(x.strftime("%y"))
print(dd+"/"+mm+"/"+yy)
dd=str(x.strftime("%m"))
mm=str(x.strftime("%A"))
yy=str(x.strftime("%Y"))
print(dd+":"+mm+":"+yy)

import datetime

x=datetime.datetime.now()
dd=x+datetime.timedelta(days=-2)
print(dd)
"""
from datetime import date
from dateutil import relativedelta
a = date(1999,1,20)
b = date(2022,1,3)
#print((a-b).days)
r = relativedelta.relativedelta(b, a)
print(r.months + (12*r.years))














