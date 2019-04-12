print("original			discount")
print("-------------------------")

original = [4.95, 9.95, 14.95, 19.95, 24.95]

for x in original:
	discount = x * 0.4
	print(f"${x}			${round(discount,2)}")
