#BÀI 22 : THỰC HÀNH SỬ DỤNG FUNCTION VÀ PARAMETER

def main():
    nameA = input("Nhập tên :")
    diemtoanA = input("Nhập điểm toán :")
    diemvanA = input("Nhập điểm văn :")

    nameB = input("Nhập tên :")
    diemtoanB = input("Nhập điểm toán :")
    diemvanB = input("Nhập điểm văn :")

    hocsinh(nameA, diemtoanA, diemvanA) #Truyền giá trị của nam, diemtoan, diemvan xuống cho hàm hocsinh() để dùng nó trong hàm
    hocsinh(nameB, diemtoanB, diemvanB) #Sau khi in của nameA ra thì nó sẽ tiếp tục in nameB

def hocsinh(name, diemtoan, diemvan): #Giá trị đã được truyền xuống, định nghĩa sẵn trên main()
    print("Học sinh :" + name)
    print("Toán : " + diemtoan)
    print("Văn : " + diemvan)

main()