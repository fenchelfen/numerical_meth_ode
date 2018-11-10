def rk_new(x, y, h, func):

    k_1 = func(x, y)
    k_2 = func(x + h/2, y + h/2*k_1)
    k_3 = func(x + h/2, y + h/2*k_2)
    k_4 = func(x + h, y + h*k_3)
    return y + h/6* \
            (k_1 + 2*k_2 + 2*k_3 + k_4)

def rk_compute(x0, y0, h, func, X):

	x, y = x0, y0
	pairs = list()
	while (x <= X):
		pairs.append((x,y));
		y = rk_new(x, y, h, func)
		x += h
	return pairs

def main():
	pass

if __name__ == "__main__":
	main()
