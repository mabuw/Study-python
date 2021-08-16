#TÌM HIỂU VỀ HÀM (FUNCTION)

#Hàm có thể viết là function()
#Hàm giống như 1 khối code , có thể lập trình sẵn để gọi ra bất cứ khi nào bạn muốn trong chương trình
#Nghĩa là 1 khối code được dùng đi dùng lại nhưng chỉ cần gọi bằng functine() là nó sẽ thực hiện khối code đấy ở bất cứ đâu trong chương trình
#Mục đích : Chia chương trình ra nhiều phần và nhiều bước khác nhau
#Bước 1 : Bạn nhập giá trị cho function() gọi là input
#Bước 2 : Function cho ra một cái gọi là output

def function(): #Đây là cấu trúc của một function (hàm)
	pass 

#def viết tắt cho define (định nghĩa), tức là định nghĩa 1 function	
#function trên đoạn code nghĩa là tên hàm, có thể đổi thành bất cứ tên gì

def print_number(): #print_number là tên hàm, lúc nào cũng phải ghi liền như : print_number() chứ không được print_number ()
#quy tắc đặt tên của function giống với variable
	print(1)
	print(2)
	print(3)
#Ở trên mới chỉ định nghĩa hàm chứ chưa gọi nó
print_number() #Đây là bước gọi hàm

#Quy trình :
#Chương trình sẽ không chạy những lệnh nào nằm trong khối def mà nó sẽ chạy những cái ở ngoài, nghĩa là đây chỉ là bước định nghĩa chứ không phải in giá trị
#Tức là trường hợp này nó sẽ chạy print_number() trước sau đó mới tìm đến hàm xem nó đã được định nghĩa chưa ( chạy ngược )
#def giống như một lệnh tĩnh, khi có kích hoạt mới chạy\

#Điểm hay của hàm là có thể gọi nó liên tục :

def print_number():
	print(1)
	print(2)
	print(3)

def print_letter():
	print("a")
	print("b")
	print("c")

print_number()
print_number()
print_number()
print_number()

#=============================

def print_letter(abc): #abc chính là input mình cho vào trong
	print("a")
	print("b")
	print("c")

#TIẾNG ANH TRONG BÀI
#parameter viết tắt là param : Tham số
#argument : Đối số
#return value : Trả về giá trị
#procedure : Quy trình