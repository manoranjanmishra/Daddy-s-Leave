#assesing the correctness of daddy's leaves

#notes about how data is stored in this program:
#Dates in the calendar are [yyyy,mm,dd,w,*] if leave, *=type,desc,duration
#Leaves are [start,end,type,desc,duration] start and end are dates without w,*

def calendar(sy,ey,sd):
	#returns a calendar:WORKING
	cal=[]
	year=sy
	ly=False
	wd=sd
	cm=[31,28,31,30,31,30,31,31,30,31,30,31]
	while (year<=ey):
		yr=[]
		day=0
		if (year%4==0) & (year%400!=0):
			ly=True
			days=366
			cm[1]=29
		else:
			ly=False
			days=365
			cm[1]=28
		month=[]
		mc=0
		md=0
		while (day<days):
			month=month+[[year,mc+1,md+1,wd]]
			day=day+1
			md=md+1
			wd=wd+1
			if (md==cm[mc]):
				md=0
				yr=yr+[month]
				month=[]
				mc=mc+1
			if (wd==7):
				wd=0

		cal=cal+[yr]
		year=year+1

	return cal
def printcalcmdline(yr,month,calendar,basey):
	#prints calendar as a readble calendar to thecommandline:WORKING
	year=yr-basey
	yr=calendar[year]
	mh=yr[month]
	i=0
	day=0
	print "Sun"+"\t"+"Mon"+"\t"+"Tue"+"\t"+"Wed"+"\t"+"Thu"+"\t"+"Fri"+"\t"+"Sat"
	while (i<6):
		j=0
		while (j<7):
			if (day<len(mh)):
				di=mh[day]
			else:
				break
			if (j==di[3]):
				s="%d"%di[2]
				a=4
				while a<len(di):
					s=s+"%d"%di[a]
					a=a+1
				print s,"\t",
				day=day+1
			else:
				print "\t",
			j=j+1
		if (day>=len(mh)):
			print
			break
		print "\n"
		i=i+1
	return 0
#def printgovtcalendar(year,calendar):
	#prints a Govt. Calendar for the specific year from the calendar, with only Public Holidays
def ascsort(date1,date2):
	#returns a array with dates sorted in ascending order:WORKING
	a=[]
	b=[]
	a=a+date1
	b=b+date2
	i=0
	while i<3:
		if date1[i]<date2[i]:
			a=date1
			b=date2
			return [a,b]
		elif date1[i]>date2[i]:
			a=date2
			b=date1
			return [a,b]
		i=i+1
	return [a,b]
def noofdays(date1,date2):
	#counts number of days between date1 and date2, both included:WORKING
	start=[]
	end=[]
	start=start+ascsort(date1,date2)[0]
	end=end+ascsort(date1,date2)[1]
	start[1]=start[1]-1
	end[1]=end[1]-1
	i=start[0]
	days=0
	while (i<=end[0]):
		if (i%4==0) & (i%400!=0):
			days=days+366
		else:
			days=days+365
		i=i+1
	caln=[31,28,31,30,31,30,31,31,30,31,30,31]
	calp=[31,29,31,30,31,30,31,31,30,31,30,31]
	i=0
	if (start[0]%4==0) and (start[0]%400!=0):
		cal1=calp
	else:
		cal1=caln
	while i<start[1]:
		days=days-cal1[i]
		i=i+1
	i=end[1]+1
	if (end[0]%4==0) and (end[0]%400!=0):
		cal2=calp
	else:
		cal2=caln
	while i<12:
		days=days-cal2[i]
		i=i+1
	days=days-start[2]-(cal2[end[1]]-end[2])
	return days+1
def comesafter(date,a):
	#returns True if date comes on or after a:WORKING
	comp=ascsort(a,date)
	if comp==[a,date]:
		return True
	else:
		return False
def comesbefore(date,a):
	#returns True if date comes before a:
	comp=ascsort(date,a)
	if comp==[date,a]:
		return True
	else:
		return False
def isinrange(date,a,b):
	#returns True if date falls in range of start and end, else false:WORKING
	start=ascsort(a,b)[0]
	end=ascsort(a,b)[1]
	c1=comesafter(date,start)
	c2=comesbefore(date,end)
	if (c1==True) and (c2==True):
		return True
	else:
		return False
def enterleavedata(listofleaves,calendar):
	#returns the calendar with leaves marked:WORKING
	newcal=[]
	newcal=newcal+calendar
	i=0
	while i<len(listofleaves):
		entry=listofleaves[i]
		start=entry[0]
		end=entry[1]
		type=entry[2]
		desc=entry[3]
		duration=entry[4]
		y=0
		while y<len(calendar):
			m=0
			while m<len(calendar[y]):
				d=0
				while d<len(calendar[y][m]):
					day=calendar[y][m][d]
					if isinrange(day,start,end):
						newcal[y][m][d]=newcal[y][m][d]+[type,desc,duration]
					d=d+1
				m=m+1
			y=y+1
		i=i+1
	return newcal
