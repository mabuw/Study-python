#BÀI 21 : THỰC HÀNH VỚI GLOBAL LOCAL VARIABLE VÀ MAIN FUNCTION

def main():
    # ten_hocsinh_A = "Son" #Đây là một biến local mà chỉ trong hàm main mới có thể sử dụng
    ten_hocsinh_B = "Linh"
    hocsinh_A()
    hocsinh_B()

def hocsinh_A():
    print("Học sinh A:")
    print("Tên : " + ten_hocsinh_A) #Lúc này chạy sẽ không được vì ten_hocsinh_A chưa được định nghĩa trong hàm hocsinh_A
    #Thứ 2 là ten_hocsinh_A không phải một global variable 
    print("Toán : 9")
    print("Văn : 6")

#ĐỊNH NGHĨA LOCAL VARIABLE TRONG HOCSINH_A
def hocsinh_A():
    ten_hocsinh_A = "Son" #Đây mới là định nghĩa một local variable để dùng trong hàm ten_hocsinh_A
    print("Học sinh A:")
    print("Tên : " + ten_hocsinh_A) 
    print("Văn : 6")


def hocsinh_B():
    print("Học sinh B:")
    print("Toán : 5")
    print("Văn : 7")

ten_hocsinh_A = "Son" # Muốn sử dụng biến này trong tất cả các hàm thì mình phải đặt ngoài đây, gọi là global variable

#SỬ DỤNG PARAMETER ( THAM SỐ ) ĐỂ TRUYỀN DỮ LIỆU VÀO CHO MỘT HÀM

def main():
    ten_hocsinh_A = "Son" #Đây là một biến local mà chỉ trong hàm main mới có thể sử dụng
    ten_hocsinh_B = "Linh"
    hocsinh_A(ten_hocsinh_A) #Đoạn này có nghĩa là mình truyền giá trị của biến ten_hocsinh_A ( Hiện là "Sơn") vào trong hàm hocsinh_A để sử dụng nó
    hocsinh_B(ten_hocsinh_B) #Học sinh B cũng tương tự như A là được truyền giá trị của biến vào để sử dụng

def hocsinh_A(name): #Sử dụng argument để truyền vào
    print("Học sinh A:")
    print("Tên : " + name)
    print("Toán : 9")
    print("Văn : 6")

def hocsinh_B(name):
    print("Học sinh B:" + name) #Dùng được trùng tên biến do là name là local variable nghĩa là chỉ giới hạn tầm ảnh hưởng ở trong biến chứ không mang ra ngoài được
    print("Toán : 5")
    print("Văn : 7")

main()