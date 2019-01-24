#
#  pdf_crop.py
#
#  Created by DAWEIXU on 2019/01/11.
#  Copyright © 2019 unimelb_daweixu. All rights reserved.
#

#! /usr/bin/python
# Originally found on http://www.mobileread.com/forums/showthread.php?t=25565

import getopt, sys
from PyPDF2 import PdfFileWriter, PdfFileReader

def usage ():
    print ("""sjvr767\'s PDF Cropping Script.
Example:
my_pdf_crop.py -s -p 0.5 -i input.pdf -o output.pdf
my_pdf_crop.py --skip --percent 0.5 -input input.pdf -output output.pdf
\n
REQUIRED OPTIONS:
-p\t--percent
The factor by which to crop. Must be positive and less than or equal to 1.

-i\t--input
The path to the file to be cropped.
\n
OPTIONAL:
-s\t--skip
Skip the first page. Ouptut file will not contain the first page of the input file.

-o\t--output
Specify the name and path of the output file. If none specified, the script appends \'cropped\' to the file name.

-m\t--margin
Specify additional absolute cropping, for fine tuning results.
\t-m "left top right bottom"
""")
    sys.exit(0)
    
# not using dictionary in this program
def cut_length(dictionary, key, factor):
	cut_factor = 1-factor
	cut = float(dictionary[key])*cut_factor
	cut = cut / 4
	return cut
		
def new_coords(dictionary, key, cut, margin, code = "tl"):
	if code == "tl":
		if key == "x":
			return abs(cut+margin["l"])
		else:
			return abs(cut+margin["t"])
	elif code == "tr":
		if key == "x":
			return abs(cut+margin["r"])
		else:
			return abs(cut+margin["t"])
	elif code == "bl":
		if key == "x":
			return abs(cut+margin["l"])
		else:
			return abs(cut+margin["b"])
	else:
		if key == "x":
			return abs(cut+margin["r"])
		else:
			return abs(cut+margin["b"])

try:
	opts, args = getopt.getopt(sys.argv[1:], "sp:i:o:m:", ["skip", "percent=", "input=", "output=", "margin="])
except getopt.GetoptError as err:
        # print help information and exit:
        print (str(err)) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

skipone = 0

for a in opts[:]:
	if a[0] == '-s' or a[0]=='--skip':
		skipone = 1

factor = 1 #default scaling factor

for a in opts[:]:
	if a[0] == '-p' or a[0]=='--factor':
		if a[1] != None:
			try:
				factor = float(a[1])
			except TypeError:
				print ("Factor must be a number.")
				sys.exit(2) #exit if no appropriate input file

input_file = None #no defualt input file
		
for a in opts[:]:
	if a[0] == '-i' or a[0]=='--input':
		if a[1] != None:
			try:
				if a[1][-4:]=='.pdf':
					input_file = a[1]
					print (input_file)
				else:
					print ("Input file must be a PDF.")
					sys.exit(2) #exit if no appropriate input file
			except TypeError:
				print ("Input file must be a PDF.")
				sys.exit(2) #exit if no appropriate input file
			except IndexError:
				print ("Input file must be a PDF.")
				sys.exit(2) #exit if no appropriate input file
		else:
			print ("Please speicfy an input file.")
			sys.exit(2) #exit if no appropriate input file

output_file = "%s_cropped.pdf" %input_file[:-4] #default output

input1 = PdfFileReader(open(input_file, "rb"))



pages = input1.getNumPages()

for a in opts[:]:
	if a[0] == '-o' or a[0]=='--output': 
		if a[1]!= None:
			try:
				if a[1][-4:]=='.pdf':
					output_file = a[1]
				else:
					print ("Output file must be a PDF.")
			except TypeError:
				print ("Output file must be a PDF.")
			except IndexError:
				print ("Output file must be a PDF.")




margin = {"t": 0, "r": 0, "l": 0, "b": 0}

for a in opts[:]:
	if a[0] == '-m' or a[0]=='--margin':
		if a[1]!= None:
			m_temp = a[1].strip("\"").split()
			for i in range(pages):
				page = input1.getPage(i)
				margin["r"] = float(m_temp[0])*float(page.mediaBox.getUpperRight_x())
				margin["t"] = float(m_temp[1])*float(page.mediaBox.getUpperRight_y())
				margin["l"] = float(m_temp[2])*float(page.mediaBox.getUpperRight_x())
				margin["b"] = float(m_temp[3])*float(page.mediaBox.getUpperRight_y())
		else:
			print ("Error")
			
output = PdfFileWriter()
outputstream = open(output_file, "wb")

for i in range(pages):
	page = input1.getPage(i)
	top_right = {'x': page.mediaBox.getUpperRight_x(), 'y': page.mediaBox.getUpperRight_y()}
	top_left = {'x': page.mediaBox.getUpperLeft_x(), 'y': page.mediaBox.getUpperLeft_y()}
	bottom_right = {'x': page.mediaBox.getLowerRight_x(), 'y': page.mediaBox.getLowerRight_y()}
	bottom_left = {'x': page.mediaBox.getLowerLeft_x(), 'y': page.mediaBox.getLowerLeft_y()}

#print('Page dim.\t%f by %f' %(top_right['x'], top_right['y']))

cut = cut_length(top_right, 'x', factor)

new_tr = (new_coords(top_right, 'x', cut, margin, code = "tr"), new_coords(top_right, 'y', cut, margin, code = "tr"))
new_br = (new_coords(bottom_right, 'x', cut, margin, code = "br"), new_coords(bottom_right, 'y', cut, margin, code = "br" ))
new_tl = (new_coords(top_left, 'x', cut, margin, code = "tl"), new_coords(top_left, 'y', cut, margin, code = "tl"))
new_bl = (new_coords(bottom_left, 'x', cut, margin, code = "bl"), new_coords(bottom_left, 'y', cut, margin, code = "bl"))

if skipone == 0:
	for i in range(0, pages):
		page = input1.getPage(i)
		page.mediaBox.upperLeft = new_tl
		page.mediaBox.upperRight = new_tr
		page.mediaBox.lowerLeft = new_bl
		page.mediaBox.lowerRight = new_br
		output.addPage(page)
else:
	for i in range(1, pages):
		page = input1.getPage(i)
		page.mediaBox.upperLeft = new_tl
		page.mediaBox.upperRight = new_tr
		page.mediaBox.lowerLeft = new_bl
		page.mediaBox.lowerRight = new_br
		output.addPage(page)
print ("Crop Finished")
output.write(outputstream)
outputstream.close()
