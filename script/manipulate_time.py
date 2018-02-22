from datetime import tzinfo, timedelta, datetime


def time_min_1_mm( timeStartString ):   
	format = '%Y-%m-%d %H:%M:%S'
	timeStart = datetime.strptime(timeStartString, format)
	timeStart_min_1_mm = timeStart - timedelta(seconds = 1)
	#print type(timeStart_min_1_mm)
	a = str(timeStart_min_1_mm)
	#print type(a)
	print a
	return timeStart_min_1_mm;


timeStartString = '2018-01-14 14:48:55'
print timeStartString

print time_min_1_mm(timeStartString)