def readdate(date):
	#reads date and numbers from a string:WORKING
	i=0
	dout=[]
	val=""
	while i<len(date):
		if (date[i]=="/") or (i+1 == len(date)):
			if (i+1==len(date)):
				val=val+date[i]
			if val!="":
				dout=dout+[int(val)]
			val=""
			i=i+1
			continue
		else:
			val=val+date[i]
			i=i+1
	if len(dout)==1:
		return dout[0]
	else:
		return dout
def readleavedata(filedata):
	#returns an array containing leave data:WORKING
	i=0
	leaves=[]
	while i<len(filedata):
		line=filedata[i]
		j=0
		linea=[]
		while j<len(line):
			a=readdate(line[j])
			if (j==2):
				desc=line[j+1]
				linea=linea+[a,desc]
				j=j+1
			else:
				linea=linea+[a]
			j=j+1
		leaves=leaves+[linea]
		i=i+1
	return leaves
def calarray(calendar):
	#returns calendar data as a one-dim array
	cala=[]
	y=0
	while y<len(calendar):
		m=0
		while m<len(calendar[y]):
			d=0
			while d<len(calendar[y][m]):
				day=calendar[y][m][d]
				cala=cala+[day]
				d=d+1
			m=m+1
		y=y+1
	return cala
#def arraycal(calendar):
	#Takes a onedimensional array, and returns a calendar
def secondsaturday(calendar):
	#marks the Second Saturday in each month as a Holiday
	rcalendar=[]
	rcalendar=rcalendar+calendar
	y=0
	while y<len(calendar):
		m=0
		while m<len(calendar[y]):
			d=0
			satc=0
			while d<len(calendar[y][m]):
				if (calendar[y][m][d][3]==6):
					satc=satc+1
				if (satc==2):
					rcalendar[y][m][d]=rcalendar[y][m][d]+[0,"Second Saturday",1]
					break
				d=d+1
			m=m+1
		y=y+1
	return rcalendar
def standardholidays(calendar):
	#Adds Holidays whose date doesn't vary year to year:WORKING
	rcalendar=[]
	rcalendar=rcalendar+calendar
	y=0
	while y<len(calendar):
		m=0
		while m<len(calendar[y]):
			d=0
			while d<len(calendar[y][m]):
				div=calendar[y][m][d]
				suffix=[]
				date=[div[2],div[1]]
				if (date==[23,1]):
					suffix=[0,"Netaji S.C.Bose Jayanti & V.S.Sai Jayanti",1]
				elif (date==[26,1]):
					suffix=[0,"Republic Day",1]
				elif (date==[5,3]):
					suffix=[0,"Panchayati Raj Diwas & Biju Pattnaik Jayanti",1]
				elif (date==[1,4]):
					suffix=[0,"Utkal Divas",1]
				elif (date==[14,4]):
					suffix=[0,"Dr.B.R Ambedkar Jayanti",1]
				elif (date==[15,8]):
					suffix=[0,"Independence Day",1]
				elif (date==[2,10]):
					suffix=[0,"Gandhi Jayanti",1]
				elif (date==[25,12]):
					suffix=[0,"Christmas",1]
				if len(suffix)!=0:
					rcalendar[y][m][d]=div+suffix
				d=d+1
			m=m+1
		y=y+1
	return rcalendar
def isleave(day,calendar,basey,mode):
	#WORKING
	#mode"0/3":returns True if given day is National Holiday or Optional Holiday, else returns False
	#mode"1/2":returns True if given day is EL or E.O.L, else False
	if (mode==0) or (mode==3):
		type=[0,3]
	elif (mode==1) or (mode==2):
		type=[1,2]
	else:
		return False
	if (day[0]>=basey):
		y=day[0]-basey
		m=day[1]-1
		d=day[2]-1
	else:
		y=day[0]
		m=day[1]
		d=day[2]
	din=calendar[y][m][d]
	if len(din)<5:
		return False
	verdict=False
	i=0
	while i<len(type):
		j=4
		while j<len(din):
			if (type[i]==din[j]):
				verdict=True
				break
			j=j+3
		if (verdict==True):
			break
		i=i+1
	return verdict
