import json

class Config:

	def __init__(self, file):
		self.file = file

	def read(self):
		try:
			with open(self.file) as jsonData:
				return(json.load(jsonData))
		except IOError:
			return(float('NaN'))

