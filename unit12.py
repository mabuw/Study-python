#WHILE LOOP (VÒNG LẶP WHILE)

i = 0 # Đối với while thì bao giờ cũng phải khởi tạo giá trị ban đầu là i = 0 trước
while i < 5: #While nghĩa là khi mà, i < 5 là một mệnh đề
	print(i)
	i = i + 1 #Khi chạy while thì luôn luôn phải có i + 1
#Sau khi chạy hết code ở trong mệnh đề while thì nó sẽ quay lại while để check xem điều kiện có đúng hay không
#i < 5 là điều kiện, nghĩa là chỉ khi nào điều kiện vẫn thỏa mãn thì code vẫn chạy
#Nếu i > 5 thì vòng lặp sẽ ngừng
#Vấn đề là mình phải làm cho mệnh đề bên trong vòng lặp While sẽ có lúc nào đó sẽ sai điều kiện để kết thúc vòng lặp không thì nó sẽ chạy mãi


#Hoặc có thể thoát vòng lặp bằng : 
			break
#THOÁT VÒNG LẶP BẰNG BREAK
i = 0
while i < 10: #điều kiện để i luôn True là nhỏ hơn 10, nếu lớn hơn 10 điều kiện sẽ False và dừng vòng lặp
	if i == 5: #Đây là nếu i là 5 thì sẽ break
		break #break Phải lùi vào dầu dòng vì nằm trong mệnh đề if
	print(i)
	i = i + 1
#Viết tắt i = i + 1 là :
	i += 1

#VÒNG LẶP VÔ HẠN (TỨC LÀ WHILE LUÔN ĐÚNG (TRUE))
i = 0

while True: #While sẽ luôn đúng, trừ khi có điều kiện khiến while thành False
	print(i)
	i += 1

#IN RA CHƯƠNG TRÌNH GỒM SỐ 9,7,5,3,1
i = -1

while i <= 8:
	i += 2
	print(10 - i)

#IN RA CHƯƠNG TRÌNH GỒM SỐ 0,2,4,6,8
i = 0
print(i)
while i < 10:
	i += 2
	if i == 10:
		continue
	print(i)


#TIẾNG ANH TRONG BÀI
#infinity loop : Vòng lặp vô hạn
#initialise : Khởi tạo