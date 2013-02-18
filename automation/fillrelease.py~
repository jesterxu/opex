#!/usr/bin/env python
#coding=utf-8
from selenium import selenium
import unittest, time, re
import sys

def fillrelease(ip, filename, sap):
    
        fileobj=open(filename)
        fileobj.seek(0)
        filelines=fileobj.readlines()
        fileobj.close()
        
        fileobj=open(sap)
        fileobj.seek(0)
        saplines=fileobj.readlines()
        fileobj.close()
        if findvalue(filelines, "Language:")!=None:
            ilanguage=findvalue(filelines, "Language:").split("(")[0].strip()
        releasetype=findvalue(filelines, "Media Type:")
        country="United States"
        osinfo=findvalue(filelines, "OS information:")
        
        if osinfo==None:
            osinfo="Win 64 86"
        
        iselenium=selenium(ip,4444,"*iexplore","http://share.autodesk.com")
        iselenium.start()
        sel=iselenium
        sel.set_timeout("10000")
        sel.open("/sites/GBS_GRE/_layouts/FormServer.aspx?XsnLocation=https://share.autodesk.com/sites/GBS_GRE/GRSDBA/Forms/template.xsn&SaveLocation=https%3A%2F%2Fshare%2Eautodesk%2Ecom%2Fsites%2FGBS%5FGRE%2FGRSDBA&ClientInstalled=true&Source=https%3A%2F%2Fshare%2Eautodesk%2Ecom%2Fsites%2FGBS%5FGRE%2FGRSDBA%2FForms%2FAllItems%2Easpx&DefaultItemOpen=1")
        sel.wait_for_page_to_load("30000")
        sel.window_maximize()
        
        sel.select("id=FormControl_V1_I1_S2_I1_D1", "index=0")  #Market Group
        sel.select("id=FormControl_V1_I1_S2_I1_D1", "index=1")
        sel.select("id=FormControl_V1_I1_S2_I1_D2", "index=0")  # Division
        sel.select("id=FormControl_V1_I1_S2_I1_D2", "index=7")  
        sel.select("id=FormControl_V1_I1_S2_I1_D3", "index=0")  #NPI Manager
        sel.select("id=FormControl_V1_I1_S2_I1_D3", "index=6")
        

        if releasetype=="DVD" or releasetype=="DVD9":
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=0")  #Type of Release
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=1")
            sel.select("id=FormControl_V1_I1_S3_I3_D6", "index=0")  # Software File System
            #sel.select("id=FormControl_V1_I1_S3_I3_D6", "index=0")  
            sel.select("id=FormControl_V1_I1_S3_I3_D7", "index=0")  #Network Path
            sel.select("id=FormControl_V1_I1_S3_I3_D7", "index=1")  
            sel.click("id=FormControl_V1_I1_S3_I3_C10") # UPI Required
            while not sel.is_element_present("id=FormControl_V1_I1_S3_I3_S11_I5_T1"):
                print "wait!"
            
            
            #Product Language
            if ilanguage!=None:
                if ilanguage=="British English" or ilanguage=="Czech" or ilanguage=="Dutch" or ilanguage=="European English" or ilanguage=="German":
                    sel.click("//input[@value='"+ilanguage+"']") 
                else:
                    sel.click("//input[@value='"+ilanguage+" ']") 

            if osinfo.find("Win")!=-1 and osinfo.find("64")!=-1 and osinfo.find("86")!=-1:
                sel.click("//input[@value='WIN 32']") # Operating System
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!" 
                sel.click("//input[@value='WIN 64']")    
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!" 
            elif osinfo.find("Win")!=-1 and osinfo.find("86")!=-1:
                sel.check("//input[@value='WIN 32']") # Operating System
            elif osinfo.find("Win")!=-1 and osinfo.find("64")!=-1:
                sel.check("//input[@value='WIN 64']")  

            sel.itype("id=FormControl_V1_I1_S2_I1_T5", findvalues(saplines, findvalue(filelines, "Part Number:"))) #SAP description
            sel.itype("id=FormControl_V1_I1_S2_I1_T6", findvalue(filelines, "Part Number:")) #Part Number
            
            if releasetype=="DVD":
                sel.select("id=FormControl_V1_I1_S3_I3_D1", "index=0")  #Pyysical Media Type
                sel.select("id=FormControl_V1_I1_S3_I3_D1", "index=1")  
            else:
                sel.select("id=FormControl_V1_I1_S3_I3_D1", "index=0")  #Pyysical Media Type
            sel.itype("id=FormControl_V1_I1_S3_I3_T2", findvalue(filelines, "File Name:")) # File Name
            sel.itype("id=FormControl_V1_I1_S3_I3_T3", findvalue(filelines, "File Size:").replace("bytes","")) # File size
            sel.itype("id=FormControl_V1_I1_S3_I3_T4", findvalue(filelines, "MD5 Checksum:")) # MD5 checksum



            if findvalue(filelines, "Internal Version Number:")!=None:
                sel.itype("id=FormControl_V1_I1_S3_I3_T8", findvalue(filelines, "Internal Version Number:").split("_")[0]) # Internal Version Number(Build Number):
            sel.itype("id=FormControl_V1_I1_S3_I3_T9", country) #Country of Origin
            
            sel.itype("id=FormControl_V1_I1_S3_I3_S11_I5_T1", findvalue(filelines, "Product Line Code (SAP):")) #Product Line Code (SAP):
            sel.itype("id=FormControl_V1_I1_S3_I3_S11_I5_T2", findvalue(filelines, "Product Line Code (SAP):")) #Product Line Code (SAP):


        elif releasetype=="WI":
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=0")  #Type of Release
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=4")
            sel.select("id=FormControl_V1_I1_S6_I9_D1", "index=0")  #Distribution Package Type
            sel.select("id=FormControl_V1_I1_S6_I9_D1", "index=6")
            sel.select("id=FormControl_V1_I1_S6_I9_D10", "index=0")  #Network Path
            sel.select("id=FormControl_V1_I1_S6_I9_D10", "index=1")  
            sel.click("id=FormControl_V1_I1_S6_I9_C13") # UPI Required
            while not sel.is_element_present("id=FormControl_V1_I1_S6_I9_S14_I5_T1"):
                print "wait!"
                
            #Product Language
            if ilanguage!=None:
                if ilanguage=="British English" or ilanguage=="Czech" or ilanguage=="Dutch" or ilanguage=="European English" or ilanguage=="German":
                    sel.click("//input[@value='"+ilanguage+"']") 
                else:
                    sel.click("//input[@value='"+ilanguage+" ']") 

            if osinfo.find("Win")!=-1 and osinfo.find("64")!=-1 and osinfo.find("86")!=-1:
                sel.click("//input[@value='Win32Bit']") # Operating System
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!"
                sel.click("//input[@value='Win64Bit']")   
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!" 
            elif osinfo.find("Win")!=-1 and osinfo.find("86")!=-1:
                sel.click("//input[@value='Win32Bit']") # Operating System
            elif osinfo.find("Win")!=-1 and osinfo.find("64")!=-1:
                sel.click("//input[@value='Win64Bit']")  


            sel.itype("id=FormControl_V1_I1_S2_I1_T5",  findvalues(saplines, findvalue(filelines, "Part Number:"))) #SAP description
            sel.itype("id=FormControl_V1_I1_S2_I1_T6", findvalue(filelines, "Part Number:")) #Part Number
            
            sel.itype("id=FormControl_V1_I1_S6_I9_T2", findvalue(filelines, "Root Product Version:")) # Root Product Version
            #sel.itype("id=FormControl_V1_I1_S6_I9_S5_I13_T1", findvalue(filelines, "File Name:")) # File Name
            sel.itype("id=FormControl_V1_I1_S6_I9_S5_I13_T2", findvalue(filelines, "File Size:").replace("bytes","")) # File Size
            sel.itype("id=FormControl_V1_I1_S6_I9_T6", findvalue(filelines, "Unpacked File Size:").replace("bytes","")) # Unpacked File Size
            sel.itype("id=FormControl_V1_I1_S6_I9_T7", findvalues(saplines, findvalue(filelines, "Part Number:"),2)) # End User Download Link
            
            
            sel.itype("id=FormControl_V1_I1_S6_I9_S9_I14_T1", findvalue(filelines, "MD5 Checksum:")) #MD5 Checksum
            sel.itype("id=FormControl_V1_I1_S6_I9_T11", country) #Country of Origin  
            if findvalue(filelines, "Internal Version Number:")!=None:
                sel.itype("id=FormControl_V1_I1_S6_I9_T12", findvalue(filelines, "Internal Version Number:").split("_")[0]) # Internal Version Number(Build Number):
        
            
            sel.itype("id=FormControl_V1_I1_S6_I9_S14_I5_T1", findvalue(filelines, "Product Line Code (SAP):")) #Product Line Code (SAP):
            sel.itype("id=FormControl_V1_I1_S6_I9_S14_I5_T2", findvalue(filelines, "Product Line Code (SAP):")) #Product Line Code (SAP):
            sel.itype("id=FormControl_V1_I1_S6_I9_S15_I15_T7", findvalue(filelines, "Link to Download Test Page:")) #Product Line Code (SAP):
            sel.click("id=FormControl_V1_I1_S6_I9_S15_I15_C8") # File Approved
            sel.itype("id=FormControl_V1_I1_S6_I9_S5_I13_T1", findvalue(filelines, "File Name:")) # File Name
        elif releasetype=="DLM":
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=0")  #Type of Release
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=4")
            sel.select("id=FormControl_V1_I1_S6_I9_D1", "index=0")  #Distribution Package Type
            sel.select("id=FormControl_V1_I1_S6_I9_D1", "index=2")
            sel.select("id=FormControl_V1_I1_S6_I9_D10", "index=0")  #Network Path
            sel.select("id=FormControl_V1_I1_S6_I9_D10", "index=1")  
            sel.click("id=FormControl_V1_I1_S6_I9_C13") # UPI Required
            while not sel.is_element_present("id=FormControl_V1_I1_S6_I9_S14_I5_T1"):
                print "wait!"
                
            #Product Language
            if ilanguage!=None:
                if ilanguage=="British English" or ilanguage=="Czech" or ilanguage=="Dutch" or ilanguage=="European English" or ilanguage=="German":
                    sel.click("//input[@value='"+ilanguage+"']") 
                else:
                    sel.click("//input[@value='"+ilanguage+" ']") 
                    
            if osinfo.find("Win")!=-1 and osinfo.find("64")!=-1 and osinfo.find("86")!=-1:
                sel.click("//input[@value='Win32Bit']") # Operating System
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!"
                sel.click("//input[@value='Win64Bit']")   
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!" 
            elif osinfo.find("Win")!=-1 and osinfo.find("86")!=-1:
                sel.click("//input[@value='Win32Bit']") # Operating System
            elif osinfo.find("Win")!=-1 and osinfo.find("64")!=-1:
                sel.click("//input[@value='Win64Bit']")    
                    
            sel.itype("id=FormControl_V1_I1_S2_I1_T5",  findvalues(saplines, findvalue(filelines, "Part Number:"))) #SAP description
            sel.itype("id=FormControl_V1_I1_S2_I1_T6", findvalue(filelines, "Part Number:")) #Part Number
            
            sel.itype("id=FormControl_V1_I1_S6_I9_T2", findvalue(filelines, "Root Product Version:")) # Root Product Version
            sel.itype("id=FormControl_V1_I1_S6_I9_S3_I10_T1", findvalue(filelines, "Number of Associated Files:")) #Number of Associated Files
            #sel.itype("id=FormControl_V1_I1_S6_I9_S3_I10_R2_I11_T1", findvalue(filelines, "File Name:")) # File Name
            sel.itype("id=FormControl_V1_I1_S6_I9_S3_I10_R2_I11_T2", findvalue(filelines, "File Size:").replace("bytes","")) # File Size
            sel.itype("id=FormControl_V1_I1_S6_I9_S3_I10_R2_I11_T3", findvalue(filelines, "MD5 Checksum:")) # MD5 Checksum:
            sel.itype("id=FormControl_V1_I1_S6_I9_T6", findvalue(filelines, "Unpacked File Size:").replace("bytes","")) # Unpacked File Size
            sel.itype("id=FormControl_V1_I1_S6_I9_T7",findvalues(saplines, findvalue(filelines, "Part Number:"),2)) # End User Download Link
            sel.itype("id=FormControl_V1_I1_S6_I9_T11", country) #Country of Origin  
            if findvalue(filelines, "Internal Version Number:")!=None:
                sel.itype("id=FormControl_V1_I1_S6_I9_T12", findvalue(filelines, "Internal Version Number:").split("_")[0]) # Internal Version Number(Build Number):
        
            
            sel.itype("id=FormControl_V1_I1_S6_I9_S14_I5_T1", findvalue(filelines, "Product Line Code (SAP):")) #Product Line Code (SAP):
            sel.itype("id=FormControl_V1_I1_S6_I9_S14_I5_T2", findvalue(filelines, "Product Line Code (SAP):")) #Product Line Code (SAP):
            sel.itype("id=FormControl_V1_I1_S6_I9_S15_I15_T7", findvalue(filelines, "Link to Download Test Page:")) #Product Line Code (SAP):
            sel.click("id=FormControl_V1_I1_S6_I9_S15_I15_C8") # File Approved
            sel.itype("id=FormControl_V1_I1_S6_I9_S3_I10_R2_I11_T1", findvalue(filelines, "File Name:")) # File Name
        elif releasetype=="ESD":
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=0")  #Type of Release
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=4")
            sel.select("id=FormControl_V1_I1_S6_I9_D1", "index=0")  #Distribution Package Type
            sel.select("id=FormControl_V1_I1_S6_I9_D1", "index=1")
            sel.select("id=FormControl_V1_I1_S6_I9_D10", "index=0")  #Network Path
            sel.select("id=FormControl_V1_I1_S6_I9_D10", "index=3")  
            sel.click("id=FormControl_V1_I1_S6_I9_C13") # UPI Required
            while not sel.is_element_present("id=FormControl_V1_I1_S6_I9_S14_I5_T1"):
                print "wait!"
            #Product Language
            if ilanguage!=None:
                if ilanguage=="British English" or ilanguage=="Czech" or ilanguage=="Dutch" or ilanguage=="European English" or ilanguage=="German":
                    sel.click("//input[@value='"+ilanguage+"']") 
                else:
                    sel.click("//input[@value='"+ilanguage+" ']") 

            if osinfo.find("Win")!=-1 and osinfo.find("64")!=-1 and osinfo.find("86")!=-1:
                sel.click("//input[@value='Win32Bit']") # Operating System
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!"
                sel.click("//input[@value='Win64Bit']")   
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!" 
            elif osinfo.find("Win")!=-1 and osinfo.find("86")!=-1:
                sel.click("//input[@value='Win32Bit']") # Operating System
            elif osinfo.find("Win")!=-1 and osinfo.find("64")!=-1:
                sel.click("//input[@value='Win64Bit']")  

            sel.itype("id=FormControl_V1_I1_S2_I1_T5", findvalues(saplines, findvalue(filelines, "Part Number:"))) #SAP description
            sel.itype("id=FormControl_V1_I1_S2_I1_T6", findvalue(filelines, "Part Number:")) #Part Number
            
            #sel.itype("id=FormControl_V1_I1_S6_I9_T2", findvalue(filelines, "Root Product Version:")) # Root Product Version
            #sel.itype("id=FormControl_V1_I1_S6_I9_S5_I13_T1", findvalue(filelines, "File Name:")) # File Name
            sel.itype("id=FormControl_V1_I1_S6_I9_S5_I13_T2", findvalue(filelines, "File Size:").replace("bytes","")) # File Size
            sel.itype("id=FormControl_V1_I1_S6_I9_T6", findvalue(filelines, "Unpacked File Size:").replace("bytes","")) # Unpacked File Size
            sel.itype("id=FormControl_V1_I1_S6_I9_T7", findvalues(saplines, findvalue(filelines, "Part Number:"),2)) # End User Download Link
            
            sel.itype("id=FormControl_V1_I1_S6_I9_S9_I14_T1", findvalue(filelines, "MD5 Checksum:")) #MD5 Checksum
            sel.itype("id=FormControl_V1_I1_S6_I9_T11", country) #Country of Origin  
            if findvalue(filelines, "Internal Version Number:")!=None:
                sel.itype("id=FormControl_V1_I1_S6_I9_T12", findvalue(filelines, "Internal Version Number:").split("_")[0]) # Internal Version Number(Build Number):
        
            
            sel.itype("id=FormControl_V1_I1_S6_I9_S14_I5_T1", findvalue(filelines, "Product Line Code (SAP):")) #Product Line Code (SAP):
            sel.itype("id=FormControl_V1_I1_S6_I9_S14_I5_T2", findvalue(filelines, "Product Line Code (SAP):")) #Product Line Code (SAP):
            sel.itype("id=FormControl_V1_I1_S6_I9_S5_I13_T1", findvalue(filelines, "File Name:")) # File Name
        elif releasetype=="USB":
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=0")  #Type of Release
            sel.select("id=FormControl_V1_I1_S2_I1_D7", "index=3")
            sel.select("id=FormControl_V1_I1_S6_I9_D10", "index=0")  #Network Path
            sel.select("id=FormControl_V1_I1_S6_I9_D10", "index=1")  

            #Product Language
            if ilanguage!=None:
                if ilanguage=="British English" or ilanguage=="Czech" or ilanguage=="Dutch" or ilanguage=="European English" or ilanguage=="German":
                    sel.click("//input[@value='"+ilanguage+"']") 
                else:
                    sel.click("//input[@value='"+ilanguage+" ']") 

            if osinfo.find("Win")!=-1 and osinfo.find("64")!=-1 and osinfo.find("86")!=-1:
                sel.click("//input[@value='Win32Bit']") # Operating System
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!"
                sel.click("//input[@value='Win64Bit']")   
                while not sel.is_element_present("//input[@value='MAC 32']"):
                    print "wait!" 
            elif osinfo.find("Win")!=-1 and osinfo.find("86")!=-1:
                sel.click("//input[@value='Win32Bit']") # Operating System
            elif osinfo.find("Win")!=-1 and osinfo.find("64")!=-1:
                sel.click("//input[@value='Win64Bit']")  

            sel.itype("id=FormControl_V1_I1_S2_I1_T5", findvalue(filelines, "Product Line Code (SAP):")) #SAP description
            sel.itype("id=FormControl_V1_I1_S2_I1_T6", findvalue(filelines, "Part Number:")) #Part Number
            
            sel.itype("id=FormControl_V1_I1_S5_I8_T1", findvalue(filelines, "File Name:")) # File Name
            sel.itype("id=FormControl_V1_I1_S5_I8_T2", findvalue(filelines, "File Size:").replace("bytes","")) # File size
            sel.itype("id=FormControl_V1_I1_S5_I8_T3", findvalue(filelines, "Inventory File Name:")) # File size
                
            sel.itype("id=FormControl_V1_I1_S5_I8_T5", findvalue(filelines, "MD5 Checksum:")) # MD5 checksum
            if findvalue(filelines, "Internal Version Number:")!=None:
                sel.itype("id=FormControl_V1_I1_S5_I8_T8", findvalue(filelines, "Internal Version Number:").split("_")[0]) # Internal Version Number(Build Number):
            sel.itype("id=FormControl_V1_I1_S5_I8_T7", country) #Country of Origin
# Return value from the line list. 
def findvalue(linelist, keyvalue, spliter=":"):
    for line in linelist:
        if line.find(keyvalue)!=-1:
            if keyvalue=="File Size:":
                if line.find( "Unpacked File Size:")==-1:
                    return line.split(keyvalue)[1].strip()
            else:
                return line.split(keyvalue)[1].strip()

# Return value from the line list. 
def findvalues(linelist, keyvalue,index=1,  spliter=","):
    for line in linelist:
        if line.find(keyvalue)!=-1:
            return line.split(spliter)[index].strip()
if __name__=="__main__":
	fillrelease(sys.argv[1], sys.argv[2], sys.argv[3])
