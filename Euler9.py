def sum(n):
	for a in range(1,n,1):
		for b in range(1,n-a,1):
			c=n-a-b
			if a**2+b**2==c**2:
				return a*b*c
	return False;
product=sum(1001)
print(product)
