#BÀI 13 : THỰC HÀNH FIX IF ELSE BUG

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
elif gender_input == "không" or (gender_input == "no") or (gender_input == "n"): #Nếu dòng này dùng if sẽ bị lỗi
#Lỗi là nếu mệnh đề if của yes mà đúng thì mềnh đề if của no sẽ sai, và if (no) với else dưới kia lại là một cụm, thành ra nó không chạy được cái if (no) thì sẽ chạy cái else
#Dẫn đến lỗi là is_male sẽ thành None
	is_male = False
else:
	is_male = None 

if is_male is None: 
	is_male = "Không rõ giới tính" 
elif is_male is True:
	if height_feet > 6.5:
		is_male = firstname + " là con trai và rất cao" 
	elif height_feet > 6.0:
		is_male = firstname + " là con trai và cao"
	else:
		is_male = firstname + " là con trai và thấp"
elif is_male is False:
	if height_feet > 5.7:
		is_male = firstname + " là con gái và cao"
	else:
		is_male = firstname + " là con gái và thấp"	
else:
	is_male = "Lỗi hệ thống, biến is_male không đúng"

#===================================IN GIÁ TRỊ===================================

print("\n--------------")
print("Họ và tên của bạn là: {0} {1}".format(lastname,firstname))
print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
print(is_male)
print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet")