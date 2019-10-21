from datetime import date
from datetime import timedelta
from itertools import cycle 
# List of interns
interns = ['Isabel','Kai','Lynette','Gladys','Shanique','Tadelin']
intern_cycle = cycle(interns)

# List of Thursdays we don't meet in our groups
no_session = { 
	date(2019,11,5), date(2019,11,7), date(2019,11,28), date(2019,12,26),
	date(2020,1,2), date(2020,1,9), date(2020,1,30), date(2020,2,27),
	date(2020,2,20), date(2020,4,2), date(2020,4,9), date(2020,4,16),
	date(2020,6,4)
	}

# Start date
start_date = date(2019,10,24)

# End date
end_date = date(2020,6,7)

# make a list of all the thursdays between start and end:
sessions=[]
date = start_date
for intern in intern_cycle:
	if date not in no_session:
		print date, intern
	if date > end_date:
		break
	date += timedelta(days=7)







