#THỰC HÀNH VỚI BIẾN BOLEAN TRONG PHẦN GIỚI TÍNH

CURRENT_YEAR = 2021 
METER_TO_FEET = 3.281
is_male = None

lastname = input("Nhập họ của bạn: ")
firstname = input("Nhập tên của bạn: ")
nam_sinh = input("Nhập năm sinh của bạn: ")
height_meter = float(input("Nhập chiều cao của bạn :"))

#==============================Phần thực hành==============================
gender_input = input("Bạn có phải con trai không (có/không): ")

if gender_input == "có":
	is_male = True
elif gender_input == "không":
	is_male = False
else:
	is_male = None #Tất cả True False và None đều là 3 keyworld khác nhau

if is_male == True:
	is_male = firstname + " là con trai"
elif is_male == False:
	is_male = firstname + " là con gái"
else:
	is_male = "Không rõ giới tính của: " + firstname

#==============================PHẦN THỰC HÀNH==============================
age = CURRENT_YEAR - int(nam_sinh) 
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1)

print("\n--------------")
print("Họ và tên của bạn:" + lastname + " " + firstname)
print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
print(is_male)
print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet")