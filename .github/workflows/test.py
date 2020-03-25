hrs = input("Enter Hours:")
rte = input("Rate per Hour:")
if hrs <= 40:
	h = float(hrs * rte)
elif hrs > 40:
	h = float(40 * rte + (hrs - 40) * 1.5 * rte)
print h
