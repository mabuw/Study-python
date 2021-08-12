#Học if - else, bolean

age = 23 #Gán cho biến age giá trị là 1(int)

if True: #Biến bolean, nếu biến này là True thì nó chỉ chạy đúng trong khung của 1 if đầu tiên sau đó nó sẽ dừng chương trình
#Nghĩa là chỉ cần 1 mệnh đề đúng là chương trình sẽ kết thúc

is_con_nit = False #Tức là kiểu dữ liệu của is_con_nit là False, kiểu dữ liệu bolean
#Thường nếu kiểu dữ liệu là bolean thì nó sẽ đặt chứ is ở đầu biến
#is_con_nit là giá trị defaut (mặc định) từ đầu chương trình và là một initialise the variable
#is_con_nit = False là đang gán giá trị False cho biến is_con_nit
if age < 10:

if False: #Nếu if là False thì nó sẽ bỏ qua phần if đầu tiên ( trong trường hợp này là dòng " con nít") nó sẽ chạy các mệnh đề còn lại
	print("con nít")

if not is_con_nit #If not sẽ ngược lại với True hoặc False ví dụ is_con_nit là True thì if not sẽ là False và ngược lại

elif (age < 18):
	print("Trẻ trâu")
	if age <= 15 and age >= 11:
		print("Siêu trẻ trâu")
else:
	print("Người lớn")

#Giải thích rõ hơn về bolean trong trường hợp này

age = 8
is_con_nit = False#=> Chưa hoạt động
 #Mặc định gán cho is_con_nit là False, tức là chưa hoạt động(False)

if age < 10: #Nếu tuổi nhỏ hơn 10 thì is_con_nit sẽ trở thành True và sẽ hoạt động dưới các dòng lệnh tiếp theo
	is_con_nit = True #=> Đã hoạt động

if is_con_nit: #Nếu is_con_nit là False thì dòng này là False, nếu là True thì là True
#Dòng này tương đương với if True:
	print("con nít")#Nếu is_con_nit mà True thì nó sẽ chạy dòng này, còn False thì nó sẽ xem xét tiếp dưới dòng tiếp theo

#CODE HOÀN CHỈNH TRONG BÀI
age = 8
is_con_nit = False

if age < 10:
	is_con_nit = True

if is_con_nit:
	print("con nít")
elif age == 18: #So sánh 2 giá trị hay con gọi là "là"
	print("18 tuổi")
elif (age < 18):
	print("Trẻ trâu")
	if age <= 15 and age >= 11:
		print("Siêu trẻ trâu")
else:
	print("Người lớn")
#Tiếng anh trong bài
#conditional statement : Câu lệnh điều kiện
#comparison statement : Mệnh đề so sánh
#initialise the variable : Khởi tạo biến
#defaut : Mặc định
#inconsisten : Không đồng bộ
#indentation : Thụt đầu dòng
#SyntaxError : Lỗi cú pháp
#invalid : Không hiệu lực
#syntax : cú pháp