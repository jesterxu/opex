#!/usr/bin/env python
#coding=utf-8
import xlrd
import codecs
import sys,os,shutil

#this is the main function to start.

def generatemedia(product, language, mediatype):
	#open the excel file as the user's input value.
	rootdir="/home/jester/Documents/OPEX/GenerateMedia/"
	basedir="/home/jester/Documents/OPEX/GenerateMedia/builddata/"
	targetdir=rootdir+"builddata_"+product+"_"+language+"_"+mediatype+"/"

	if not os.path.exists(targetdir):
		os.mkdir(targetdir)
	#print rootdir+product+".xlsx"
	excelfile=xlrd.open_workbook(rootdir+product+".xls")
	isheetcommon=excelfile.sheet_by_name("COMMON")
	isheetdlm=excelfile.sheet_by_name("DLM")
	isheetwi=excelfile.sheet_by_name("WI")
	isheetimg=excelfile.sheet_by_name("IMG")
	isheetiso=excelfile.sheet_by_name("ISO")

	shutil.rmtree(targetdir)
	shutil.copytree(basedir,targetdir)
	

	#this part handle the COMMON mediatype
	if mediatype=="COMMON":
		updatecommon(targetdir,isheetcommon,language)
	elif mediatype=="DLM":
		updatedlm(targetdir,isheetdlm,language)
	elif mediatype=="WI":
		updatewi(targetdir,isheetwi,language)
	elif mediatype=="IMG":
		updateimg(targetdir,isheetimg,language)
	elif mediatype=="ISO":
		updateiso(targetdir,isheetiso,language)
	elif mediatype=="ALL":
		updatecommon(targetdir,isheetcommon,language)
		updatedlm(targetdir,isheetdlm,language)
		updatewi(targetdir,isheetwi,language)
		updateimg(targetdir,isheetimg,language)
		updateiso(targetdir,isheetiso,language)
	else:
		print "The intput format or somthing wrong, please recheck before continue!"

	
# update the common type
def updatecommon(targetdir,isheet,language):

	irow=1
	#get the row number according the language
	for i in range(0,isheet.nrows):
		if isheet.cell_value(i,0)==language:
			irow=i
			break

	#get the list from "manifest.txt"
	MFfile=open(targetdir+"manifest.txt")
	MFlist=MFfile.readlines()
	MFfile.close()
	
	#Update the values.
	MFlist=replacevalue(MFlist,"platform=",isheet.cell_value(irow,1),"[COMMON]")
	MFlist=replacevalue(MFlist,"version=",isheet.cell_value(irow,2),"[COMMON]")
	MFlist=replacevalue(MFlist,"productname=",isheet.cell_value(irow,3),"[COMMON]")

	writelisttofile(MFlist,targetdir+"manifest.txt")

	print "COMMON created"

#update the dlm type
def updatedlm(targetdir,isheet,language):
	irow=1
	#get the row number according the language
	for i in range(0,isheet.nrows):
		if isheet.cell_value(i,0)==language:
			irow=i
			break

	# this part update the "manifest.txt" file
	MFfile=open(targetdir+"manifest.txt")
	MFlist=MFfile.readlines()
	MFfile.close()
		
	#Update the values.
	MFlist=replacevalue(MFlist,"type=",isheet.cell_value(irow,1),"[DLM]")
	MFlist=replacevalue(MFlist,"outputname=",isheet.cell_value(irow,2),"[DLM]")
	MFlist=replacevalue(MFlist,"mid=",isheet.cell_value(irow,3),"[DLM]")
	MFlist=replacevalue(MFlist,"partnumber=",isheet.cell_value(irow,4),"[DLM]")

	writelisttofile(MFlist,targetdir+"manifest.txt")

	#this part update the "dlm.ini" file
	MFfile=open(targetdir+"dlm.ini")
	MFlist=MFfile.readlines()
	MFfile.close()
		
	#Update the values.
	MFlist=replacevalue(MFlist,"EXE_PATH=",isheet.cell_value(irow,10),"[DLM_LAUNCH]")

	writelisttofile(MFlist,targetdir+"dlm.ini")

	#this part will handle the "dlm.media.xml"
	MFfile=codecs.open(targetdir+"dlm.media.xml",encoding="utf-16")
	MFlist=MFfile.readlines()
	MFfile.close()

	MFlist=replacevalue(MFlist,"<name>",isheet.cell_value(irow,5),"<product>")
	MFlist=replacevalue(MFlist,"<version>",isheet.cell_value(irow,6),"<product>")
	MFlist=replacevalue(MFlist,"<urlroot>",isheet.cell_value(irow,7),"<product>")
	MFlist=replacevalue(MFlist,"<name>",isheet.cell_value(irow,8),"<media>")
	MFlist=replacevalue(MFlist,"<language>",isheet.cell_value(irow,9),"<media>")
	MFlist=replacevalue(MFlist,"<part partnumber=\"",isheet.cell_value(irow,11),"<media>")
	#MFlist=replacevalue(MFlist,"",isheet.cell_value(irow,4),"")
	#MFlist=replacevalue(MFlist,"",isheet.cell_value(irow,4),"")
		

	writelisttofile(MFlist,targetdir+"dlm.media.xml")



	print "DLM created"

