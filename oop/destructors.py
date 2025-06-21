class Filehandler:
    def __init__(self, Filename):
        self.Filename = Filename
        self.file = open(Filename, 'r')
        
    def read_data(self):
        return self.file.read()
    
    def _del_ (self):
        return self.file.close()
    
file_obj = Filehandler('sample.txt')
print(file_obj.read_data())