def sixdaylogic(date,calendar,basey,many,days,skip):
	#returns true if present for "many" in "days",after skipping "skip" days at the beginning.:TRY
	if (many>days):
		many,days=days,many
	day=date[:]
	cala=calarray(calendar)
	i=noofdays(day,[2004,01,01])-(1+skip)
	#if (i+1)<days:
	#	return True
	dcount=0
	count=0
	while True:
		if dcount==days:
			break
		i=i-1
		x=cala[i]
		c1a=(x[3]==0)
		c1b=isleave(x,calendar,basey,0)
		c3=isleave(x,calendar,basey,1)
		c4=c1a or c1b
		if not(c4):
			dcount=dcount+1
			if not(c3):
				count=count+1
			else:
				if(many==days):
					break
	if count>=many:
		return True
	else:
		return False
def abccheck(a,b,c,calendar,basey):
	#WORKING:DON'T USE ON EOL:DON'T USE AT ALL
	#if b is a Sunday/National Holiday, it is a valid leave only if a & c are leaves. returns True if b is a leave
	m=[]
	m=m+b
	if (b[0]>=basey):
		m[0]=b[0]-basey
		m[1]=b[1]-1
		m[2]=b[2]-1
	c1=isleave(m,calendar,basey,0)	#National Holiday
	c2=(calendar[m[0]][m[1]][m[2]][3]==0)	#Sunday
	c12=c1 or c2 #b is a Sunday or a National Holiday
	c3=isleave(a,calendar,basey,1)	#a is a leave day
	c4=isleave(c,calendar,basey,1)	#c is a leave day
	c34= c3 and c4
	c5=isleave(b,calendar,basey,1)	#b is a leave day
	if not c5:
		return False
	else:
		if not c12:
			return True
		else:
			if c34:
				return True
			else:
				return False
def legend(type):
	if type==0:
		s="National Holiday"
	elif type==1:
		s="E.L"
	elif type==2:
		s="E.O.L"
	elif type==3:
		s="Optional Holiday"
	return s
def whatholiday(date,calendar,basey,leave):
	#Is the date a holiday or not, and why:WORKING
	answer=""
	day=[]
	day=day+date
	if day[0]>=basey:
		day[0]=day[0]-basey
		day[1]=day[1]-1
		day[2]=day[2]-1
	div=calendar[day[0]][day[1]][day[2]]
	if len(div)<5:
		return "WORKING DAY"
	if leave==1:
		c1=isleave(date,calendar,basey,1)
		if c1==True:
			why=""
			a=4
			while a<len(div):
				if (div[a]==1) or (div[a]==2):
					why=div[a+1]
				a=a+3
			answer=answer+why
	if div[3]==0:
		if len(answer)!=0:
			answer=answer+" & "
		answer=answer+"Sunday"
	i=4
	while i<len(div):
		if (div[i]==0):
			if len(answer)!=0:
				answer=answer+" & "
			answer=answer+div[i+1]
		i=i+3
	return answer
#Leave checking functions and rules only after this line.
def checkleave1(leavedata):
	#checks if the duration mentioned in the leave is actually correct
	i=0
	errors=[]
	errorc=1
	while i<len(leavedata):
		entry=leavedata[i]
		givdurn=entry[4]
		calcdurn=noofdays(entry[0],entry[1])
		if (calcdurn!=givdurn):
			s="Error #%d: %d-%d-%d to %d-%d-%d is %d days, not %d days"%(errorc,entry[0][0],entry[0][1],entry[0][2],entry[1][0],entry[1][1],entry[1][2],calcdurn,givdurn)
			errors=errors+[(i,s,calcdurn)]
			errorc=errorc+1
		i=i+1
	return errors
