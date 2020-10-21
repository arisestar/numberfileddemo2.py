"""
program numberfileddemo2.py
author :audrey 10/14/2020
pg 264-265
"""


class NumberFieldDemo2(EasyFrame):
	""" cumputes and Displays the square root of an input number """


	def __init__(self):
		"""Sets up the window and widgets"""
		EasyFrame.__init__(self, title = "number Field demo")

		# label and filed for the input 
		self.addLabel(text = "An integer", row = 0, column = 1)
		self.inputField = self. addIntegerField( value = 0, row =0, column = 1,width=10)
		# bind the enter key to the inputField
		self.inputField.bind("<Return>" , lambda event : self.computeSqrt())


		# label and field for the output 
		self.addLabel( text = "square root=", row = 1 , column = 0)
		self.outputField = self.addloatField( value = 0.0, row = 1, column = 1 , state = "readonly", width = 8, precision = 2)

		# the command button 
		self.addButton(text = " Compute", row = 2, column = 0, columnspan = 2, command= self.computeSqrt)

	# the event handing method for the button 
	def computeSqrt(self):
		""" Inputs the string coverts it to uppercase and outputs the result.""" 
		try:
			number = self.inputField.getNumber()
			result = math.sqrt(number)
			self.outputField.setNumber(result)
		except ValueError:
			self.messageBox(title = "ERROR", message = "Input must be an integer >= 0 ")

def main():
	"""Instantiates and pops up the window"""
	NumberFiledDemo2().mainloop()

# global call to the main() function 
if __name == "__main__":
	main()