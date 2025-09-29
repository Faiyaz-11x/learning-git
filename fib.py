def Fib(n: int)->int:

	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return Fib(n-1) + Fib(n-2)

if __name__=='__main__':
	number = int(input("enter a number: "))
	print(Fib(number))