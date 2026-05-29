import re
class Validator:
    def __init__(self):
        self.errors = []
        self.namePattern = "^[A-Z][a-zA-Z ]+$"
        self.numberPattern = "^\\d+$"
        self.decimalPattern = "^-?\\d+(\\.\\d+)?$"
        
    def validate(self, pattern, input):
        return re.match(pattern, input)
    
    def isEmpty(self, input):
        return input == ""
    
    def generateErrors(self, name):
        if not self.validate(self.namePattern, name):
            self.addError("Incorrect name pattern!\n")
    
    def generateErrors(self, name, credit, age, no):
        if not self.validate(self.namePattern, name):
            self.addError("Incorrect name pattern!\n")
        if not self.validate(self.decimalPattern, credit):
            self.addError("Incorrect credit pattern!\n")
        if not self.validate(self.numberPattern, age):
            self.addError("Incorrect age pattern!\n")
        if not self.validate(self.numberPattern, no):
            self.addError("Incorrect number pattern!\n")
    
    def isValid(self, name):
        return self.validate(self.namePattern, name)
    
    def isValid(self, name, credit, age, no):
        return self.validate(self.namePattern, name) and \
               self.validate(self.decimalPattern, credit) and \
               self.validate(self.numberPattern, age) and \
               self.validate(self.numberPattern, no)
    
    def addError(self, msg):
        self.errors.append(msg)

    def errors(self):
        return self.errors

    def clear(self):
        self.errors.clear()