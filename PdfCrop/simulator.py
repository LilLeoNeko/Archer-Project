#
#  simulator.py
#
#  Created by DAWEIXU on 2019/01/11.
#  Copyright © 2019 unimelb_daweixu. All rights reserved.
#

#! /usr/bin/python

import os, sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def MergePdf(file1, file2_output):
	output = PdfFileWriter()
	outputPages = 0

	input = PdfFileReader(open(file1,"rb"))
	input1 = PdfFileReader(open(file2_output,"rb"))

	pageCount = input.getNumPages()
	pageCount1 = input1.getNumPages()
	
	for iPage in range(pageCount):
		output.addPage(input.getPage(iPage))

	for jPage in range(pageCount1):
		output.addPage(input1.getPage(jPage))	

	outputStream = open(file2_output,"wb")
	output.write(outputStream)
	outputStream.close()
	print("Finish combine Title and Content.")


marginless = 'pdf-crop-margins -v -s -u '
crop = 'python3 pdf_crop.py -m '

file_name = str(sys.argv[1])
numOfSection = str(sys.argv[2])

os.system(marginless + '"'+file_name+'"'+' -o '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"')

if file_name[:6] == "death1":
	if numOfSection == "1":
		os.system(crop + '"'+"0.955 0.9627 0.09 0.6985"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(ONE).pdf" %file_name[:-4]+'"')
	elif numOfSection == "2":
		os.system(crop + '"'+"0.955 0.735 0.09 0.6"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(TWO).pdf" %file_name[:-4]+'"')
	elif numOfSection == "3":
		os.system(crop + '"'+"0.955 0.635 0.09 0.55"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(THREE).pdf" %file_name[:-4]+'"')
	elif numOfSection == "4":
		os.system(crop + '"'+"0.955 0.585 0.09 0.49"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(FOUR).pdf" %file_name[:-4]+'"')
	elif numOfSection == "5":
		os.system(crop + '"'+"0.955 0.53 0.09 0.419"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(FIVE).pdf" %file_name[:-4]+'"')
	elif numOfSection == "6":
		os.system(crop + '"'+"0.955 0.46 0.09 0.33"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(SIX).pdf" %file_name[:-4]+'"')
	elif numOfSection == "7":
		os.system(crop + '"'+"0.955 0.38 0.09 0.263"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(SEVEN).pdf" %file_name[:-4]+'"')	
	elif numOfSection == "8":				
		os.system(crop + '"'+"0.955 0.33 0.09 0.0713"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(EIGHT).pdf" %file_name[:-4]+'"')
	else: 
		print ("Invalid Input for Section.")

	

elif file_name[:6] == "death2":
	if numOfSection == "1":
		os.system(crop + '"'+"0.955 0.98 0.09 0.77"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(ONE).pdf" %file_name[:-4]+'"')
	elif numOfSection == "2":
		os.system(crop + '"'+"0.955 0.81 0.09 0.73"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(TWO).pdf" %file_name[:-4]+'"')
	elif numOfSection == "3":
		os.system(crop + '"'+"0.955 0.765 0.09 0.71"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(THREE).pdf" %file_name[:-4]+'"')	
	elif numOfSection == "4":
		os.system(crop + '"'+"0.955 0.744 0.09 0.61"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(FOUR).pdf" %file_name[:-4]+'"')
	elif numOfSection == "5":
		os.system(crop + '"'+"0.955 0.635 0.09 0.56"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(FIVE).pdf" %file_name[:-4]+'"')
	elif numOfSection == "6":
		os.system(crop + '"'+"0.955 0.58 0.09 0.477"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(SIX).pdf" %file_name[:-4]+'"')
	elif numOfSection == "7":
		os.system(crop + '"'+"0.955 0.5 0.09 0.435"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(SEVEN).pdf" %file_name[:-4]+'"')
	elif numOfSection == "8":
		os.system(crop + '"'+"0.955 0.45 0.09 0.345"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(EIGHT).pdf" %file_name[:-4]+'"')
	elif numOfSection == "9":
		os.system(crop + '"'+"0.955 0.368 0.09 0.3"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(NINE).pdf" %file_name[:-4]+'"')
	elif numOfSection == "10":
		os.system(crop + '"'+"0.955 0.32 0.09 0.19"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(TEN).pdf" %file_name[:-4]+'"')
	elif numOfSection == "11":
		os.system(crop + '"'+"0.955 0.23 0.09 0.05"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(ELEVEN).pdf" %file_name[:-4]+'"')		
											
elif file_name[:6] == "death3":
	if numOfSection == "L1":
		os.system(crop + '"'+"0.458 0.96 0 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"0.458 0.83 0 0.64"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftONE).pdf" %file_name[:-4]+'"')
		MergePdf("%s(LeftTITLE).pdf" %file_name[:-4],"%s(LeftONE).pdf" %file_name[:-4])
	elif numOfSection == "L2":
		os.system(crop + '"'+"0.458 0.96 0 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"0.458 0.685 0 0.48"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftTWO).pdf" %file_name[:-4]+'"')
		MergePdf("%s(LeftTITLE).pdf" %file_name[:-4],"%s(LeftTWO).pdf" %file_name[:-4])
	elif numOfSection == "L3":
		os.system(crop + '"'+"0.458 0.96 0 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"0.458 0.533 0 0.325"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftTHREE).pdf" %file_name[:-4]+'"')
		MergePdf("%s(LeftTITLE).pdf" %file_name[:-4],"%s(LeftTHREE).pdf" %file_name[:-4])
	elif numOfSection == "L4":
		os.system(crop + '"'+"0.458 0.96 0 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"0.458 0.385 0 0.175"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftFOUR).pdf" %file_name[:-4]+'"')
		MergePdf("%s(LeftTITLE).pdf" %file_name[:-4],"%s(LeftFOUR).pdf" %file_name[:-4])
	elif numOfSection == "L5":
		os.system(crop + '"'+"0.458 0.96 0 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"0.458 0.235 0 0.01"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftFIVE).pdf" %file_name[:-4]+'"')
		MergePdf("%s(LeftTITLE).pdf" %file_name[:-4],"%s(LeftFIVE).pdf" %file_name[:-4])
	elif numOfSection == "LT":
		os.system(crop + '"'+"0.458 0.96 0 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(LeftTITLE).pdf" %file_name[:-4]+'"')
	elif numOfSection == "R1":
		os.system(crop + '"'+"1 0.96 0.4 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"1 0.835 0.4 0.635"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightONE).pdf" %file_name[:-4]+'"')
		MergePdf("%s(RightTITLE).pdf" %file_name[:-4],"%s(RightONE).pdf" %file_name[:-4])
	elif numOfSection == "R2":
		os.system(crop + '"'+"1 0.96 0.4 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"1 0.685 0.4 0.48"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightTWO).pdf" %file_name[:-4]+'"')
		MergePdf("%s(RightTITLE).pdf" %file_name[:-4],"%s(RightTWO).pdf" %file_name[:-4])
	elif numOfSection == "R3":
		os.system(crop + '"'+"1 0.96 0.4 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"1 0.535 0.4 0.325"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightTHREE).pdf" %file_name[:-4]+'"')
		MergePdf("%s(RightTITLE).pdf" %file_name[:-4],"%s(RightTHREE).pdf" %file_name[:-4])
	elif numOfSection == "R4":
		os.system(crop + '"'+"1 0.96 0.4 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"1 0.38 0.4 0.17"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightFOUR).pdf" %file_name[:-4]+'"')
		MergePdf("%s(RightTITLE).pdf" %file_name[:-4],"%s(RightFOUR).pdf" %file_name[:-4])
	elif numOfSection == "R5":
		os.system(crop + '"'+"1 0.96 0.4 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightTITLE).pdf" %file_name[:-4]+'"')
		os.system(crop + '"'+"1 0.235 0.4 0"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightFIVE).pdf" %file_name[:-4]+'"')
		MergePdf("%s(RightTITLE).pdf" %file_name[:-4],"%s(RightFIVE).pdf" %file_name[:-4])
	elif numOfSection == "RT":
		os.system(crop + '"'+"1 0.96 0.4 0.79"+'"'+' -i '+'"'+"%s(MARGINLESS).pdf" %file_name[:-4]+'"'+' -o '+'"'+"%s(RightTITLE).pdf" %file_name[:-4]+'"')
