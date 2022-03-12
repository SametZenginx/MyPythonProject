class Kuvvet3():
    def __init__(self,max = 0):
        self.max = max
        self.kuvvet = 0
    def __iter__(self):
        return self
    def __next__(self):

        if (self.kuvvet<=self.max):
            sonuc = 3 ** self.kuvvet
            self.kuvvet += 1
            return sonuc
        else:
            self.kuvvet = 0 #Bu sekilde birdaha for ile donebiliyoruz.
            raise StopIteration

kuvvet = Kuvvet3(6)
for i in kuvvet:
    print(i)

for j in kuvvet: #Bastirmaz cunku 6 da kaldi bida donemedik.
    print(j)