def checkleave3(calendar,leavedata):
	#prefix and suffix leaves: a national holiday/sunday or combination at the beginning or end of the leave period cannot be counted as part of the leave period
	#personalnote:leaves need to be modified for this function to work. Work with leave array? or Calendar array??
	#For E.L all holidays are holidays. For E.O.L a holiday will be considered as a holiday (and NOT leave) if a)The day prior is a working day marked present b)6 prev days have no valid leaves
	#eol=6 will check for prev 6 working days, eol=1 checks for prev working day
	cala=calarray(calendar)
	crxns=[]
	i=0
	while i<len(cala):
		cala[i]=[[],[]]+cala[i]
		i=i+1
	i=0
	while i<len(leavedata):
		crxns=crxns+[[[],[]]]
		entry=leavedata[i]
		index=i
		start=entry[0]
		end=entry[1]
		type=entry[2]
		duration=entry[4]
		if (type==0) or (type==3):
			i=i+1
			continue
		j=noofdays(start,[2004,1,1])-1
		jmax=noofdays(end,[2004,1,1])
		skip=0
		while (isinrange(cala[j][2:5],start,end)):
			if (isleave(cala[j][2:5],calendar,2004,1)==False):
				j=j+1
				continue
			if (type==1):
				wrongleave=False
				c1=(isleave(cala[j][2:5],calendar,2004,0)) or (cala[j][5]==0)
				if c1==True:
					if (j>0):
						a=cala[j-1]
						if (len(a[0])!=0):
							c2a=False
						else:
							c2a=isleave(cala[j-1][2:5],calendar,2004,1)
					else:
						c2a=False
					if (j+1<len(cala)):
						c=cala[j+1]
						if (len(c[0])!=0):
							c2b=False
						else:
							c2b=isleave(cala[j+1][2:5],calendar,2004,1)
					else:
						c2b=False
					c2=c2a and c2b
					if c2==True:
						wrongleave=False
					else:
						wrongleave=True
				else:
					wrongleave=False
				if (wrongleave==True) and (noofdays(cala[j][2:5],start)<duration):
					cala[j][0]=cala[j][0]+["P"]
					cala[j][1]=cala[j][1]+[index]
				else:
					break
			elif (type==2):
				wrongleave=False
				c1a=isleave(cala[j][2:5],calendar,2004,0)
				if (cala[j][5]==0):
					c1b=sixdaylogic(cala[j][2:5],calendar,2004,6,6,skip)
				else:
					c1b=False
				c1= c1a or c1b
				if c1==True:
					if (j>0):
						a=cala[j-1]
						if len(a[0])!=0:
							c2a=False
						else:
							c2a=isleave(cala[j-1][2:5],calendar,2004,1)
					else:
						c2a=False
					if (j+1<len(cala)):
						c=cala[j+1]
						if len(c[0])!=0:
							c2b=False
						else:
							c2b=isleave(cala[j+1][2:5],calendar,2004,1)
					else:
						c2b=False
					c2=c2a and c2b
					if c2==True:
						wrongleave=False
					else:
						wrongleave=True
				else:
					wrongleave=False
				if (wrongleave==True) and (noofdays(cala[j][2:5],start)<duration):
					cala[j][0]=cala[j][0]+["P"]
					cala[j][1]=cala[j][1]+[index]
					skip=skip+1
				else:
					skip=0
					break
			j=j+1
		jmin=noofdays(start,[2004,1,1])-1
		j=noofdays(end,[2004,1,1])-1
		while (isinrange(cala[j][2:5],start,end)):
			if (isleave(cala[j][2:5],calendar,2004,1)==False):
				j=j-1
				continue
			if (type==1):
				wrongleave=False
				c1=(isleave(cala[j][2:5],calendar,2004,0)) or (cala[j][5]==0)
				if c1==True:
					if j+1<len(cala):
						c=cala[j+1]
						if len(c[0])!=0:
							c2b=False
						else:
							c2b=isleave(c[2:5],calendar,2004,1)
					else:
						c2b=False
					if j>0:
						a=cala[j-1]
						if len(a[0])!=0:
							c2a=False
						else:
							c2a=isleave(a[2:5],calendar,2004,1)
					else:
						c2a=False
					c2 = c2a and c2b
					if c2==True:
						wrongleave=False
					else:
						wrongleave=True
				else:
					wrongleave=False
				if (wrongleave==True) and (noofdays(cala[j][2:5],end)<duration):
					cala[j][0]=cala[j][0]+["S"]
					cala[j][1]=cala[j][1]+[index]
				else:
					break
			elif (type==2):
				pass
			j=j-1
		i=i+1
	i=0
	while i<len(cala):
		if (len(cala[i][0])==0) and (len(cala[i][1])==0):
			i=i+1
			continue
		else:
			j=0
			while j<len(cala[i][0]):
				type=cala[i][0][j]
				index=cala[i][1][j]
				if type=="P":
					crxns[index][0]=crxns[index][0]+[cala[i][2:5]]
				elif type=="S":
					crxns[index][1]=crxns[index][1]+[cala[i][2:5]]
				j=j+1
		i=i+1
	return crxns
##main program starts here

# Part 1: Read Leave file, and generate raw array of leave data from file.
leavefile=open("leave.txt",'r')
rawleaves=[]
for entry in leavefile:
	i=0
	item=""
	leaveentry=[]
	while i<len(entry):
		if (entry[i]==",") or (i+1==len(entry)):
			#personal note: last char is end-of-line, so no problem if last character is omitted
			leaveentry=leaveentry+[item]
			item=""
		else:
			item=item+entry[i]
		i=i+1
	rawleaves=rawleaves+[leaveentry]
leavefile.close()

