#BÀI 20 : HÀM MAIN,GLOBAL VÀ LOCAL VARIABLE

#GLOBAL VARIABLE : Biến mà có thể sử dụng xuyên suốt chương trình
#LOCAL VARIABLE : Biến mà chỉ có thể sử dụng ở một khu vực như hàm
#MAIN FUNCTION : Không nên đặt chương trình rời rạc như ở dưới mà phải luôn luôn gói gọn trong hàm MAIN
#Hàm cần phải được định nghĩa trước khi gọi, nghĩa là câu lệnh gọi hàm luôn luôn phải ở dưới hàm
#TẤT CẢ NHỮNG GÌ TRONG CHƯƠNG TRÌNH MÌNH CHẠY THÌ LUÔN LUÔN SẼ BẮT ĐẦU TỪ HÀM MAIN

def hocsinh_A():
	print("Học sinh A:")
	print("Toán : 9")
	print("Văn : 6")

def hocsinh_B():
	print("Học sinh B:")
	print("Toán : 5")
	print("Văn : 7")

hocsinh_A()
hocsinh_B()

#Mọi chương trình bình thường nếu cần hàm thì đều bắt đầu từ hàm main trước
#Mỗi khi code 1 chương trình thì luôn luôn bắt đầu như này : 

def main():#Tức là luôn luôn sẽ có hàm main, cả chương trình của mình sẽ chỉ gọi đúng một hàm
	hocsinh_A() #Hàm main có thể gọi được các hàm khác ở trong nó, rồi gọi hàm main ra để in giá trị của cả các hàm khác
	hocsinh_B() #Các hàm này sẽ không cần phải gọi ở đầu mà có thể ở bất cứ đâu, giống như hàm MAIN sẽ call tất cả hàm về 1 chỗ và chạy nó
#Hàm main không cần phải đặt tên chuẩn là main mà chỉ cần hiểu nó là một hàm chính của tất cả các hàm, giống như sếp và nhân viên
main()

#Mỗi hàm tượng trưng cho 1 chương trình, chỉ nên dùng local variable ở trong khối lệnh của hàm để bao bọc lấy chính nó, hạn chế sử dụng global variable

#CHƯƠNG TRÌNH HOÀN CHỈNH VỀ HÀM MAIN 
def main():
    hocsinh_A()
    hocsinh_B()

def hocsinh_A():
    print("Học sinh A:")
    print("Toán : 9")
    print("Văn : 6")

def hocsinh_B():
    print("Học sinh B:")
    print("Toán : 5")
    print("Văn : 7")

main()

#VÍ DỤ VỀ BIẾN CỤC BỘ

def hocsinh_A():
	a = "Sơn" #Biến này chỉ được dùng trong hàm hocsinh_A chứ không thể dùng ra ngoài hoặc cho hàm khác, như vậy gọi là biến cục bộ
    print("Học sinh:", a)
    print("Toán : 9")
    print("Văn : 6")


