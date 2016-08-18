class PrimeChecker(object):
	def __init__(self, number = ""):
		self.number = number
	def is_prime(self):
		if self.number == "":
			return False
		elif (type(self.number) is not str) or type(self.number is not int):
			return False
		else:
			try:
				int(self.number)
			except(ValueError):
				return False
			else:
				if self.number < 2:
					return False
				elif self.number == 2:
					return True
				elif self.number > 2:
					for num in range(2,self.number):
						if self.number % num == 0:
							return False
					return True
prime_number = PrimeChecker("kevin")
print(prime_number.is_prime())
