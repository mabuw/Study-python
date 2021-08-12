#BÀI 3 : NHẬP THÊM TÍNH CHIỀU CAO BẰNG MÉT TÍNH RA FEET
CURRENT_YEAR = 2021 
METER_TO_FEET = 3.281 #Dòng này nghĩa là 1 mét = 3.281 feet, gán phép tính (mét) x 3,281 cho biến METER_TO_FEET

print("Nhập họ của bạn: ")
lastname = input()
#Thay vì như này mình có thể rút gọn thành
lastname = input("Nhập họ của bạn: ")

print("Nhập tên của bạn:")
firstname = input()

print("Họ và tên của bạn:" + lastname + " " + firstname)

print("Nhập năm sinh của bạn: ")
nam_sinh = input()

age = CURRENT_YEAR - int(nam_sinh) 

print("Tuổi của bạn là: " + str(age) + " vào năm " + "" + str(CURRENT_YEAR))
#Thường thì dòng này quá dài nên sẽ có cách rút gọn như sau:
print("Tuổi của {2} là: {0} vào năm {1} ".format(age,CURRENT_YEAR,firstname)) #Khi mình đang .format() nghĩa là mình đang dùng hàm format() cho dòng code, bất khi nào mình thấy dấu chấm như dòng này
#thì nó là áp dụng phần đằng sau cho phần đằng trước, format sẽ làm cho các biến trở thành kiểu dữ liệu string()
#age và CURRENT_YEAR được hiểu lần lượt là 0 và 1, như vậy code sẽ gọn hơn
#firstname là biến tên của mình đã nhập từ trước, tương ứng với số 2
print("Chiều cao của bạn (mét): ")
height_meter = float(input()) #Sau khi nhập chiều cao thì sẽ lưu vào biến height_meter
#Lỗi : TypeError (Lỗi về kiểu dữ liệu), tại vì khi không có float thì input ở dạng string, mà string thì không thể nhận và nhân với kiểu dữ liệu float là 3.281 được
#Cách khắc phục :
#Cần thêm float để nó đọc được hàng chứ thập phân
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1) #Đây là hàm dùng để làm tròn chữ số thập phân, phẩy 1 nghĩa là chỉ lấy 1 số sau dấu phẩy để hiển thị
#Cần lưu round() vào một biến rồi in biến đó ra mới chạy được
#round() là một hàm built-in function
print("\n--------------")#\n là kí tự xuống dòng (newline character)
print("Họ và tên của bạn:" + lastname + " " + firstname)
print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet") #In ra số feet sau khi tính được

#CODE HOÀN CHỈNH (ĐÃ ĐƯỢC RÚT GỌN)

CURRENT_YEAR = 2021 
METER_TO_FEET = 3.281
 
lastname = input("Nhập họ của bạn: ")
firstname = input("Nhập tên của bạn: ")
nam_sinh = input("Nhập năm sinh của bạn: ")
height_meter = float(input("Nhập chiều cao của bạn :"))

age = CURRENT_YEAR - int(nam_sinh) 
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1)

print("\n--------------")
print("Họ và tên của bạn:" + lastname + " " + firstname)
print("Tuổi của {2} là: {0} vào năm {1}".format(age,CURRENT_YEAR,firstname))
print("Chiều cao của {0} là: ".format(firstname) + str(height_feet) + " feet")


#Tiếng anh trong bài
#String format : Định dạng chuỗi
#newline character : Kí tự xuống dòng
#prompt : Nhập