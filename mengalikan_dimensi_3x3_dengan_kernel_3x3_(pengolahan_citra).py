gambar_list = [
	[4,7,1,9,8,5],
	[3,8,5,1,3,9],
	[2,2,8,2,5,7],
	[3,3,4,6,7,9],
	[2,5,5,1,4,8],
	[7,3,6,3,8,5]
]

# 6 ada 4x
# 7 ada 5x
# 8 ada 6x


kernel = [
	[0,-1,0],
	[-1,4,-1],
	[0,-1,0]
]


def hitungKernel(p1,q1,r1,s1):
	listKernel = []
	for i in range(p1,q1):
		for j in range(r1,s1):
			listKernel.append(kernel[i][j])
	return listKernel

def keKanan(koordinatSatu, batasKoordinatSatu, koordinatDua, batasKoordinatDua):
	hasil = []
	for i in range(koordinatSatu, batasKoordinatSatu):
		# print(i)
		for j in range(koordinatDua, batasKoordinatDua):	
			valueDariList = gambar_list[i][j]
			hasil.append(valueDariList)
	return hasil

def memisahSatuRangkaian(x1,x2,y1,y2,z):
	listBesar = []
	mark = z-2
	i = 0
	while i < mark:
		listBesar.append(keKanan(x1,x2,y1,y2))
		if i==3:
			y1=0
			y2=0
		elif i < 3:
			y1+=1
			y2+=1
		i=i+1

	return listBesar

def keBawah(dimensi1,dimensi2,y1,y2):
	panjangList = len(gambar_list)
	panjangIsiList = len(gambar_list[0])
	iterasi = panjangList - dimensi2
	totalIterasi = iterasi + 1
	i = 0
	while i < totalIterasi:
		if i == 0:
			wadah1 = memisahSatuRangkaian(dimensi1,dimensi2,y1,y2,panjangIsiList)
		elif i == 1:
			dimensi1+=1
			dimensi2+=1
			wadah2 = memisahSatuRangkaian(dimensi1,dimensi2,y1,y2,panjangIsiList)
		elif i == 2:
			dimensi1+=1
			dimensi2+=1
			wadah3 = memisahSatuRangkaian(dimensi1,dimensi2,y1,y2,panjangIsiList)
		elif i == 3:
			dimensi1+=1
			dimensi2+=1
			wadah4 = memisahSatuRangkaian(dimensi1,dimensi2,y1,y2,panjangIsiList)
		elif i == 4:
			dimensi1+=1
			dimensi2+=1
			wadah5 = memisahSatuRangkaian(dimensi1,dimensi2,y1,y2,panjangIsiList)

		i+=1
	return wadah1, wadah2, wadah3, wadah4

def perkalian(lists,kernels):
	taruhList = lists
	taruhKernel = kernels
	panjangKotakPertama = len(taruhList)
	panjangList = len(taruhList[0])
	hasilPerkalianSementara = 0
	hasilAkhirPerkalian = []
	z = 0
	for i in range(0,panjangKotakPertama):
		for j in range(0,panjangList):
			if i < panjangKotakPertama:
				hasilPerkalianSementara = hasilPerkalianSementara + (taruhList[i][j]*taruhKernel[z])
				z+=1
				if j == panjangList-1:
					hasilAkhirPerkalian.append(hasilPerkalianSementara)
					z=0
					hasilPerkalianSementara=0
			else:
				break
				
	return hasilAkhirPerkalian


def deklarasiUtama(startX, endX, startY, endY):
	kernelList = hitungKernel(0,3,0,3)
	hasilPemisahanBaris = keBawah(startX,endX,startY,endY)
	i=0
	while i < len(hasilPemisahanBaris):
		print(perkalian(hasilPemisahanBaris[i],kernelList))
		if i == len(hasilPemisahanBaris)-1:
			print("Congrats! Problem Solved")
		i+=1

deklarasiUtama(0,3,0,3)


# (wadah1, wadah2, wadah3, wadah4) = keBawah(0,3,0,3)



# nyimpen code nya dari pak billy tapi ga paham samsek :(

# fullkanan = 0
# for geserkanan4x in range(0,4):
# 	for geserbawah4x in range(0,4):
# 		geserkanan = 0 + geserkanan4x
# 		geserbawah = 0 + geserbawah4x
# 		hasil = 0
# 		starty = 0 + geserkanan
# 		endy = 3 + geserkanan
# 		startx = 0 + geserbawah
# 		endx = 3 + geserbawah
# 		for x in range(startx, endx):
# 			for y in range(starty, endy):
# 				print(gambar_list[x][y]) 

# 		print(" ")
# 	if fullkanan == 3:
# 		fullkanan = 0
# 	fullkanan 



