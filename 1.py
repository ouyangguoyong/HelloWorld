def func():
	a = 1
	b = 2
	c = 3
	args = ()
	args = a,b,c
	return args
	
if __name__ == '__main__':
	r = func()
	print(type(r))
	print(r)
	

