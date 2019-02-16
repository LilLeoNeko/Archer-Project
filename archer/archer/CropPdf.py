import os, sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from archer import db
from archer.models import Document, Partition

class CropPdf(object):
	def __init__(self, filename, filepath):
		target = os.path.join(filepath,filename[:-4])
		if not os.path.isdir(target):
			os.mkdir(target)
		print (target)	
		os.system('pdf-crop-margins -v -s -u ' + '"'+filepath+filename+'"'+' -o '+'"'+target
				+"/"+"%s(MARGINLESS).pdf" %filename[:-4]+'"')
		crop = 'python3 archer/pdf_crop.py -m '
		if filepath[-16:]=="death_1968-1973/":
			newdoc = Document.query.filter_by(docname = filename).first()

			os.system(crop+'"'+"0.955 0.9627 0.09 0.6985"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(ONE).pdf" %filename[:-4]+'"')
			part1 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
						url = "death_1968-1973/%s/%s(ONE).pdf" %(filename[:-4],filename[:-4]),
						properties="No.;When and where died;Usual Place of Residence;Name and Surname;Occupation;Sex and age")

			os.system(crop+'"'+"0.955 0.735 0.09 0.6"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(TWO).pdf" %filename[:-4]+'"')
			part2 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 2, count = 0, flag = False, 
						url = "death_1968-1973/%s/%s(TWO).pdf" %(filename[:-4],filename[:-4]),
						properties="Cause of death and duration of last illness;\
									Legally qualified medical practitioner by whom certified and when he last saw deceased")

			os.system(crop+'"'+"0.955 0.635 0.09 0.55"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(THREE).pdf" %filename[:-4]+'"')
			part3 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1968-1973/%s/%s(THREE).pdf" %(filename[:-4],filename[:-4]),
						properties="Name and surname of father and mother(malden name, if known), with occupation")
			
			os.system(crop+'"'+"0.955 0.585 0.09 0.49"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FOUR).pdf" %filename[:-4]+'"')
			part4 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1968-1973/%s/%s(FOUR).pdf" %(filename[:-4],filename[:-4]),
						properties="Signature, description, and residence of informant")
			
			os.system(crop+'"'+"0.955 0.53 0.09 0.419"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FIVE).pdf" %filename[:-4]+'"')
			part5 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 3, count = 0, flag = False, 
						url = "death_1968-1973/%s/%s(FIVE).pdf" %(filename[:-4],filename[:-4]),
						properties="Signature of Registration Officer;Date;Where registered")
			
			os.system(crop+'"'+"0.955 0.46 0.09 0.33"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SIX).pdf" %filename[:-4]+'"')
			part6 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 2, count = 0, flag = False, 
						url = "death_1968-1973/%s/%s(SIX).pdf" %(filename[:-4],filename[:-4]),
						properties="When and where buried;Name and Religion of Minister, or names of witnesses of burial")
			
			os.system(crop+'"'+"0.955 0.38 0.09 0.263"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SEVEN).pdf" %filename[:-4]+'"')
			part7 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1968-1973/%s/%s(SEVEN).pdf" %(filename[:-4],filename[:-4]),
						properties="Where born and how long in the Australian states, stating which")
			
			os.system(crop+'"'+"0.955 0.33 0.09 0.0713"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(EIGHT).pdf" %filename[:-4]+'"')
			part8 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 5, count = 0, flag = False, 
						url = "death_1968-1973/%s/%s(EIGHT).pdf" %(filename[:-4],filename[:-4]),
						properties="Where and;At what age and;To whom;Conjugal Condition at date of Death;\
						Issue in order of birth, the names and ages")

			db.session.add(part1)
			db.session.add(part2)
			db.session.add(part3)
			db.session.add(part4)
			db.session.add(part5)
			db.session.add(part6)
			db.session.add(part7)
			db.session.add(part8)
			db.session.commit()


		elif filepath[-16:]=="death_1959-1966/":
			newdoc = Document.query.filter_by(docname = filename).first()

			os.system(crop+'"'+"0.955 0.9627 0.09 0.6985"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(ONE).pdf" %filename[:-4]+'"')
			part1 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
						url = "death_1959-1966/%s/%s(ONE).pdf" %(filename[:-4],filename[:-4]),
						properties="No.;When and where died;Usual Place of Residence;Name and Surname;Occupation;Sex and age")

			os.system(crop+'"'+"0.955 0.735 0.09 0.6"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(TWO).pdf" %filename[:-4]+'"')
			part2 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 4, count = 0, flag = False, 
						url = "death_1959-1966/%s/%s(TWO).pdf" %(filename[:-4],filename[:-4]),
						properties="Cause of death;Duration of last illness;\
									Legally qualified medical practitioner by whom certified;When he last saw deceased")

			os.system(crop+'"'+"0.955 0.635 0.09 0.55"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(THREE).pdf" %filename[:-4]+'"')
			part3 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1959-1966/%s/%s(THREE).pdf" %(filename[:-4],filename[:-4]),
						properties="Name and surname of father and mother(malden name, if known), with occupation")
			
			os.system(crop+'"'+"0.955 0.585 0.09 0.49"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FOUR).pdf" %filename[:-4]+'"')
			part4 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1959-1966/%s/%s(FOUR).pdf" %(filename[:-4],filename[:-4]),
						properties="Signature, description, and residence of informant")
			
			os.system(crop+'"'+"0.955 0.53 0.09 0.419"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FIVE).pdf" %filename[:-4]+'"')
			part5 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 3, count = 0, flag = False, 
						url = "death_1959-1966/%s/%s(FIVE).pdf" %(filename[:-4],filename[:-4]),
						properties="Signature of Registration Officer;Date;Where registered")
			
			os.system(crop+'"'+"0.955 0.46 0.09 0.33"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SIX).pdf" %filename[:-4]+'"')
			part6 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 2, count = 0, flag = False, 
						url = "death_1959-1966/%s/%s(SIX).pdf" %(filename[:-4],filename[:-4]),
						properties="When and where buried;Name and Religion of Minister, or names of witnesses of burial")
			
			os.system(crop+'"'+"0.955 0.38 0.09 0.263"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SEVEN).pdf" %filename[:-4]+'"')
			part7 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1959-1966/%s/%s(SEVEN).pdf" %(filename[:-4],filename[:-4]),
						properties="Where born and how long in the Australian states, stating which")
			
			os.system(crop+'"'+"0.955 0.33 0.09 0.0713"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(EIGHT).pdf" %filename[:-4]+'"')
			part8 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 5, count = 0, flag = False, 
						url = "death_1959-1966/%s/%s(EIGHT).pdf" %(filename[:-4],filename[:-4]),
						properties="Where and;At what age and;To whom;Conjugal Condition at date of Death;\
						Issue in order of birth, the names and ages")

			db.session.add(part1)
			db.session.add(part2)
			db.session.add(part3)
			db.session.add(part4)
			db.session.add(part5)
			db.session.add(part6)
			db.session.add(part7)
			db.session.add(part8)
			db.session.commit()

		elif filepath[-16:]=="death_1940-1956/":
			newdoc = Document.query.filter_by(docname = filename).first()

			os.system(crop+'"'+"0.955 0.98 0.09 0.77"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(ONE).pdf" %filename[:-4]+'"')
			part1 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 3, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(ONE).pdf" %(filename[:-4],filename[:-4]),
						properties="No.;When and where died;Usual Place of Residence")

			os.system(crop+'"'+"0.955 0.81 0.09 0.73"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(TWO).pdf" %filename[:-4]+'"')
			part2 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 2, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(TWO).pdf" %(filename[:-4],filename[:-4]),
						properties="Name andSurname;Occupation")

			os.system(crop+'"'+"0.955 0.765 0.09 0.71"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(THREE).pdf" %filename[:-4]+'"')
			part3 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(THREE).pdf" %(filename[:-4],filename[:-4]),
						properties="Sex and age")

			os.system(crop+'"'+"0.955 0.744 0.09 0.61"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FOUR).pdf" %filename[:-4]+'"')
			part4 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 4, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(FOUR).pdf" %(filename[:-4],filename[:-4]),
						properties="Cause of death;Duration of last illness;\
						Legally qualified medical practitioner by whom certified;\
						When he last saw deceased")

			os.system(crop+'"'+"0.955 0.635 0.09 0.56"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FIVE).pdf" %filename[:-4]+'"')
			part5 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(FIVE).pdf" %(filename[:-4],filename[:-4]),
						properties="Name and surname of father and mother(malden name, if known). \
						with occupation")

			os.system(crop+'"'+"0.955 0.58 0.09 0.477"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SIX).pdf" %filename[:-4]+'"')
			part6 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(SIX).pdf" %(filename[:-4],filename[:-4]),
						properties="Signature, Description, and Residence of Informant")

			os.system(crop+'"'+"0.955 0.5 0.09 0.435"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SEVEN).pdf" %filename[:-4]+'"')
			part7 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 3, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(SEVEN).pdf" %(filename[:-4],filename[:-4]),
						properties="Signature of Registrar;Date and;Where Registered")

			os.system(crop+'"'+"0.955 0.45 0.09 0.345"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(EIGHT).pdf" %filename[:-4]+'"')
			part8 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 3, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(EIGHT).pdf" %(filename[:-4],filename[:-4]),
						properties="When and where Buried;Undertaker by whom certified;Name and Religion of Minister,\
						 or names of Witnesses of burial")

			os.system(crop+'"'+"0.955 0.368 0.09 0.3"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(NINE).pdf" %filename[:-4]+'"')
			part9 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(NINE).pdf" %(filename[:-4],filename[:-4]),
						properties="Where born, and how long in the Australian States, stating which")

			os.system(crop+'"'+"0.955 0.32 0.09 0.19"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(TEN).pdf" %filename[:-4]+'"')
			part10 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 4, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(TEN).pdf" %(filename[:-4],filename[:-4]),
						properties="Where;At what Age;To Whom;Conjugal Condition at Date of Death")

			os.system(crop+'"'+"0.955 0.23 0.09 0.05"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(ELEVEN).pdf" %filename[:-4]+'"')
			part11 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1940-1956/%s/%s(ELEVEN).pdf" %(filename[:-4],filename[:-4]),
						properties="Issue in order of Birth, the Names and Ages")

			db.session.add(part1)
			db.session.add(part2)
			db.session.add(part3)
			db.session.add(part4)
			db.session.add(part5)
			db.session.add(part6)
			db.session.add(part7)
			db.session.add(part8)
			db.session.add(part9)
			db.session.add(part10)
			db.session.add(part11)
			db.session.commit()

		elif filepath[-16:]=="death_1885-1929/":
			newdoc = Document.query.filter_by(docname = filename).first()

			os.system(crop+'"'+"0.458 0.83 0 0.64"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftONE).pdf" %filename[:-4]+'"')
			part1 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(LeftONE).pdf" %(filename[:-4],filename[:-4]),
					properties="No.;When and where Died;Name and Surname, Occupation;Sex and Age;Cause of Death,\
					Duration of last Illness, Legally qualified Medical practitioner by whom certified;\
					When he last saw Deceased;Nam and Surname of Father and Mother(Maiden Name if known), with Occupation")

			os.system(crop+'"'+"0.458 0.685 0 0.48"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftTWO).pdf" %filename[:-4]+'"')
			part2 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(LeftTWO).pdf" %(filename[:-4],filename[:-4]),
					properties="No.;When and where Died;Name and Surname, Occupation;Sex and Age;Cause of Death,\
					Duration of last Illness, Legally qualified Medical practitioner by whom certified;\
					When he last saw Deceased;Nam and Surname of Father and Mother(Maiden Name if known), with Occupation")

			os.system(crop+'"'+"0.458 0.533 0 0.325"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftTHREE).pdf" %filename[:-4]+'"')
			part3 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(LeftTHREE).pdf" %(filename[:-4],filename[:-4]),
					properties="No.;When and where Died;Name and Surname, Occupation;Sex and Age;Cause of Death,\
					Duration of last Illness, Legally qualified Medical practitioner by whom certified;\
					When he last saw Deceased;Nam and Surname of Father and Mother(Maiden Name if known), with Occupation")

			os.system(crop+'"'+"0.458 0.385 0 0.175"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftFOUR).pdf" %filename[:-4]+'"')
			part4 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(LeftFOUR).pdf" %(filename[:-4],filename[:-4]),
					properties="No.;When and where Died;Name and Surname, Occupation;Sex and Age;Cause of Death,\
					Duration of last Illness, Legally qualified Medical practitioner by whom certified;\
					When he last saw Deceased;Nam and Surname of Father and Mother(Maiden Name if known), with Occupation")

			os.system(crop+'"'+"0.458 0.235 0 0.01"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftFIVE).pdf" %filename[:-4]+'"')
			part5 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(LeftFIVE).pdf" %(filename[:-4],filename[:-4]),
					properties="No.;When and where Died;Name and Surname, Occupation;Sex and Age;Cause of Death,\
					Duration of last Illness, Legally qualified Medical practitioner by whom certified;\
					When he last saw Deceased;Nam and Surname of Father and Mother(Maiden Name if known), with Occupation")

			os.system(crop+'"'+"1 0.835 0.4 0.635"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightONE).pdf" %filename[:-4]+'"')
			part6 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(RightONE).pdf" %(filename[:-4],filename[:-4]),
					properties="Signature, Description and Residence of Informant;Signature of Registrar, Date and Where Registered;\
					When and where buried. Undertaker by whom certified;name and Religion of Minister, or Names of Witnesses of Burial;\
					Where Born, and how long in the Australian States, stating which;Where and at what, Age, and to Whom;\
					Issue in order of Birth, the Names and Ages")

			os.system(crop+'"'+"1 0.685 0.4 0.48"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightTWO).pdf" %filename[:-4]+'"')
			part7 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(RightTWO).pdf" %(filename[:-4],filename[:-4]),
					properties="Signature, Description and Residence of Informant;Signature of Registrar, Date and Where Registered;\
					When and where buried. Undertaker by whom certified;name and Religion of Minister, or Names of Witnesses of Burial;\
					Where Born, and how long in the Australian States, stating which;Where and at what, Age, and to Whom;\
					Issue in order of Birth, the Names and Ages")

			os.system(crop+'"'+"1 0.535 0.4 0.325"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightTHREE).pdf" %filename[:-4]+'"')
			part8 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(RightTHREE).pdf" %(filename[:-4],filename[:-4]),
					properties="Signature, Description and Residence of Informant;Signature of Registrar, Date and Where Registered;\
					When and where buried. Undertaker by whom certified;name and Religion of Minister, or Names of Witnesses of Burial;\
					Where Born, and how long in the Australian States, stating which;Where and at what, Age, and to Whom;\
					Issue in order of Birth, the Names and Ages")

			os.system(crop+'"'+"1 0.38 0.4 0.17"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightFOUR).pdf" %filename[:-4]+'"')
			part9 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(RightFOUR).pdf" %(filename[:-4],filename[:-4]),
					properties="Signature, Description and Residence of Informant;Signature of Registrar, Date and Where Registered;\
					When and where buried. Undertaker by whom certified;name and Religion of Minister, or Names of Witnesses of Burial;\
					Where Born, and how long in the Australian States, stating which;Where and at what, Age, and to Whom;\
					Issue in order of Birth, the Names and Ages")

			os.system(crop+'"'+"1 0.235 0.4 0"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightFIVE).pdf" %filename[:-4]+'"')
			part10 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_1885-1929/%s/%s(RightFIVE).pdf" %(filename[:-4],filename[:-4]),
					properties="Signature, Description and Residence of Informant;Signature of Registrar, Date and Where Registered;\
					When and where buried. Undertaker by whom certified;name and Religion of Minister, or Names of Witnesses of Burial;\
					Where Born, and how long in the Australian States, stating which;Where and at what, Age, and to Whom;\
					Issue in order of Birth, the Names and Ages")


			db.session.add(part1)
			db.session.add(part2)
			db.session.add(part3)
			db.session.add(part4)
			db.session.add(part5)
			db.session.add(part6)
			db.session.add(part7)
			db.session.add(part8)
			db.session.add(part9)
			db.session.add(part10)
			db.session.commit()