class PersegiPanjang:
    panjang = 0
    lebar = 0

    def __init__(self, panjang, lebar):
        if panjang == 0 or lebar == 0:
            raise ValueError("nilai tidak boleh 0")
        self.panjang = panjang
        self.lebar = lebar
