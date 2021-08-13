#FOR LOOP IN FOR LOOP ( VÒNG LẶP FOR TRONG FOR)

for i in range(0,2): #i = 0
	print(i) #In ra giá trị = 0
	for j in range(3,5): #Cái j này lặp xong chu kì của nó mới quay lại lặp của i
		print(j) #Ví dụ khoảng 3 đến 5, thì nó sẽ chạy print(3) rồi print(4) sau đó mới quay lại tăng giá trị i = 1

#GIẢI THÍCH RÕ HƠN
i = 0
for j in range(3,5):
		print(j) #In ra 3 và 4

i = 1
for j in range(3,5):
		print(j)#In ra 3 và 4


#Tiếng anh trong bài
#nested loop : Loop trong Loop