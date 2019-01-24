#
#  simulator.py
#
#  Created by DAWEIXU on 2019/01/11.
#  Copyright © 2019 unimelb_daweixu. All rights reserved.
#

#! /usr/bin/python

import os, sys

file_name = str(sys.argv[1])

marginless = 'pdf-crop-margins -v -s -u '
os.system(marginless + '"'+file_name+'"'+' -o '+'"'+"Marginless"+file_name+'"')

crop = 'python3 pdf_crop.py -m '

os.system(crop + '"'+"0.955 0.33 0.09 0.0713"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_12_13_"+file_name+'"')
os.system(crop + '"'+"0.955 0.38 0.09 0.263"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_11_"+file_name+'"')
os.system(crop + '"'+"0.955 0.46 0.09 0.33"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_9_10_"+file_name+'"')
os.system(crop + '"'+"0.955 0.53 0.09 0.419"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_8_"+file_name+'"')
os.system(crop + '"'+"0.955 0.585 0.09 0.49"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_7_"+file_name+'"')
os.system(crop + '"'+"0.955 0.635 0.09 0.55"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_6_"+file_name+'"')
os.system(crop + '"'+"0.955 0.735 0.09 0.6"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_5_"+file_name+'"')
os.system(crop + '"'+"0.955 0.9627 0.09 0.6985"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_1_2_3_4_"+file_name+'"')

'''death1
os.system(crop + '"'+"0.955 0.23 0.09 0.05"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_13_"+file_name+'"') 
os.system(crop + '"'+"0.955 0.32 0.09 0.19"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_12_"+file_name+'"')
os.system(crop + '"'+"0.955 0.368 0.09 0.3"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_11_"+file_name+'"')
os.system(crop + '"'+"0.955 0.45 0.09 0.345"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_9_10_"+file_name+'"')
os.system(crop + '"'+"0.955 0.5 0.09 0.435"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_8_"+file_name+'"')
os.system(crop + '"'+"0.955 0.58 0.09 0.477"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_7_"+file_name+'"')
os.system(crop + '"'+"0.955 0.635 0.09 0.56"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_6_"+file_name+'"')
os.system(crop + '"'+"0.955 0.744 0.09 0.61"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_5_"+file_name+'"')
os.system(crop + '"'+"0.955 0.765 0.09 0.71"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_4_"+file_name+'"')
os.system(crop + '"'+"0.955 0.81 0.09 0.73"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_3_"+file_name+'"')
os.system(crop + '"'+"0.955 0.98 0.09 0.77"+'"'+' -i '+'"'+"Marginless"+file_name+'"'+' -o '+'"'+"_1_2_"+file_name+'"')
'''
