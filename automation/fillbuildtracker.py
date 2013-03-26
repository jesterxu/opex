#!/usr/bin/env python
#coding=utf-8
import xlrd,time, re
import sys,os

def fillrelease(product, filename,mediatype): 
	
	basedir='/home/jester/Documents/OPEX/FillBuildTracker/'
	
	# Use this list to solve the different language input issue.
	PL_cbl={
			'British English':'British English',
			'CSY':'Czech',
			'Dutch':'Dutch',
			'ENU':'English',
			'FRA':'French',
			'DEU':'German',
			'HUN':'Hungarian',
			'ITA':'Italian',
			'JPN':'Japanese',
			'KOR':'Korean',
			'Nordic':'Nordic',
			'PLK':'Polish',
			'PTB':'Portuguese',
			'RUS':'Russian',
			'CHS':'Simplified Chinese',
			'ESP':'Spanish',
			'CHT':'Traditional Chinese',
			'Vietnamese':'Vietnamese',
			#will use the full name
			'Czech':'Czech',
			'English':'English',
			'French':'French',
			'German':'German',
			'Hungarian':'Hungarian',
			'Italian':'Italian',
			'Japanese':'Japanese',
			'Japanese Kanji':'Japanese',
			'Korean':'Korean',
			'Polish':'Polish',
			'Portuguese':'Portuguese',
			'Portuguese Brazil':'Portuguese',
			'Russian':'Russian',
			'Simplified Chinese':'Simplified Chinese',
			'Spanish':'Spanish',
			'European Spanish':'Spanish',
			'Tranditional Chinese':'Traditional Chinese',
			}
	
	# get all values from current input txt file.
	allvalues=getallvalues(filename)
	
	#Open the execel files and select the right table
	excelfile=xlrd.open_workbook(basedir+'GBS_Scores_2014_Release_Template_'+product+'.xls')
	
	#handled according different mediatypes.
	if mediatype=='ISO':
		isheet=excelfile.sheet_by_name("Physical_Media")
		fillISO(isheet,allvalues,PL_cbl)
	elif mediatype=='USB':
		isheet=excelfile.sheet_by_name("USB_Media")
		fillUSB(isheet,allvalues,PL_cbl)
	elif mediatype=='DLM':
		isheet=excelfile.sheet_by_name("Download_Now")
		fillDLM(isheet,allvalues,PL_cbl)
	elif mediatype=='WI':
		isheet=excelfile.sheet_by_name("Install_Now")
		fillWI(isheet,allvalues,PL_cbl)
	elif mediatype=='LP':
		isheet=excelfile.sheet_by_name("Browser_Download")
		fillLP(isheet,allvalues,PL_cbl)
	else:
		print 'The media type you input cant be recongized.Please make sure you input the right type!'
	excelfile.save()

 
#fill the ISO table.
def fillISO(isheet,allvalues,PL_cbl):
	irow=1
	#get the row number according the language
	ctype=1  #0 empty, 1 string, 2 number,3 date, 4 boolean, 5 error
	xf=0 #extend format.
	for i in range(0,isheet.nrows):
		if isheet.cell_value(i,1).strip()=='':
			isheet.put_cell(i,1,ctype,allvalues['Division'],xf) # fill the Division.
			isheet.put_cell(i,2,ctype,allvalues['NPI'],xf) # fill the NPI manager.
			isheet.put_cell(i,3,ctype,allvalues['COO'],xf)# file the country of origin.
			isheet.put_cell(i,4,ctype,allvalues['SAPD'],xf) # fill the SAP description.
			print isheet.cell_value(i,4)
			isheet.put_cell(i,5,ctype,allvalues['PN'],xf) # fill the part number.
			isheet.put_cell(i,6,ctype,PL_cbl[allvalues['PL']],xf) # fill the product language.
			if allvalues['OS'].find("32")!=-1 and allvalues['OS'].find("64")!=-1:  #fill the os.
				isheet.put_cell(i,7,ctype,'Windows 32Bit; Windows 64Bit',xf)
			elif allvalues['OS'].find("64")!=-1:
				isheet.put_cell(i,7,ctype,'Windows 64Bit',xf)
			else:
				isheet.put_cell(i,7,ctype,'Windows 32Bit',xf)

			isheet.put_cell(i,8,ctype,allvalues['PNA'],xf)# fill the product name.
			isheet.put_cell(i,9,ctype,allvalues['FN'],xf) # fill the file name.
			isheet.put_cell(i,10,ctype,allvalues['MD5'],xf)# fill the MD5 checksum
			isheet.put_cell(i,11,ctype,allvalues['FS'],xf) # fill the file size.
			isheet.put_cell(i,12,ctype,allvalues['NP'],xf)# fill the network path.
			isheet.put_cell(i,13,ctype,"ISO9660/Joliet",xf) #fill the SoftWare file system
			isheet.put_cell(i,14,ctype,allvalues['IVN'],xf) # fill the build number.
			if allvalues['UPI32']!='None':
				isheet.put_cell(i,15,ctype,allvalues['UPI32'],xf) #fill the upi 32bits.
				isheet.put_cell(i,16,ctype,allvalues['UPI64'],xf) # fill the upi 64bits.

			isheet.put_cell(i,18,ctype,allvalues['QASOD'],xf) # select the Division.
			isheet.put_cell(i,19,ctype,allvalues['FBPOS'],xf) # select the Division.
			
			
			break

	print 'fill ISO finished.!'

