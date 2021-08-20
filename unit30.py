#BÀI 30 : KIỂU DỮ LIỆU LIST / ARRAY ( Danh sách ) / ( Mảng )

colors = ["red", "green", "blue"] #Khi mà nhìn thấy dấu ngoặc vuông thì sẽ là một cái gì đó liên quan đến list
#Tạo list bao gồm red, green, blue rồi gán giá trị vào biến colors, khi này colors được hiểu là 1 list

#In chữ "red"
print(colors) #In ra cả list
print(colors[0]) #Được hiểu là in string thứ nhất tính từ trái qua phải
print(colors[1]) #In ra "green"
print(colors[2]) #In ra "blue"
#Giá trị trong ngoặc vuông ví dụ như colors[0] được gọi là index()
#List / Array thường xuất phát từ 0

print(len(colors)) #len() là hàm check ra xem có bao nhiêu phần tử trong list 
#len viết tắt cho từ lenght ( độ dài )

#Sử dụng vòng lặp for để in ra các giá trị trong list:
for i in range(0,3):
	print(colors[i])

#While loop
while i < 3:
	print(colors[i])
	i += 1

#======================
colors = ["red", True, 12, 1.54] #True và 12, 1.54 là boolean và int và float nhưng khi cho vào list thì nó sẽ thành kiểu dữ liệu list
#Vì colors là kiểu dữ liệu list nên có thể cho vào True hoặc các int nó vẫn sẽ quy đổi về 1 kiểu dữ liệu là list

#Thêm giá trị vào list bằng hàm
colors.append("yellow") #append là thêm, giống bài FileIO

#Hàm thêm giá trị append()
i = 0
colors = ["red", "green", "blue"]

colors.append("Yellow") #Thêm yellow

while i < 4: #Khi này list sẽ có 4 giá trị
	print(colors[i])
	i += 1

print(colors[len(colors) - 1]) #Đây là cách in ra index cuối trong list
#Hoặc
print(colors[- 1]) # -1 tức là kí hiệu thằng cuối cùng trong list

#Chương trình hoàn chỉnh 
i = 0
colors = ["red", "green", "blue"]

colors.append("Yellow")

while i < len(colors): #len(colors) có thể thay đổi tùy theo độ dài của list
	print(colors[i])
	i += 1


print(colors[-1])

#Tiếng anh trong bài
#zero base index : Giá trị cốt lõi là 0
#lenght : độ dài