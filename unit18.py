#BÀI 18 : THỰC HÀNH VỚI MUTIPLE PARAMETER

def print_number(min_number, max_number): 
	for i in range(min_number,max_number): #Dòng này tương đương range(2,10)
		print(i + 1)


print_number(2,10) #2 và 10 tương ứng với 2 giá trị mình sẽ gán cho min và max_number, được gọi là input giá trị vào để hàm tính toán và trả cho chúng ta kết quả

def print_number(min_number, max_number, khoangcach): #Thêm khoangcach nghĩa là thêm 1 parameter
    for i in range(min_number, max_number, khoangcach): #Dòng này tương ứng range(2,10,2)
        print(i)

print_number(2,10,2) #Gán giá trị cho từng parameter, dòng này gọi là argument ( đối số )