#update the WI type
def updatewi(targetdir,isheet,language):
	irow=1
	#get the row number according the language
	for i in range(0,isheet.nrows):
		if isheet.cell_value(i,0)==language:
			irow=i
			break

	# this part update the "manifest.txt"
	MFfile=open(targetdir+"manifest.txt")
	MFlist=MFfile.readlines()
	MFfile.close()
		
	#Update the values.
	MFlist=replacevalue(MFlist,"mid=",isheet.cell_value(irow,7),"[WI]")
	MFlist=replacevalue(MFlist,"partnumber=",isheet.cell_value(irow,6),"[WI]")

	writelisttofile(MFlist,targetdir+"manifest.txt")


	#this part update the "wi.media.xml"
	MFfile=codecs.open(targetdir+"wi.media.xml",encoding='utf-16')
	MFlist=MFfile.readlines()
	MFfile.close()
		
	#Update the values.
	#print isheet.cell_value(irow,1)
	MFlist=replacevalue(MFlist,"<name>",isheet.cell_value(irow,1),"<product>")
	MFlist=replacevalue(MFlist,"<version>",isheet.cell_value(irow,2),"<product>")
	MFlist=replacevalue(MFlist,"<urlroot>",isheet.cell_value(irow,3),"<product>")
	MFlist=replacevalue(MFlist,"<name>",isheet.cell_value(irow,4),"<media>")
	MFlist=replacevalue(MFlist,"<platform>",isheet.cell_value(irow,5),"<media>")
	MFlist=replacevalue(MFlist,"<part partnumber=\"",isheet.cell_value(irow,6),"<media>")

	writelisttofile(MFlist,targetdir+"wi.media.xml")

	print "WI created"

#update img type:
def updateimg(targetdir,isheet,language):
	irow=1
	#get the row number according the language
	for i in range(0,isheet.nrows):
		if isheet.cell_value(i,0)==language:
			irow=i
			break

	#get the list from "manifest.txt"
	MFfile=open(targetdir+"manifest.txt")
	MFlist=MFfile.readlines()
	MFfile.close()
		
	#Update the values.
	MFlist=replacevalue(MFlist,"imgsize=",isheet.cell_value(irow,1),"[IMG]")
	MFlist=replacevalue(MFlist,"compact=",isheet.cell_value(irow,2),"[IMG]")
	MFlist=replacevalue(MFlist,"outputname=",isheet.cell_value(irow,3),"[IMG]")
	MFlist=replacevalue(MFlist,"volumename=",isheet.cell_value(irow,4),"[IMG]")
	MFlist=replacevalue(MFlist,"mid=",isheet.cell_value(irow,5),"[IMG]")
	MFlist=replacevalue(MFlist,"partnumber=",isheet.cell_value(irow,6),"[IMG]")

	writelisttofile(MFlist,targetdir+"manifest.txt")
	print "IMG created"

