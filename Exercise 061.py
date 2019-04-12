inputs = 0
total = 0
print("Continue inputting numbers. Input -1 to stop.")
while True:
	add = float(input("Num: "))
	if add == -1:
		break
	else:
		inputs += 1
		total += add

average = total / inputs

print(f"Average: {average}")
