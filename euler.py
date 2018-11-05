def euler_new(x, y, h, func):
	return y+func(x,y)*h

def euler_compute(x0, y0, h, func, n):
	x, y = x0, y0
	pairs = list()
	for i in range(n+1):
		pairs.append((x,y));
		y = euler_new(x, y, h, func)
		x += h
	return pairs

def main():
	pass

if __name__ == "__main__":
	main()
