def heun_new(x, y, h, func):
	return y+h/2*(func(x,y)+ \
			func(x+h,y+h* \
			func(x,y)))

def compute_heun(x0, y0, h, func, n):
	x, y = x0, y0
	pairs = list()
	for i in range(n):
		pairs.append((x,y));
		y = heun_new(x, y, h, func)
		x += h
	return pairs

def main():
	pass

if __name__ == "__main__":
	main()
