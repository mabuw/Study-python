#VÒNG LẶP FOR LOOP

for i in range(5): #i là một biến, range tiếng anh nghĩa là khoảng, và khoảng từ 0 đến 5 trong trường hợp này
#Ý nghĩa : Nó sẽ chạy i trong khoảng từ 0 đến 5
#Có thể rút gọn range(0,5) thành range(5)
	print(i)# i sẽ in ra giá trị từ 0 đến 4 (0,1,2,3,4 => đủ 5 giá trị)

#Giải thích logic:
# Nó sẽ chạy lần lượt là i = 0, i = 1, i = 2, i = 3, i = 4
# Sau mỗi lần chạy như vậy thì các mệnh đề nằm trong đó cũng sẽ chạy với số lần tương đương
#Trong trường hợp này là print(i) như vậy là 0,1,2,3,4

#IN CHƯƠNG TRÌNH 5, 4, 3, 2, 1
for i in range(5):
	print(5 - i)

#Giải thích logic : i sẽ chạy từ 0 đến 4 là : i = 0, i = 1, i = 2, i = 3, i = 4
#Giá trị đầu tiên sẽ là 0, vậy : 5 - 0 = 5
#Giá trị thứ 2 sẽ là 1, vậy 5 - 1 = 4
#Áp dụng đối với các giá trị còn lại
#Như vậy đáp án là : 5,4,3,2,1

#IN CHƯƠNG TRÌNH BAO GỒM CÁC SỐ CHẴN : 0, 2, 4, 6, 8
for i in range(5):
	print(2 * i)

#Giải thích logic :
#i sẽ in lần lượt là i = 0, = 1, = 2, = 3, = 4
#và sẽ nhân với 2 lần lượt là 2*0, 2*1, 2*2, 2*3, 2*4
#Suy ra kết quả là 0, 2, 4, 6, 8

#IN CHƯƠNG TRÌNH BAO GỒM CÁC SỐ LẺ : 1, 3, 5, 7, 9
for i in range(5):
	print(2 * i + 1)

#Giải thích logic :
#i sẽ in lần lượt là i = 0, = 1, = 2, = 3, = 4
#và sẽ nhân với 2 lần lượt là 2 * 0 + 1, 2 * 1 + 1, 2 * 2 + 1, 2 * 3 + 1, 2 * 4 + 1
#Suy ra kết quả là 1, 3, 5, 7, 9, 0

for i in range(0,5,3): #Trong trường hợp này, nó sẽ chỉ chạy nhừng số chia hết cho 3 mà nhỏ hơn 5 ví dụ như 0 và 3
	print(i)