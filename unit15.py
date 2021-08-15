#BÀI 15 : SỬ DỤNG VÒNG LẶP WHILE VÀ TRUE - BREAK ĐỂ BẮT NGƯỜI DÙNG NHẬP LẠI KHI NHẬP SAI
#HỌC VỀ LIST

#===================================KHAI BÁO BIẾN===================================

CURRENT_YEAR = 2021 
METER_TO_FEET = 3.281
is_male = None
i = 0

#===================================NHẬP GIÁ TRỊ===================================

lastname = input("Nhập họ của bạn: ")
firstname = input("Nhập tên của bạn: ")
nam_sinh = input("Nhập năm sinh của bạn: ")
height_meter = float(input("Nhập chiều cao của bạn :"))

while True: #While sẽ luôn đúng và luôn lặp lại đến khi nào người dùng nhập đúng các kí tự của gender_input đề ra thì mới break

	gender_input = input("Bạn có phải con trai không (có/không): ")

	age = CURRENT_YEAR - int(nam_sinh) 
	height_feet = height_meter * METER_TO_FEET
	height_feet = round(height_feet,1)

#===================================XỬ LÍ DỮ LIỆU===================================

#HỌC LIST

	answer_yes = ["có", "yes", "y"] #List answer được gán giá trị bao gồm những kí tự trong ngoặc []

	#Dòng này tương đương với if (gender_input == "có") or (gender_input == "yes") or (gender_input == "y"):
	
	answer_no = ["không" "no", "n" ] #Phải thụt lề vào để coi như trong vòng lặp, không sẽ bị lỗi 

	if gender_input in answer_yes : #Nó sẽ so sánh với toàn bộ list answer_yes, nếu kí tự bên trong đúng thì mệnh đề đúng
		is_male = True
		break #Khi người dùng nhập đúng thì sẽ break ra khỏi vòng lặp và tiếp tục chạy phần code ngoài vòng lặp ở dưới
	elif gender_input in answer_no : #Nó sẽ so sánh với toàn bộ list answer_no, nếu kí tự bên trong đúng thì mệnh đề đúng
		is_male = False
		break #Khi người dùng nhập đúng thì sẽ break ra khỏi vòng lặp và tiếp tục chạy phần code ngoài vòng lặp ở dưới
	else:
		print(firstname + " nhập giới tính sai hãy nhập lại") #Dòng này là khi người dùng nhập các kí tự không trong gender_input == 
		continue #Skip phần dưới, tiếp tục lặp

#===================================IN GIÁ TRỊ===================================

print("\n--------------")
print("Họ và tên của bạn là: {0} {1}".format(lastname,firstname))
print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet")

if is_male is True:
	if height_feet > 6.5:
		print(firstname + " là con trai và ", end='' )
		for i in range(5):
			print("rất ", end='')
		print("cao")
	elif height_feet > 6.0:
		print(firstname + " là con trai và cao")
	else:
		print(firstname + " là con trai và thấp")
elif is_male is False:
	if height_feet > 5.7:
		print(firstname + " là con gái và cao")
	elif height_feet < 5.0:
		print(firstname + " là con gái và ", end='')	
		while i < 5:
			print("rất ", end='')
			i += 1
		print("thấp")
	else:
		print(firstname + " là con gái và thấp")
else:
	print("Lỗi hệ thống, biến is_male không đúng")