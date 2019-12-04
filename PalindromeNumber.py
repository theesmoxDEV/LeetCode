if __name__=="__main__":

	def isPalindrome(x: int) -> bool:
			if x<0:
				return False
			rev = 0
			origin = x
			while x!= 0:
				pop = x%10
				x//=10
				rev = rev*10+pop
			if origin==rev:
				return True
			else:
				return False

	while True:
	
		x = int(input("Number: "))
		print(isPalindrome(x))