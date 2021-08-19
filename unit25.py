#BÀI 25 : CODE RÚT GỌN LẠI CHƯƠNG TRÌNH ĐẦU TIÊN VỚI HÀM 

def cohoackhong(firstname, prompt):
	while True: 
		answer_yes = ["có", "yes", "y"] 
		answer_no = ["không", "no", "n" ]
		gender_input = input(prompt)

		if gender_input.lower() in answer_yes : 
			return True 
		elif gender_input.lower() in answer_no : 
			return False
		else:
			print(firstname + " nhập giới tính/đất nước sai hãy nhập lại") 
			continue 

def tinhtuoi_va_chieucao(CURRENT_YEAR, nam_sinh): #Bài này rút gọn hàm tính tuổi 
	return CURRENT_YEAR - int(nam_sinh) 

def main():

	CURRENT_YEAR = 2021 
	METER_TO_FEET = 3.281
	is_male = None
	i = 0

	#===================================NHẬP GIÁ TRỊ===================================

	lastname = input("Nhập họ của bạn: ")
	firstname = input("Nhập tên của bạn: ")
	nam_sinh = input("Nhập năm sinh của bạn: ")
	height_meter = float(input("Nhập chiều cao của bạn :"))
	height_feet = height_meter * METER_TO_FEET
	height_feet = round(height_feet,1)

	age = tinhtuoi_va_chieucao(CURRENT_YEAR, nam_sinh)
	is_male = cohoackhong(firstname,"Bạn có phải con trai không (có/không): ")
	is_vietnamese = cohoackhong(firstname,"Bạn có phải người Việt không (có/không): ") 

	#===================================IN GIÁ TRỊ===================================

	print("\n--------------")
	print("Họ và tên của bạn là: {0} {1}".format(lastname,firstname))
	print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
	print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet")

	if is_vietnamese: 
		print(firstname + " Là người Việt Nam number one")
	else:
		print(firstname + " Là người ngoại quốc")

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

main()