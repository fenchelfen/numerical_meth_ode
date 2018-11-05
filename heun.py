def heun_new(x, y, h, func):
	return y+h/2*(func(x,y)+ \
			func(x+h,y+h* \
			func(x,y)))

def heun_compute(x0, y0, h, func, n):
	x, y = x0, y0
	pairs = list()
	for i in range(n+1):
		pairs.append((x,y));
		y = heun_new(x, y, h, func)
		x += h
	return pairs

def main():
	pass

if __name__ == "__main__":
	main()