#fill the USB table.
def fillUSB(sel,allvalues,imediakey):

	print 'fill USB finished.!'

#fill the DLM table.
def fillDLM(sel,allvalues,imediakey):
	print 'fill DLM finished.!'

#fill the WI table.
def fillWI(sel,allvalues,imediakey):
	print 'fill the WI finished.!'

#fill the LP table.
def fillLP(sel,allvalues,imediakey):
	print 'fill the LP finished.!'
	
#Get the all the values from txt input.
def getallvalues(filename):
	# open the file and readlines.
	fileobj=open(filename)
	fileobj.seek(0)
	filelines=fileobj.readlines()
	fileobj.close()

	allvalues={
			'MGRS':findvalue(filelines,'Market Group Release Status'),
			'Division':findvalue(filelines,'Division'),
			'NPI':findvalue(filelines,'NPI Manager'),
			'COO':findvalue(filelines,'Country Of Origin'),
			'PL':findvalue(filelines,'Product Language'),
			'IVN':findvalue(filelines,'Internal Version Number'),
			'PK':findvalue(filelines,'Product Key'),
			'NOAF':findvalue(filelines,'Number of Associated Files'),
			'NP':findvalue(filelines,'Network Path'),
			'FN':findvalue(filelines,'File Name'),
			'PN':findvalue(filelines,'Part Number'),
			'FS':findvalue(filelines,'File Size'),
			'UFS':findvalue(filelines,'Unpacked File Size'),
			'MT':findvalue(filelines,'Media Type'),
			'MID':findvalue(filelines,'MID'),
			'OS':findvalue(filelines,'Operating System'),
			'MD5':findvalue(filelines,'MD5 Checksum'),
			'SAPD':findvalue(filelines,'SAP Description'),
			'RPV':findvalue(filelines,'Root Product Version'),
			'URLR':findvalue(filelines,'URLRoot'),
			'DTPL':findvalue(filelines,'Download TEST Page Link'),
			'PNA':findvalue(filelines,'Product Name'),
			'INL':findvalue(filelines,'Internal link'),
			'EXL':findvalue(filelines,'External link'),
			'IFN':findvalue(filelines,'Inventory File Name'),
			'UPI32':findvalue(filelines,'Product Line Code (SAP)'),
			'UPI64':findvalue(filelines,'Product Line Code (SAP)'),
			'QASOD':findvalue(filelines,'QA Sing-off Date'),
			'FBPOS':findvalue(filelines,'Full Build Path On Storebox')
			}
	return allvalues

# Return value from the line list. 
def findvalue(linelist, keyvalue, spliter=':'):
	keyvalue=keyvalue.lower()
	for line in linelist:
		if line.lower().find(keyvalue)!=-1:
			if keyvalue.find("file size")!=-1:
				return line.replace(line.split(spliter)[0]+':','').split("bytes")[0].strip()
			else:
				return line.replace(line.split(spliter)[0]+':','').strip()
            
if __name__=='__main__':
	fillrelease(sys.argv[1], sys.argv[2],sys.argv[3])






