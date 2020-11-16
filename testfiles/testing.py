
def testfunc(x):
	x+=10
	return x

for x in range(10):
	x = testfunc(x)
	print(x)
