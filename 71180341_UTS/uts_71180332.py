class Node:
    def __init__(self, element, n):
        self._element = element
        self._next = n

class SLLNC:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        self._batas = 0
        self._kalori = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def push(self, e):
        if(self._kalori + e[1] <= self._batas):
            baru = Node(e, None)
            if self.isEmpty():
                self._head = baru
                self._tail = baru
                self._tail._next = None
                self._kalori += e[1]
            else:
                baru._next = self._head
                self._head = baru
                self._kalori += e[1]
            self._size += 1
            print("Data",baru._element[0],"(",baru._element[1]," kal ) disimpan!")
        else:
            print("Kalori akan melebihi batas!")
    
    def top(self):
        if self.isEmpty == True:
            return "Stack kosong!"
        else:
            return self._head._element
    
    def pop(self):
        if self.isEmpty()==False:
            d = ""
            if self._head._next==None:
                d = self._head._element
                self._head=None
            else:
                hapus = self._head
                d = hapus._element
                self._head = self._head._next
                hapus._next=None
                self._kalori -= d[1]
                del hapus
                return d
            self._size -= 1
        else:
            print("Stack kosong!")
    
    # def buang(self, e):
    #     simpan = []
    #     simpan.append(e)

    def printAll(self):
        if self.isEmpty()==False:
            bantu = self._head
            print("Riwayat Makanan : ", end='')
            while (bantu!= None):
                print(bantu._element[0],"(",bantu._element[1],"kal)"," ",end="")
                bantu = bantu._next
            print()
        else:
            print("Kosong!")

myStack = SLLNC()
print("Pilih Jenis Kelamin: ")
print("1. Pria\n2. Wanita")
pilih = int(input("Pilihan Anda : "))
if pilih == 1:
    myStack._batas = 2000
else:
    myStack._batas = 1500

while True:
    print()
    print("Pilih Menu:")
    print("1. Makan\n2. Buang\n3. Riwayat Makanan\n4. Keluar")
    print("Kalori saat ini: ",myStack._kalori)
    menu = int(input("Pilihan Anda : "))
    if menu == 1:
        nama = input("Masukkan nama: ")
        kalori = int(input("Masukkan kalori: "))
        myStack.push([nama, kalori])
    
    elif menu == 2:
        bagi = myStack.__len__() // 2
        simpan = []
        if bagi == 0:
            print("Data tidak bisa dibuang karena hasil pembulatan = 0")
        else:
            for i in range(bagi):
                simpan.append(myStack.pop())
            print("Makanan dibuang : ",end='')
            for x in simpan:
                print(x[0],"(",x[1],"kal)",end=", ")
            print()

    elif menu == 3:
        myStack.printAll()
    
    elif menu == 4:
        print("Terima Kasih !!")
        break