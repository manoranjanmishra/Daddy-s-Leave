#enter leave data in leave.txt
#Entry Structure: Start-Date,End-Date,Type,Description,Duration
#Dates are / separated, items are comma separated
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
	#returns True if date comes on or before a:WORKING
	comp=ascsort(date,a)
	if comp==[date,a]:
		return True
	else:
		return False
def readdate(date):
	#reads date and numbers from a string:WORKING
	i=0
	dout=[]
	val=""
	while i<len(date):
		if (date[i]=="/") or (date[i]==".") or (date[i]=="-") or (i+1 == len(date)):
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
def filetoarray(entry):
	#converts entry from file into a form that can be used to search, sort and enter information:WORKING
	entrya=[]
	i=0
	item=""
	ic=0
	while i<len(entry):
		if (entry[i]==",") or (i+1==len(entry)):
			if (i+1==len(entry)):
				item=item+entry[i]
			if (len(item)!=0):
				if (ic!=3):
					proper=readdate(item)
				else:
					proper=item
			entrya=entrya+[proper]
			item=""
			ic=ic+1
		else:
			item=item+entry[i]
		i=i+1
	return entrya
def arraytofile(entry):
	#converts entry from array into a string that can be written back to the file
	i=0
	entrys=""
	while i<len(entry):
		item=entry[i]
		if (i==0) or (i==1):
			s="%d/%d/%d"%(item[0],item[1],item[2])
		elif (i==2) or (i==4):
			s="%d"%item
		else:
			s=item
		entrys=entrys+","+s
		i=i+1
	return entrys

#1: Open file in readonly mode, and read all data to array. Close file
file=open("leave.txt",'r')
filebackup=open("leave_backup.txt","w+")
filea=[]
for entry in file:
	filebackup.write(entry)
	filea=filea+[filetoarray(entry)]
filebackup.close()
file.close()
#2: Enter data, make changes
change=True
adds=0
changes=0
more=True
while more==True:
	entry=[]
	i=0
	while i<5:
		if (i==0):
			inp=readdate(raw_input("YYYY/MM/DD: "))
		elif (i==1):
			inp=entry[0]
		elif (i==2):
			inp=0
		elif (i==3):
			inp=raw_input("Desc:")
		elif (i==4):
			inp=1
		entry=entry+[inp]
		i=i+1
	a=ascsort(entry[0],entry[1])[0]
	b=ascsort(entry[0],entry[1])[1]
	entry[0]=a
	entry[1]=b
	if len(filea)==0:
		filea=filea+[entry]
	else:
		i=0
		while i<len(filea):
			if not(comesafter(entry[0],filea[i][0])):
				break
			i=i+1
		filea=filea[:i]+[entry]+filea[i:]
	adds=adds+1
	if raw_input("Enter more data Y/N")!="Y":
		more=False
if (adds!=0) or (changes!=0):
	change=True
else:
	change=False
if (adds==0):
	adds="None"
else:
	adds="%d"%adds
if (changes==0):
	changes="None"
else:
	changes="%d"%changes
#3: If there are any changes, open file in write mode, and write array to file
if (change==True):
	file2=open("leave.txt","w+")
	i=0
	while i<len(filea):
		s=arraytofile(filea[i])
		data=s+"\n"
		file2.write(data[1:])
		i=i+1
	file2.close()
	print "%s added, %s changed, %d entries saved."%(adds,changes,len(filea))
else:
	print "No changes"
