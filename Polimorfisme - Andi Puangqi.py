class A(object):
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "Object1 Lebih kecil dari Object2"
        else:
            return "Object2 Lebih kecil dari Object1"
    def __eq__(self, other):
        if(self.a == other.a):
            return "Keduanya Objectnya Sama"
        else:
            return "Objectnya Tidak Sama"
def main():
    ob1 = A(6)
    ob2 = A(3)
    print (ob1<ob2)
    ob3 = A(4)
    ob4 = A(4)
    print(ob4 == ob4)

if __name__ == "__main__":
   main()
