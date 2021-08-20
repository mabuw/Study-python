#BÀI 31 : CÁC HÀM ĐỂ XỬ LÍ LIST / ARRAY

colors = ["red", "green", "blue", "yellow"]

print(colors)

#======================HÀM REMOVE=========================
colors.remove(colors[1]) #HÀM remove() dùng để xóa 1 index nào đó trong list
print(colors)

if "greenn" in colors: #Check xem string "greenn" có ở trong list colors hay không
    colors.remove("greenn") #Nếu có thì nó sẽ remove
else:
    print("not exits")

#Hoặc

try:
	colors.remove("greenn") #Nếu dòng này không có lỗi thì nó sẽ chạy
except:
	print("not exits") #Tương tự như else, nếu có lỗi nó sẽ chạy dòng này

#======================HÀM POP============================
colors = ["red", "green", "blue", "yellow"]
colors.pop() #HÀM pop() dùng để xóa index cuối cùng trong list, trong trường hợp này là "yellow"
print(colors) #In list sau khi xóa

#======================HÀM INSERT=========================
colors = ["red", "green", "blue", "yellow"]

print(colors)

colors.insert(0, "black") #HÀM insert() dùng để thêm giá trị vào bất kì index nào trong list
#Ví dụ 0, "black" là thêm string "black" vào index 0, nghĩa là ngay đầu list

print(colors) #In list sau khi thêm

#======================HÀM APPEND=========================
colors = ["red", "green", "blue"]

colors.append("yellow") #HÀM append() dùng để thêm một string vào index cuối của list

print(colors) #In list sau khi thêm

#======================HÀM LEN============================
colors = ["red", "green", "blue"]

print(len(colors)) #HÀM len() dùng để in ra số phần tử có trong list, ví dụ như ở đây là 3

#======================HÀM INDEX============================
colors = ["red", "green", "blue"]

print("Từ 'red' xuất hiện ở những vị trí sau đây: " + str(colors.index("red"))) #HÀM index() dùng để tìm vị trí của một string trong list, ví dụ ở đây tìm red và red nằm ở 0
#Nó sẽ in ra số 0 vì "red " nằm ở vị trí 0 trong list

#Hoặc 

print(colors.index(input())) #Tìm giá trị nào có thể nhập từ bàn phím, ví dụ tìm "red" thì nó sẽ hiện lên là 0 trong trường hợp này

#TÌM VỊ TRÍ CỦA "RED" NẾU CÓ NHIỀU "RED" TRONG CÙNG 1 LIST
colors = ["red", "green", "blue", "yellow", "red"]

red_index = []
for i in range(len(colors)):
	if colors[i] is "red":
		red_index.append(i)

print("Từ 'red' xuất hiện ở những vị trí sau đây: " + str(red_index))

#TÌM XEM "RED" XUẤT HIỆN BAO NHIÊU LẦN Ở TRONG LIST
colors = ["red", "green", "blue", "yellow", "red"]

red_index = 0
for i in range(len(colors)):
	if colors[i] is "red":
		red_index += 1

print("Số red có là :" + str(red_index))

#Hoặc : 

#======================HÀM COUNT============================
colors = ["red", "green", "blue", "yellow", "red"]

print("Số lần red xuất hiện là : " + str(colors.count("red")))#Đếm xem số lần "red" xuất hiện trong list

#======================HÀM SORT=============================
a = [1,3,6,7,3,2,6]
a.sort() #HÀM sort() dùng để sắp xếp theo số thứ tự từ bé đến lớn nếu trong list là số nguyên
print(a)

#Thay thế một string hay giá trị nào đó trong list
a = [1,3,6,7,3,2,6]

a[5] = "Son" #Trong list a, giá trị nào nằm ở vị trí thứ 5 sẽ bị đổi thành "Sơn"

print(a) #In ra a sau khi được thay thế

#TIẾNG ANH TRONG BÀI
#Validation : hoạt động
#occurance ( occur ) : Số lần xuất hiện