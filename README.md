# Archer-Project
Computing Project for Master of Information Technology in University of Melbourne

prefer operating system: Mac OS.
Warning: Using Windows will lead to the result of missing "python3" command, which will makes admin upload certificate function not working properly.

installation:
1. install python3 and setup your own virtual environment(optional)
2. install all flask extensions: flask_sqlalchemy, flask_bcrypt, flask_login, flask_wtf, pdfCropMargins, PyPDF2
3. install pdftoppm by installing poppler, mac user can install poppler by :
  - ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
  - brew install poppler
 
4. using command line to go to archer folder, e.g "cd Archer-Project/archer" and execute the program e.g "python runArcher.py"
5. go to your local host by browser(default is 127.0.0.1/5000)



# How to use PdfCrop
1. In this program, we took advantage of a command-line application pdfCropMargins to crop the margins of PDF files, so you need to install pdfCropMargins, pdftoppm and PyPDF2.
Way to install pdfCropMargins：

pip install pdfCropMargins

Way to install PyPDF2:

pip install PyPDF2

Way to install pdftoppm:

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null

brew install poppler

