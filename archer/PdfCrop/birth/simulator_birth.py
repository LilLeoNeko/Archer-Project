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
