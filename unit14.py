#BÀI 14 : THỰC HÀNH VÒNG LẶP WHILE FOR LOOP

#===================================KHAI BÁO BIẾN===================================

CURRENT_YEAR = 2021 
METER_TO_FEET = 3.281
is_male = None

#===================================NHẬP GIÁ TRỊ===================================

lastname = input("Nhập họ của bạn: ")
firstname = input("Nhập tên của bạn: ")
nam_sinh = input("Nhập năm sinh của bạn: ")
height_meter = float(input("Nhập chiều cao của bạn :"))
gender_input = input("Bạn có phải con trai không (có/không): ")

age = CURRENT_YEAR - int(nam_sinh) 
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1)
#===================================XỬ LÍ DỮ LIỆU===================================

if (gender_input == "có") or (gender_input == "yes") or (gender_input == "y"):
	is_male = True
elif gender_input == "không" or (gender_input == "no") or (gender_input == "n"): 
	is_male = False
else:
	is_male = None 

if is_male is None: 
	print(firstname + "Không rõ giới tính" )
elif is_male is True:
	if height_feet > 6.5:
#ĐỀ BÀI: IN RA 10 LẦN TỪ VERY ( RẤT CAO) BẰNG FOR
		
		### ================CÁCH 1================

		print(firstname + " là con trai và" )
		print(" rất " * 10) #In ra 10 lần "rất", dấu nhân ở đây được hiểu là 10 lần từ rất, nhưng xuống dòng
		print("cao")
		### ======================================

		### ================CÁCH 2================

		print(firstname + " là con trai và" + " rất" * 10 + " cao"  ) #In ra 10 lần "rất", dấu nhân ở đây được hiểu là 10 lần từ rất, nhưng ở cùng một dòng

		### ======================================

		### ================CÁCH 3================

		print(firstname + "là con trai và ", end='' )# end ở đây dùng để xóa từ \n, nghĩa là sẽ không xuống dòng nữa
		for i in range(10):
			print(" rất ",end='') #In ra 10 lần từ rất, khi i = 0 thì in ra 1 lần, i = 1 tiếp tục in
		print("cao")

#ĐỀ BÀI: IN RA 5 LẦN TỪ VERY ( RẤT CAO) BẰNG WHILE
	### ======================================

		print(firstname + " là con trai và ", end='' )
		i = 0
		while i < 5: #I sẽ lại lặp và + 1 đến khi nào i không còn < 5 nữa thì kết thúc vòng lặp
			print("rất ", end='') # Lặp từ rất ra 5 lần, đầu tiên i = 0 lặp 1 từ rất, sau đó + 1, rồi i = 1 lặp 1 từ rất và cứ thế đến khi kết thúc vòng lặp
			i += 1 #Điều kiện tiên quyết để kết thúc vòng lặp
		print("cao")

	### ======================================

	elif height_feet > 6.0:
		print(firstname + " là con trai và cao")
	else:
		print(firstname + " là con trai và thấp")
elif is_male is False:
	if height_feet > 5.7:
		print(firstname + " là con gái và cao")
	else:
		print(firstname + " là con gái và thấp")	
else:
	 print("Lỗi hệ thống, biến is_male không đúng")

#===================================IN GIÁ TRỊ===================================

print("\n--------------")
print("Họ và tên của bạn là: {0} {1}".format(lastname,firstname))
print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet")