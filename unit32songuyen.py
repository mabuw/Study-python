n = int(input("Nhập số nguyên N : "))

with open("data.txt", "w") as file:
	for i in range(n):
		file.write(str(n - i) + "\n")

number = []
with open("data.txt", "r") as file:
	data = file.read().split("\n")
for i in range(len(number)):
	print("Line " + str(i + 1) + ": " + data[i])
