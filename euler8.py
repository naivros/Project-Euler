import operator
import functools
L = []
L.append("73167176531330624919225119674426574742355349194934")
L.append("96983520312774506326239578318016984801869478851843")
L.append("85861560789112949495459501737958331952853208805511")
L.append("12540698747158523863050715693290963295227443043557")
L.append("66896648950445244523161731856403098711121722383113")
L.append("62229893423380308135336276614282806444486645238749")
L.append("30358907296290491560440772390713810515859307960866")
L.append("70172427121883998797908792274921901699720888093776")
L.append("65727333001053367881220235421809751254540594752243")
L.append("52584907711670556013604839586446706324415722155397")
L.append("53697817977846174064955149290862569321978468622482")
L.append("83972241375657056057490261407972968652414535100474")
L.append("82166370484403199890008895243450658541227588666881")
L.append("16427171479924442928230863465674813919123162824586")
L.append("17866458359124566529476545682848912883142607690042")
L.append("24219022671055626321111109370544217506941658960408")
L.append("07198403850962455444362981230987879927244284909188")
L.append("84580156166097919133875499200524063689912560717606")
L.append("05886116467109405077541002256983155200055935729725")
L.append("71636269561882670428252483600823257530")
LToStr =''.join(L)
x = 0
y = 4
num = 0
oldNum = 0
listStr=list(LToStr)
listNum= list(map(int, listStr))
while(y<=988):
	num = functools.reduce(operator.mul, listNum[x:y], 1)
	if num> oldNum:
		oldNum = num
	x+=1
	y+=1
print(oldNum)

