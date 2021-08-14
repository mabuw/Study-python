#TỪ KHÓA VÒNG LẶP FOR (FOR LOOP) LÀ BREAK VÀ CONTINUE

#CONTINUE
for i in range(10):
	if i == 5:
		continue #Nếu code chạy đến continue thì tất cả đoạn code bên dưới sẽ bị skip và vòng lặp lại tiếp diễn
	print(i)

#BREAK
for i in range(10):
	if i == 5:
		break #Nếu code chạy đến đây và thỏa mãn điều kiện i là 5 thì sẽ hủy toàn bộ vòng lặp for và xuống chạy tiếp dưới đoạn chương trình còn lại
	print(i)

#TIẾNG ANH TRONG BÀI
#iteration : Từng lần lặp
#iterate : Lặp