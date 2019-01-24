# Archer-Project
Computing Project for Master of Information Technology in University of Melbourne
1. setup your own virtual environment(or at your local environment at your own risk)
2. install all the python packages and flask extensions: flask_sqlalchemy, flask_bcrypt, flask_login
3. using command line to go to archer folder, execute"python runArcher.py"
4. go to your local host by browser



# How to use PdfCrop
1. In this program, we took advantage of a command-line application pdfCropMargins to crop the margins of PDF files, so you need to install pdfCropMargins, pdftoppm and PyPDF2.
Way to install pdfCropMargins：

pip install pdfCropMargins

Way to install PyPDF2:

pip install PyPDF2

Way to install pdftoppm:

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null

brew install poppler

2. Run the program use:
python3 simulator.py PATH/"file_name.pdf" NUMBEROFSECTION
e.g 
python3 simulator.py death1/"Alberry, Frank 1968.pdf" 6
python3 simulator.py death2/"BARBER_Robert_Glayward_1956.pdf" 5
python3 simulator.py death3/"VIC death 1885_9952_9956.pdf" L3
NumOfSection of .pdfs in death3 need add 'L' or 'R' as prefix.