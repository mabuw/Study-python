#BÀI 29 : ĐỌC FILE TEXT, SỬ DỤNG HÀM WITH

#Hàm close để đóng file khi dùng xong cho đỡ bị xung đột giữa các file
file = open("data.txt", "w") #writing mode ( tạo file và ghi file)
file.write("a\n")
file.write("b\n")
file.close() #Đóng file data đi, mỗi lần mở thì cần có close

#Viết thêm vào file txt ở trên
file = open("data.txt", "a") #append mode ( ghi thêm vào file )
file.write("c\n")
file.write("d\n")
file.write("e")
file.close()

#Đọc file txt ở trên
file = open("data.txt", "r") #reading mode ( đọc file )
data = file.read()
print(data) #Hàm print lúc nào nó cũng tự thêm cái dấu xuống dòng ở cuối
file.close()

#Dùng hàm with để không cần close
with open("data.txt", "w") as file: #Hàm with sẽ tự tắt file sau khi dùng xong, nghĩa là bật file lên rồi chạy khối lệnh nằm trong nó rồi tắt file
	file.write("a\n")
	file.write("b\n")

#Tương đương với :

file = open("data.txt", "w") 
file.write("a\n")
file.write("b\n")
file.close() 

with open("data.txt", "a") as file: # as file nghĩa là với danh nghĩa file, file là tên biến có thể thay đổi
	file.write("c\n")
	file.write("d\n")
	file.write("e")

with open("data.txt", "r") as file:
	data = file.read()
	print(data)

#Bổ sung :
with open("data.txt", "r") as file:
	data = file.read() #Đọc file sau đó lưu vào data
	a = [data] #Chuyển data thành kiểu dữ liệu list sau đó lưu vào a
	print(a) #Đọc ra a, a = [abcde]
	#Sau khi có a thì mình sẽ có được cái gọi là index() để có thể kiểm soát được nội dung trong data của mình theo từng dòng một cách dễ dàng

#Tiếng anh trong bài :
#Operation : Thao tác
#writable viết bởi ( write ) và ( able )
#able : có thể, được
#not (..)able : Không được, không thể