# Part 2: Generate calendar, extract numeric leave data from file, add leave data to calendar
maincal=calendar(2004,2018,4)
mainleaves=readleavedata(rawleaves)
calleaves=enterleavedata(mainleaves,maincal)
calleaves=secondsaturday(calleaves)
calleaves=standardholidays(calleaves)
checkarray=calarray(calleaves)
#print "Do you want to print(P) or export(E) leave data as a calendar?"

# Part 3: Check for errors in leaves and print errors
allerrchks=[]
errormsgs="Error Messages:"
errorsp=False
#Check if calculated durations match
durerror=checkleave1(mainleaves)
if len(durerror)!=0:
	errorsp=True
	i=0
	errormsgs=errormsgs+"\n"+"%d duration errors"%(len(durerror))
	while i<len(durerror):
		error=durerror[i]
		errormsgs=errormsgs+"\n"+error[1]
		i=i+1
else:
	errormsgs=errormsgs+"\n"+"0 Duration Errors"
#Check if Sundays or National Holidays marked as EL,EOL are valid.

#Check if anyleaves have any prefix or sufix dates
#Check if consecutive leave-days have same or different leave types
i=0
typeerr=""
tec=0
while i<(len(checkarray)-1):
	day1=checkarray[i]
	day2=checkarray[i+1]
	c1a=comesafter(day2,day1)
	c1b=(noofdays(day1,day2)==2)
	c1=c1a and c1b
	c2=(isleave(day1[0:3],calleaves,2004,1) and isleave(day2[0:3],calleaves,2004,1))
	c3=(c1) and (c2)
	if c3==True:
		if day1[4]!=day2[4]:
			s1="%d/%d/%d is %s"%(day1[0],day1[1],day1[2],legend(day1[4]))
			s2="%d/%d/%d is %s"%(day2[0],day2[1],day2[2],legend(day2[4]))
			tec=tec+1
			s="Error %d: "%(tec)+s1+" whereas "+s2
			typeerr=typeerr+"\n"+s
	i=i+1
if tec==0:
	errormsgs=errormsgs+"\n"+"No Type Mismatches"
else:
	errormsgs=errormsgs+"\n"+"%d Type Mismatches"%(tec)+typeerr
	errorsp=True
if True:
	print errormsgs
#put and remove statements here for testing this program
arrtest=calarray(calleaves)
i=0
s1=""
s2=""
lvs=0
while i<len(arrtest):
	div=arrtest[i]
	day=[div[0],div[1],div[2]]
	if isleave(day,calleaves,2004,1):
		s1=s1+"%r\n"%(arrtest[i])
		lvs=lvs+1
	if isleave(day,calleaves,2004,0):
		s2=s2+"%r\n"%(arrtest[i])
	i=i+1
print s1
print "Leave Days: %d"%(lvs)
print s2

i=1
n=0
while i<(len(checkarray)-1):
	c1=abccheck(checkarray[i-1],checkarray[i],checkarray[i+1],calleaves,2004)
	c2=isleave(checkarray[i],calleaves,2004,1)
	if c1==False and  c2==True:
		n=n+1
		if (checkarray[i][3]==0):
			b=sixdaylogic(checkarray[i],calleaves,2004,6,6,0)
		else:
			b=""
		print "Violation#%d at %d/%d/%d \t %s"%(n,checkarray[i][0],checkarray[i][1],checkarray[i][2],whatholiday(checkarray[i],calleaves,2004,1)),b
	i=i+1

#print noofdays([2004,1,1],[2003,12,1])
#print isleave([2013,11,9],calleaves,2004,1),"\t",isleave([2013,11,9],calleaves,2004,0)
#print whatholiday ([2013,4,1],calleaves,2004,0)
#notes for development
# Add checks: CHECK IF A LEAVE DATE EXISTS EG.. 29FEB IN A NON LEAP YEAR IE CHECK DATE VALIDITY
# Modify printcalcmdline function to print holiday
# Modify printcalcmdline function to print calendar to file
#Need to explain any leave errors and violations.
#add daddys logic
#Since the Rules apply in so many different ways, generate a report ... will require a lot of work
a=checkleave3(calleaves,mainleaves)
i=0
count=0
while i<len(a):
	if mainleaves[i][2]==2:
		i=i+1
		continue
	prefix=a[i][0]
	suffix=a[i][1]
	if len(prefix)!=0 or len(suffix)!=0:
		print "Leave#",(i+1)
		count=count+1
		print mainleaves[i]
	if len(prefix)!=0:
		print "Prefixes:",prefix
	if len(suffix)!=0:
		print "Suffixes:",suffix
	i=i+1
print count
