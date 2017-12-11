def is_prime(n):
	if n%2 ==0:return False
	checkOdd=3
	while checkOdd < n**.5 + 1:
		if n  % checkOdd ==0: return False
		checkOdd+=2
	return True
def nth_prime(n):
	prime = 2
	counter = 1
	iter = 3
	while counter<n:
		if is_prime(iter):
			prime = iter
			counter += 1
		iter += 2
	return prime
prime = nth_prime(10001)
print(prime)
