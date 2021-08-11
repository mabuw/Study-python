# Kiểu dữ liệu và biến
# I, Kiểu dữ liệu
#Datatype ( Kiểu dữ liệu ) có những loại cơ bản sau:
#string viết tắt là str() ví dụ "son" "thai"
#integer viết tắt là int ví dụ 12345
#float viết là float dùng để đo chiều cao, những dữ liệu có số thập vân như : 1.78m hay 65.3kg
#boolean viết tắt là bool có 2 giá trị là Đúng (True) Sai (False)
# II, Biến (variable viết tắt là var)
# Biến có thể thay đổi được dựa vào quá trình mình code, biến không thể đổi gọi là constant variable
# Khi code thì chương trình sẽ chạy từ trên xuống dưới

#================== Bài tập 1 ================== 
print("123") #123 là 1 số nguyên (integer), cả cụm "123" là một string(kí tự)
print("son")#Không thể đặt print(son) mà phải đặt là print("son") ví nếu không nó sẽ hiểu kí tự bên trong là 1 biến, mà bên trong dấu phải là 1 kiểu dữ liệu gì đó

#================== Bài tập 2 ================== 

firstname = "son" #firstname là biến được gán giá trị cho xâu kí tự "son" (assignment statement : mệnh đề gán giá trị)
print(firstname) #In ra biến firstname là "son"
#Lưu ý : + Khoảng trống giữa dấu cách ( = ) và giá trị có thể có hoặc không, để cho code gọn hơn vì đó là qui chuẩn
# + Tên của biến luôn luôn phải là lower case ( chữ thường), chữ hoa cũng được
# + Khi muốn cách thì phải đặt giấu gạch ngang ở giữa ( ví dụ : first_name)
#firstname có thể đặt tên khác như : ABC, abc không quan trọng miễn nó là chữ cái 
#Quy luật đặt tên biến (naming convention) : Tên lúc nào cũng phải viết liền (trong trường hợp này thì firstname phải viết liền, không được là first name)

#Lỗi : Có nhiều kiểu lỗi khác nhau NameError (Lỗi đặt tên), TypeError, SyntaxError,..

#Tiếng anh trong bài học :
#lower case : chữ thường
#upper case : Chữ hoa
#defined : Định nghĩa
#"" : quotation mark
#'' : single quotation mark
# = : gán ...
# == : ... Là ...
#unused variable : Biến không dùng ( Định nghĩa nhưng chưa dùng )
#Datatype : Kiểu dữ liệu 
#string : Kí tự
#integer : Số nguyên
#Variable : Biến
#constant variable : Biến không thể đổi
#print : in
#assignment statement : mệnh đề gán giá trị
#naming convention : Thông lệ đặt tên