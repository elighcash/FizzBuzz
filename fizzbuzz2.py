n = 1

def fizz():
	x = n % 3
	return x

def buzz():
	x = n % 5
	return x

def fizzbuzz():
	x = n % 15
	return x



while (n < 101):
	if fizzbuzz() == 0:
		print "FizzBuzz"
	elif buzz() == 0:
		print "Buzz"
	elif fizz() == 0:
		print "Fizz"
	else:
		print n
	n = n + 1
