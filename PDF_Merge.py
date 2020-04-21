import os
import sys
from PyQt5.QtWidgets import *
from PyPDF2 import PdfFileReader, PdfFileWriter

class App(QWidget):
   def __init__(self, parent = None):
      super(App, self).__init__(parent)

      self.layout = QVBoxLayout()

      self.le = QLabel("Merging PDF files!")
      self.layout.addWidget(self.le)

      self.btn = QPushButton("Open File(s)")
      self.btn.clicked.connect(self.getfile)
      self.layout.addWidget(self.btn)

      btn1 = QPushButton("Merge!")
      btn1.clicked.connect(self.PDF_Merg_Fn)
      self.layout.addWidget(btn1)

      self.le = QLabel("Added Files: ")
      self.layout.addWidget(self.le)

      self.setLayout(self.layout)
      self.setWindowTitle("PDF Merger!")

   def getfile(self):
      self.paths, _ = QFileDialog.getOpenFileNames(self, 'Open files', "~",
                                                "PDF Files (*.pdf)")

      i = 0
      while i < len(self.paths):
          _, file_name = os.path.split(self.paths[i])
          self.layout.addWidget(QLabel("{}".format(file_name)))
          i += 1

      return self.paths


   def PDF_Merg_Fn(self):
       paths = self.paths
       main_path = os.path.split(self.paths[0])
       output = os.path.join(main_path[0], 'merged.pdf')

       pdf_writer = PdfFileWriter()
       for path in paths:
           pdf_reader = PdfFileReader(path)
           for page in range(pdf_reader.getNumPages()):
               pdf_writer.addPage(pdf_reader.getPage(page))

       with open(output, 'wb') as out:
           pdf_writer.write(out)
           alert = QMessageBox()
           alert.setText("Files Sucessfully Merged!")
           alert.exec_()


app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())
