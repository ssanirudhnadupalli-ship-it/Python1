from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

class TextFile(FileHandler):
    def read(self):
        print("Reading Text File")

class PDFFile(FileHandler):
    def read(self):
        print("Reading PDF File")

class CSVFile(FileHandler):
    def read(self):
        print("Reading CSV File")

f1 = TextFile()
f2 = PDFFile()
f3 = CSVFile()

f1.read()
f2.read()
f3.read()