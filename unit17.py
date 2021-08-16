#BÀI 17 : HỌC PARAMETER

def print_number(max_number):# max_number là parameter (tham số)
	for i in range(max_number): #dòng này thuộc phần body của def nên thụt đầu dòng
			print(i)

print_number(max_number)

#======================

def print_number(max_number): 
	for i in range(max_number):
		print(i + 1)

max_number = 5

print_number(max_number)#Nó sẽ chạy dòng này trước, max_number bằng 5 gọi là input, nó sẽ input vào hàm và chạy cái khối lệnh trong hàm, cho ra kết quả output

max_number = 6 #ở đây max_number bằng 6, nó sẽ linh hoạt trong việc input cho mình

print_number(max_number

#GIẢI THÍCH LOGIC : Khi mình gọi hàm thì những tham số trong print_number(....) (... là tham số) sẽ gọi là input, input sẽ đi vào khối lệnh def để nó xử lí theo các quy trình hay các bước mình cho sẵn
#rồi nó đẻ ra output, chính là cái mình gọi 
#input là kiểu số nguyên, nghĩa là chỉ nhận số chứ không nhận kiểu dữ liệu string là chữ

#TIẾNG ANH TRONG BÀI
#TypeError : Lỗi kiểu
#missing : thiếu
#required : cần phải có
#positional : vị trí
#argument : đối số
#object : vật thể, khối
#interpreted : giải nghĩa