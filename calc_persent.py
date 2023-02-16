if input("Начинаем? (Y/N) ") == "y":
	while True:
		lst = input("Введите число и процент который надо посчитать(fe: 100 20) ").split()
		print(f"{lst[1]}% от числа {lst[0]}: {round(float(lst[0])/100*float(lst[1]),2)}")
		if input("Продолжить? (Y/N) ") == "y":
			continue
		else:	break
