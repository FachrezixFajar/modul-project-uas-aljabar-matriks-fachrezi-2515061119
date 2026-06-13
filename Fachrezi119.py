class Fachrezi119:
    def __init__(self, data):
        if len(data) != 2 or len(data[0]) != 2 or len(data[1]) != 2:
            raise ValueError("Matriks harus berukuran 2x2")
        self.data = data

    def tambah(self, matriks_lain):
        hasil = [
            [
                self.data[i][j] + matriks_lain.data[i][j]
                for j in range(2)
            ]
            for i in range(2)
        ]
        return Fachrezi119(hasil)

    def kurang(self, matriks_lain):
        hasil = [
            [
                self.data[i][j] - matriks_lain.data[i][j]
                for j in range(2)
            ]
            for i in range(2)
        ]
        return Fachrezi119(hasil)

    def transpose(self):
        hasil = [
            [self.data[0][0], self.data[1][0]],
            [self.data[0][1], self.data[1][1]]
        ]
        return Fachrezi119(hasil)

    def __str__(self):
        return "\n".join(
            [" ".join(map(str, baris)) for baris in self.data]
        )