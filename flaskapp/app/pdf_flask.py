# PDF in a Flask.
# pdf_flask.py

# Description: Program to generate PDF from text, over the web,
# using xtopdf, ReportLab and the Flask web framework.
# It can be used to create short, simple PDF e-books.
# Author: Vasudev Ram - http://dancingbison.com
# Copyright 2013 Vasudev Ram 
# Tested with Python 2.7.

# Version: 0.1

import traceback
from textwrap import TextWrapper
from PDFWriter import PDFWriter
from flask import Flask, request

app = Flask(__name__)

@app.route("/pdf_book", methods=['GET', 'POST'])
def pdf_book():
    if request.method == 'GET':
        # Display the PDF book creation form.
        return '''
            <form action="/pdf_book" method="post">
                PDF file name: <input type="text" name="pdf_file_name" />

                Header: <input type="text" name="header" />
                Footer: <input type="text" name="footer" />

                Content:
                <textarea name="content" rows="15" cols="50"></textarea>

                <input type="submit" value="Submit" />

            </form>
            '''
    else:
        # Create the PDF book from the posted form content.
        try:
            # Get the needed fields from the form.
            pdf_file_name = request.form['pdf_file_name']
            header = request.form['header']
            footer = request.form['footer']
            content = request.form['content']

            # Create a PDFWriter instance and set some of its fields.
            pw = PDFWriter(pdf_file_name)
            pw.setFont("Courier", 12)
            pw.setHeader(header)
            pw.setFooter(footer)

            # Get the content field.
            # Split it into paragraphs delimited by newlines.
            # Convert each paragraph into a list of lines of
            # maximum width 70 characters.
            # Print each line to the PDF file.
            paragraphs = content.split('\n')
            wrapper = TextWrapper(width=70, drop_whitespace=False)
            for paragraph in paragraphs:
                lines = wrapper.wrap(paragraph)
                for line in lines:
                    pw.writeLine(line)

            pw.savePage()
            pw.close()
            return "OK. PDF book created in file " + pdf_file_name + ".\n"
        except Exception, e:
            traceback.print_stack()
            return "Error: PDF book not created.\n" + repr(e) + ".\n" 

if __name__ == "__main__":
    app.run(debug=True) 
    
# EOF

