#BÀI 26 : CODE RÚT GỌN LẠI CHƯƠNG TRÌNH ĐẦU TIÊN VỚI HÀM 

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

def tinhtuoi(CURRENT_YEAR, nam_sinh): 
	return CURRENT_YEAR - nam_sinh

def tinhchieucao(height_meter): #Rút gọn height_feet thành một hàm như này
	METER_TO_FEET = 3.281
	return round(height_meter * METER_TO_FEET,1) #Rút gọn luôn 2 đoạn đổi thành một dòng để return luôn

def main():
	CURRENT_YEAR = 2021 
	is_male = None
	#===================================NHẬP GIÁ TRỊ===================================
	while True:
		try:
			lastname = input("Nhập họ của bạn: ")
			firstname = input("Nhập tên của bạn: ")
			nam_sinh = int(input("Nhập năm sinh của bạn: "))
			height_meter = float(input("Nhập chiều cao của bạn :"))
			break
		except:
			print("Hãy kiếm tra lại các kí tự số và chữ, nhập sao cho đúng")
			continue

	height_feet = tinhchieucao(height_meter) #NoneType là trống rỗng
	age = tinhtuoi(CURRENT_YEAR, nam_sinh)
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