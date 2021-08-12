input() #Hàm (function) dùng để nhập thứ gì đó từ bàn phím
#input là một hàm có sẵn (built-in function)

print("Nhap ten cua ban: ")
a = input() #Lưu hàm vào biến a nhưng chưa sử dụng, khi mình nhập cái gì vào input thì nó sẽ gán giá trị cho biến a
print(a) # Sử dụng biến a
print("" + a) #"" là một string, 2 string có thể nối lại với nhau, a là string được nhập từ bàn phím vì input() luôn mặc định là 1 string
#Khi nối 2 cái trong print(... + ...) thì phải cùng kiểu dữ liệu với nhau như print("Son" + a), integer với integer ( cộng 2 số với nhau), string với string ( ghép 2 kí tự với nhau)

print("Nhập tên của bạn:") #Tên
firstname = input() 

print("Nhập họ của bạn:") #Họ
lastname = input()

print("Họ và tên của bạn: " + firstname + " " + lastname) #In ra cả họ và tên, " " là dấu cách ở giữa 
#Hàm input luôn luôn trả về dạng string, vậy nên nhập số nó vẫn sẽ hiểu là string chứ không phải integer

#Viết một chương trình tính tuổi hiện tại của bản thân  (chương trình này lỗi)

CURRENT_YEAR = 2021 #Những biến không đổi (constant variable) luôn phải đặt tên in hoa, những biến không đổi thường là dùng mặc định cho 1 chương trình
 
print("Nhập họ của bạn: ")
lastname = input()

print("Nhập tên của bạn:")
firstname = input()

print("Nhập năm sinh của bạn: ")
nam_sinh = input() #Tên thường là những từ khóa chứ không cần phải có nghĩa ( cách đặt tên cho biến)

age = CURRENT_YEAR - nam_sinh #Biến age (tuổi) được định nghĩa là Năm hiện tại (CURRENT_YEAR) trừ đi năm sinh

print("Tuổi của bạn là: " + age)

#Lỗi TypeError, vì CURRENT_YEAR = 2021, Python sẽ hiểu là một kiểu số nguyên(int), và nam_sinh sẽ được hiểu là một string vì ở trong "" và 2 cái là kiểu dữ liệu khác nhau
#cho nên sẽ không thể tính được bằng phép trừ, str() cant - int()
#Cách sửa lỗi : Chỉnh nam_sinh thành một kiểu dữ liệu số nguyên(int), khi đó python sẽ hiểu là 2 số nguyên trừ cho nhau 

age = CURRENT_YEAR - int(nam_sinh) #Tuy nhiên nó sẽ chỉ hiểu nam_sinh là số nguyên(int) ở dòng này, khi dùng dòng code khác thì nó sẽ lại là string()

#Cách sửa khác :

nam_sinh = int(input()) #Sẽ chuyển nam_sinh là số nguyên(int) cho cả chương trình vế sau
#hoặc
nam_sinh = int(nam_sinh) #Cách này sẽ đổi một kiểu string sang kiểu integer(số nguyên)
#Giải thích: Nghĩa là sẽ đổi vế bên phải thành kiểu integer và gán vào biến nam_sinh

#CHƯƠNG TRÌNH HOÀN CHỈNH TRONG BÀI HỌC

CURRENT_YEAR = 2021 
 
print("Nhập họ của bạn: ")
lastname = input()

print("Nhập tên của bạn:")
firstname = input()

print("Họ và tên của bạn:" + lastname + " " + firstname)

print("Nhập năm sinh của bạn: ")
nam_sinh = input()

age = CURRENT_YEAR - int(nam_sinh) 

print("Tuổi của bạn là: " + str(age) + " vào năm " + "" + str(CURRENT_YEAR))

#Tiếng anh trong bài học :
#concatenate : Nối 
#String concatenation : Nối string lại với nhau
#function : Hàm
#input : Nhập
#built-in function : Hàm có sẵn
#unsupported : Không hỗ trợ
#operand : Các phép tính (toán tử)
#type(s) : Kiểu, thêm(s) là nhiều kiểu
#overwrite : Viết đè