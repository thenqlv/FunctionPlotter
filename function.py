class Function	:
	def __init__(self,codeString):
		self.codeString = codeString
		self.indexOfTheCodeString = -1
		self.indexOfBrackets = -1
	
	def getNextTransition(self):
		self.indexOfTheCodeString += 1
		return self.codeString[self.indexOfTheCodeString]
	
	def getCurrentTransition(self):
		return self.codeString[self.indexOfTheCodeString]
		
	def isError(self):
		return self.indexOfTheCodeString != (len(self.codeString) - 1) or self.indexOfBrackets != -1

