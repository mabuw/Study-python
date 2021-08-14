#THỰC HÀNH VÒNG LẶP FOR

#CHO S =            1
#======      -----------------
#======       1 + 1 + 1 + 1 + 1        + 1
#======       -   -   -   -   -  .....   -
#======       3   5   7   9   11         99
#====== Tính S

#CÁCH 1 của FOR
mauso = 0 #khai báo biến mauso có giá trị là 0

for i in range(100):
	if i == 1: #Bởi vì trong đề bài nó chỉ lấy từ 3 đến 99 nên gặp 1 sẽ bỏ qua 
		continue
	if i % 2 == 0: #% là toán tử chia, dòng này nghĩa là i sẽ chạy từ 0 đến 99, nếu i chia hết cho 2 thì bỏ qua, == 0 nghĩa là chia hết
#% nghĩa là lấy phần dư, trong trường hợp này nó sẽ bỏ qua những số nào chia cho 2 mà số dư bằng 0 ( chia hết )
		continue
	mauso = mauso + 1/i #/ là phân số và cũng là phép chia, tượng trưng cho 1/3, 1/5, 1/7
# phần mauso + tương trưng cho phần mẫu số của đề bài 1/3 + 1/5 + 1/7 + 1/9

# mauso = mauso + 1/i có thể viết tắt là :
 mauso += 1/i 
 #TƯƠNG ĐƯƠNG
 mauso = mauso + 1/i

 #Ngoài ra còn có :
 mauso -= 1/i

 s = 1/mauso #Nghĩa là s sẽ được gán giá trị như số 1 trên tử của đề bài, mauso = 1/3, 1/5, 1/7, còn S =
																									#                    1
																									#======      -----------------
																									#======       1 + 1 + 1 + 1 + 1        + 1
																									#======       -   -   -   -   -  .....   -
																									#======       3   5   7   9   11         99																									
s = round(s,2) #Rút gọn thập phân, chỉ lấy 2 giá trị sau dấu phẩy
print(s) # In giá trị S

#CÁCH 1 HOÀN CHỈNH :

mauso = 0


for i in range(100):

	if i == 1:
		continue

	if i % 2 == 0:
		continue
	
	mauso += 1/i	

s = 1/mauso
s = round(s,2)
print("S = " + str(s))

#CÁCH 2 của FOR (ngắn gọn hơn)
for i in range(3,100,2):
	mauso += 1/i	

s = 1/mauso
s = round(s,2)
print("S = " + str(s))


#TIẾNG ANH TRONG BÀI:
#Module : Phần dư
#division, divided by : Chia
#mutiply : nhân
#fraction : phân số, gồm tử số (numerator) và mẫu số (denominator)
#underscore : Dấu gạch chân
#semantic meaning : Có nghĩa