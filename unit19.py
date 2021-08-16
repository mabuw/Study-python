#BÀI 19 : RETURN VALUE ( GIÁ TRỊ TRẢ VỀ )


#HÀM TRẢ VỀ SỐ 3 VÌ NUMBER = NUMBER + 1 ( TƯƠNG ĐƯƠNG : NUMBER = 2 + 1)
def add_one(number): #number chính là input
	number = number + 1 #Gán giá trị cho biến number là number + 1
	print(number) #In ra giá trị của number
	return number #number sẽ trả về lại giá trị tại add_one(number), nghĩa là sau khi + 1 thì = 3, sau đó trả lại giá trị = 3 đó cho number trên def
	# và thoát ra khỏi hàm, không chạy code dưới nữa
x = 2
new_number = add_one(x) #x là giá trị input cho number
#new_number được hiểu là giá trị của hàm sau khi được trả về ( return )
print(new_number)


#HÀM TRẢ VỀ SỐ 10
def add_one(number): 
    number = number + 1 #Trong lập trình thì gọi là bạn đang increment number với 1, nghĩa là cộng
    return 10 #Trong dòng này nó chỉ quan tâm cái cần trả về, và nó trả về chỗ number, điền cái gì nó trả về cái đó
    #Nếu return không trả về gì thì nó sẽ là None ( trống rỗng)
    #Nếu muốn tính toán gì sau đó trả ra ngoài hàm thì phải có return để nó trả giá trị mới sau khi tính toán được ra
x = 2

new_number = add_one(x) #return nó sẽ trả lại 10 và phải gán vào một biến mới rồi in biến dó ra mới in ra được giá trị mới trả về, gọi là lưu giá trị được trả về

print(new_number)
#Tiếng anh trong bài 
#Return : Trả về
#Value : Giá trị
#Assign : Gán