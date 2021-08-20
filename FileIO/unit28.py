#BÀI 28 : TẠO VÀ CHẠY FILEIO ( INPUT - OUTPUT )

file = open("data.txt", "w") #Gán cho biến file giá trị của hàm open(), nghĩa là mở file data.txt
#Các mode trong FileIO ( chữ "w" được gọi là mode) ( Chỉ được ở 1 trong các mode, không thể nào chạy 2 mode cùng lúc )
#"w" tức là writting ( Tạo file, xóa file cũ, nếu tên của nó trùng nhau) (mode w sẽ tạo 1 file mới và xóa file cũ và ghi nội dùng vào file mới)
#"r" tức là reading ( đọc file)
#"a" tức là append ( mở và ghi tiếp tục lên nội dung của file ) ( mở file và ghi tiếp vào nội dung trong file )
#Kiểu dữ liệu của file là file

file.write("Son Linh") #Viết string vào file
#Hàm write chỉ được ghi kiểu dữ liệu string, không phải integer hay float

#Đọc file txt
file = open("data.txt", "r") #Đầu tiên là mở file data với chế độ r

data = file.read() #Rồi sau đó file.read để đọc rồi lưu vào giá trị đã đọc được vào biến data
print(data)# In data ra giá trị
#Kết luận: Muốn đọc 1 file trước hết phải đổi nó sang mode r và có (tên biến).read

#Thường sau dấu chấm là một hành động gì đó hoặc thuộc tính ví dụ file.read, sau dấu chấm sẽ là đọc, còn trước dấu chấm sẽ là vật thể hoặc biến 


#Tiếng anh trong bài:
#configuration : Tùy chỉnh