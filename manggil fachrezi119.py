import Fachrezi119 as zi

if __name__ == "__main__":

    A = zi.Fachrezi119([[1, 2],
                      [3, 4]])

    B = zi.Fachrezi119([[5, 6],
                      [7, 8]]) 

    print("Matriks A :")
    print(A)

    print("\nMatriks B :")
    print(B)

    hasil_tambah = A.tambah(B)
    print("\nHasil Penjumlahan A + B :")
    print(hasil_tambah)

    hasil_kurang = A.kurang(B)
    print("\nHasil Pengurangan A - B :")
    print(hasil_kurang)

    hasil_transpose = A.transpose()
    print("\nTranspose Matriks A :")
    print(hasil_transpose)