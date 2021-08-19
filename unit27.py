#BÀI 27 : RÚT GỌN CODE VỚI HÀM ĐÃ HỌC
import datetime 
now = datetime.datetime.now()

def hoi_thong_tin(): #Rút gọn nốt cái hỏi người dùng thành 1 hàm
	while True:
		try:
			lastname = input("Nhập họ của bạn: ")
			firstname = input("Nhập tên của bạn: ")
			nam_sinh = int(input("Nhập năm sinh của bạn: "))
			height_meter = float(input("Nhập chiều cao của bạn :"))
			is_male = co_hoac_khong(firstname,"Bạn có phải con trai không (có/không): ") #Nó sẽ chạy cái hàm main rồi hàm này trước nên chạy được hàm co_hoac_khong
			is_vietnamese = co_hoac_khong(firstname,"Bạn có phải người Việt không (có/không): ") 
			break
		except:
			print("Hãy kiếm tra lại các kí tự số và chữ, nhập sao cho đúng")
			continue	
	return lastname, firstname, nam_sinh, height_meter, is_male, is_vietnamese #Return nhiều giá trị cùng 1 lúc

def co_hoac_khong(firstname, prompt):
	while True: 
		answer_yes = ["có", "yes", "y"] 
		answer_no = ["không", "no", "n"]
		gender_input = input(prompt)

		if gender_input.lower() in answer_yes : 
			return True 
		elif gender_input.lower() in answer_no : 
			return False
		else:
			print(firstname + " nhập giới tính/đất nước sai hãy nhập lại") 
			continue 

def very(): #Thay vòng lặp rất bằng 1 hàm và dùng nó cho gọn
	rat = "rất " * 5 #Không cần vòng lặp nữa
	return rat

def tinh_chieucao_va_tuoi(height_meter,CURRENT_YEAR, nam_sinh): 
	METER_TO_FEET = 3.281
	return round(height_meter * METER_TO_FEET,1), (CURRENT_YEAR - nam_sinh) #Đoạn này rút gọn hơn nữa bằng cách 1 return trả 2 giá trị

def in_thong_tin(lastname, firstname, age, CURRENT_YEAR, height_feet, is_vietnamese, is_male): #Rút gọn phần này riêng biệt ra cái nào in cái nào so sánh, để lúc sửa code không cần phải tìm nhiều
	print("\n--------------")
	print("Họ và tên của bạn là: {0} {1}".format(lastname,firstname))
	print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
	print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet")
	in_chieu_cao_va_region(height_feet, is_vietnamese, firstname, is_male) #Gọi hàm trong hàm và gọi 2 hàm ra 1 hàm main

def in_chieu_cao_va_region(height_feet, is_vietnamese, firstname, is_male):
	if is_vietnamese: 
		print(firstname + " Là người Việt Nam number one")
	else:
		print(firstname + " Là người ngoại quốc")

	if is_male is True:
		if height_feet > 6.5:
			print(firstname + " là con trai và", very(), "cao" ) #Dùng hàm vòng lặp rất
		elif height_feet > 6.0:
			print(firstname + " là con trai và cao")
		else:
			print(firstname + " là con trai và thấp")
	elif is_male is False:
		if height_feet > 5.7:
			print(firstname + " là con gái và cao")
		elif height_feet < 5.0:
			print(firstname + " là con gái và",very(), "thấp")	
		else:
			print(firstname + " là con gái và thấp")
	else:
		print("Lỗi hệ thống, biến is_male không đúng")

def main():
	CURRENT_YEAR = now.year
	lastname, firstname, nam_sinh, height_meter, is_male, is_vietnamese = hoi_thong_tin() #Các giá trị được return sẽ được gán lần lượt từ trái sang phải
	height_feet, age = tinh_chieucao_va_tuoi(height_meter, CURRENT_YEAR, nam_sinh) #Giá trị được trả sẽ gắn lần lượt từ trái sang phải
	in_thong_tin(lastname, firstname, age, CURRENT_YEAR, height_feet, is_vietnamese, is_male)

main()

#TIẾNG ANH TRONG BÀI
#consistent : Đồng bộ
#condense : Cô đặc 