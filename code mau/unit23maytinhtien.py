#THỰC HÀNH LÀM MÁY TÍNH TIỀN TỰ ĐỘNG BẰNG FUNCTION VÀ KIẾN THỨC ĐÃ HỌC

def main():
	GIATAO = 20000 #Giá tiền của một cân táo
	can = float(input("Nhập cân nặng số táo khách mua : "))
	tongtien = tinhtien(GIATAO, can)
	print("Tổng tiền khách cần phải trả cho {} kg táo là : {}VND".format(can,tongtien))
	tientra =int(input("Tiền khách trả cho bạn là : "))
	tienthua = tienthoi(tientra, tongtien)
	if tienthua < 0:
		tienthua = int(tienthua) - int(tienthua) - int(tienthua)
		print("Khách đưa thiếu {}VND, cần đưa thêm".format(tienthua))
	else:
		print("Tiền bạn cần thối lại cho khách là : ",tienthua)
		tienvnd(tienthua)

def tienvnd(tienthua): 
	#500 200 100 50 10 5 1
	to_500 = int(tienthua/500000)
	tienthua = tienthua - 500000 * to_500

	if to_500 != 0:
		print("Số tờ 500k phải trả : " + str(to_500))

	to_200 = int(tienthua/200000)
	tienthua = tienthua - 200000 * to_200

	if to_200 != 0:
		print("Số tờ 200k phải trả : " + str(to_200))

	to_100 = int(tienthua/100000)
	tienthua = tienthua - 100000 * to_100

	if to_100 != 0:	
		print("Số tờ 100k phải trả : " + str(to_100))

	to_50 = int(tienthua/50000)
	tienthua = tienthua - 50000 * to_50

	if to_50 != 0:
		print("Số tờ 50k phải trả : " + str(to_50))

	to_10 = int(tienthua/10000)
	tienthua = tienthua - 10000 * to_10

	if to_10 != 0:	
		print("Số tờ 10k phải trả : " + str(to_10))

	to_5 = int(tienthua/5000)
	tienthua = tienthua - 5000 * to_5

	if to_5 != 0:
		print("Số tờ 5k phải trả : " + str(to_5))

	to_1 = int(tienthua/1000)
	tienthua = tienthua - 1000 * to_1

	if to_1 != 0:
		print("Số tờ 1k phải trả : " + str(to_1))



def tienthoi(tientra, tongtien):
	tienthoi = tientra - tongtien
	if tienthoi < 0:
		return tienthoi #-1 được hiểu là không có giá trị ( không đúng ), 1 hàm mà gặp return thì coi như sẽ skip hàm, giống continue
	return tienthoi

def tinhtien(GIATAO, can):
	tongtien = GIATAO * can
	return tongtien

main()

# #Tiếng anh trong bài :
# #assumption : Giả sử
# #decouple : Chia chương trình thành nhiều phần
# #decoupling : Không liên kết
# #module : phần