#update the ISO type
def updateiso(targetdir,isheet,language):
	irow=1
	#get the row number according the language
	for i in range(0,isheet.nrows):
		if isheet.cell_value(i,0)==language:
			irow=i
			break

	#get the list from "manifest.txt"
	MFfile=open(targetdir+"manifest.txt")
	MFlist=MFfile.readlines()
	MFfile.close()
		
	#Update the values.
	try:
		float(isheet.cell_value(irow,1))
		value1=str(int(isheet.cell_value(irow,1)))
	except:
		value1=isheet.cell_value(irow,1)

	try:
		float(isheet.cell_value(irow,2))
		value2=str(int(isheet.cell_value(irow,2)))
	except:
		value2=isheet.cell_value(irow,2)

	try:
		float(isheet.cell_value(irow,3))
		value3=str(int(isheet.cell_value(irow,3)))
	except:
		value3=isheet.cell_value(irow,3)
	#ivalue=str(isheet.cell_value(irow,1))+","+str(isheet.cell_value(irow,2))+","+str(isheet.cell_value(irow,3))
	MFlist=replacevalue(MFlist,"iso1=",value1+","+value2+','+value3,"[ISO]")
	MFlist=replacevalue(MFlist,"mid=",isheet.cell_value(irow,4),"[ISO]")

	writelisttofile(MFlist,targetdir+"manifest.txt")

	print "ISO finished"





# Repalce the value from the line list and then return the updated linelist. 
def replacevalue(linelist, keyvalue, replacevalue,prekey):
	if prekey=='':
		prefound=True
	else:
		prefound=False
	
	#the variable K used to fill the dlm partnumber.
	k=0

	for i in range(0,len(linelist)):
		if linelist[i].find(prekey)!=-1:
			prefound=True
			continue 
		if (linelist[i].find("[")!=-1 or linelist[i].find("<product>")!=-1 or linelist[i].find("<media>")!=-1)and prefound:
			break
		else:
			if linelist[i].find(keyvalue)!=-1 and prefound:
				try:
					float(replacevalue)
					replacevalue=str(int(replacevalue))
				except:
					#this a string
					iak=1


				#this part added for dlm.media.xml update.
				if prekey=="<media>" and keyvalue=="<name>":
					if linelist[i+1].find("<platform>")!=-1 and linelist[i-1].find("wi")==-1:
						if linelist[i+1].find("x64")!=-1:
							replacevalue=replacevalue.replace("_32bit_","_64bit_")
							replacevalue=replacevalue.replace("_32-64bit_","_64bit_")
						elif linelist[i+1].find("x86")!=-1:
							replacevalue=replacevalue.replace("_64bit_","_32bit_")
							replacevalue=replacevalue.replace("_32-64bit_","_32bit_")
						elif linelist[i+1].find("all")!=-1:
							replacevalue=replacevalue.replace("_32bit_","_32-64bit_")
							replacevalue=replacevalue.replace("_64bit_","_32-64bit_")

				#handle the xml update speical case
				if keyvalue.find("<")!=-1 and keyvalue.find(">")!=-1:
					ireplacevalue=replacevalue+keyvalue.replace("<","</")
				elif keyvalue=="<part partnumber=\"":
					if len(replacevalue.split(":"))>1:
						ireplacevalue=replacevalue.split(":")[k]+"\" sequence=\"0\">"
						k=k+1
					else:
						ireplacevalue=replacevalue+"\" sequence=\"0\">"
				else:
					ireplacevalue=replacevalue


				linelist[i]=linelist[i].replace(linelist[i].split(keyvalue)[1].strip(),ireplacevalue)
				#print linelist[i]
				#prefound=False
	
	return linelist



# write the list to the target file.
def writelisttofile(linelist, filename):
	if filename.find(".xml")!=-1:
		targetfile=codecs.open(filename,mode="w",encoding="utf_16")
	else:
		targetfile=open(filename,"w")
	targetfile.writelines(linelist)
	targetfile.close()

if __name__=="__main__":
	generatemedia(sys.argv[1], sys.argv[2], sys.argv[3])
