from operator import itemgetter
class Node:
    def __init__(self, data, parent):
        self._data = data
        self._parent = parent
        self._left = None
        self._right = None
    
    def insert(self, data):
        if data < self.operator():
            if self.left() is None:
                self._left = Node(data, self)
            else:
                self.left().insert(data)
        elif data > self.operator():
            if self.right() is None:
                self._right = Node(data, self)
            else:
                self.right().insert(data)
        else:
            return False #jika tidak berhasil menambah data
        return True #jika berhasil menambah data
    
    def operator(self):
        return self._data
    
    def left(self):
        return self._left

    def right(self):
        return self._right

    def parent(self):
        return self._parent
    
    def isRoot(self):
        return self._parent is None
    
    def isExternal(self):
        return self._left is None and self._right is None

class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0
    
    def add(self, data):
        if self._root is None:
            self._root = Node(data, None)
            self._size+=1
        else:
            if self._root.insert(data):
                self._size+=1
        print("Data berhasil ditambahkan!")
    
    def size(self):
        return self._size
    
    def empty(self):
        return self._size == 0
    
    def nodes(self):
        self.inorder(self._root)
    
    def _nodes(self):
        self._inorder(self._root)
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left())
            simpan = node.operator()
            print(simpan[0]+" - "+str(simpan[1]), end = '\n')
            self.inorder(node.right())
    
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left())
            tampung.append(node.operator())
            self._inorder(node.right())

tree = BinaryTree()
tampung = []
while True:
    print("Pilih Menu:")
    print("1. Tambah Mahasiswa\n2. Tampilkan Urut Nama\n3. Tampilkan Urut IPK")
    pilih = int(input("Pilihan Anda: "))
    if pilih == 1:
        nama = input("Masukkan Nama: ")
        ipk = float(input("Masukkan IPK: "))
        data = [nama,ipk]
        tree.add(data)
        print()
    elif pilih == 2:
        print("Daftar Mahasiswa:")
        tree.nodes()
        print()
    elif pilih == 3:
        print("Daftar Mahasiswa:")
        tree._nodes()
        sorted_list = sorted(tampung, key=itemgetter(1))
        for i in range(len(sorted_list)):
            print(sorted_list[i][0]+" - "+str(sorted_list[i][1]))
        print()