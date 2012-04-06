n = 1

fizz = n % 3
buzz = n % 5
fizzbuzz = n % 15

while (n < 101):
	if n % 15 == 0:
		print "FizzBuzz"
	elif n % 5 == 0:
		print "Buzz"
	elif n % 3 == 0:
		print "Fizz"
	else:
		print n
	n = n + 1
