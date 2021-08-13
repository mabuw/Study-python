#LUYỆN TẬP VỚI AND OR BOLEAN

CURRENT_YEAR = 2021 
METER_TO_FEET = 3.281
is_male = None

lastname = input("Nhập họ của bạn: ")
firstname = input("Nhập tên của bạn: ")
nam_sinh = input("Nhập năm sinh của bạn: ")
height_meter = float(input("Nhập chiều cao của bạn :"))
gender_input = input("Bạn có phải con trai không (có/không): ")

#ĐOẠN NÀY LÀ QUY ĐỔI GIÁ TRỊ TỪ STRING(INPUT) SANG BOLEAN

if (gender_input == "có") or (gender_input == "yes") or (gender_input == "y"): #Trường hợp này là ví dụ của or : Chỉ cần một điều kiện đúng,tức nghĩa là người dùng nhập 1 trong 3 cái
# thì mệnh đề sẽ đúng và chương trình sẽ chạy tiếp
	is_male = True
elif gender_input == "không" or (gender_input == "no") or (gender_input == "n"): #Tương tự như dòng yes
	is_male = False
else:
	is_male = None #Gán giá trị is_male là None

#==============================================================

if is_male == None: #So sánh is_male với None
#Thay vì == chúng ta có thể thay là is
if is_male is None: #Ví dụ
	print("Không rõ giới tính") #Nếu is_male là None sẽ in ra dòng này
elif is_male is True:
	if height_feet > 6.5: #Logic của dòng này là nó sẽ check > 6.5 trước, nếu sai thì nó sẽ check xuống dòng tiếp theo là > 6.0
		print("Bạn là con trai và rất cao") 
	elif height_feet > 6.0:#Chỉ cần 1 mệnh đề đúng là tất cả mệnh đề if, elif sẽ bị hủy và chương trình sẽ chạy
		print("Bạn là con trai và cao")
	else:
		print("Bạn là con trai và thấp")
elif is_male is False:
	if height_feet > 5.7:
		print("Bạn là con gái và cao")
	else:
		print("Bạn là con gái và thấp")	
else:
	print("Lỗi hệ thống, biến 'is_male' không đúng")#Trường hợp này là dành cho biến is_male không phải kiểu dữ liệu Bolean	
#Khi dùng dấu nháy ở trong một string() thì ta nên dùng dấu nháy đơn
#Trường hợp này là dấu nháy đơn bên trong dấu nháy kép

#==============================================================

age = CURRENT_YEAR - int(nam_sinh) 
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1)

print("\n--------------")
print("Họ và tên của bạn:" + lastname + " " + firstname)
print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
print(is_male)
print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet")

#CHƯƠNG TRÌNH HOÀN CHỈNH TRONG BÀI

CURRENT_YEAR = 2021 
METER_TO_FEET = 3.281
is_male = None

lastname = input("Nhập họ của bạn: ")
firstname = input("Nhập tên của bạn: ")
nam_sinh = input("Nhập năm sinh của bạn: ")
height_meter = float(input("Nhập chiều cao của bạn :"))
gender_input = input("Bạn có phải con trai không (có/không): ")

age = CURRENT_YEAR - int(nam_sinh) 
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1)

#=============================================================

if (gender_input == "có") or (gender_input == "yes") or (gender_input == "y"):
	is_male = True
elif gender_input == "không" or (gender_input == "no") or (gender_input == "n"):
	is_male = False
else:
	is_male = None 

#=============================================================

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
	print("Lỗi hệ thống, biến is_male không đúng")	

#=============================================================

print("\n--------------")
print("Họ và tên của bạn là: {0} {1}".format(lastname,firstname))
print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
print(is_male)
print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet")

#Dùng phím tắt Ctrl + / để comment dòng mà bạn bôi đen