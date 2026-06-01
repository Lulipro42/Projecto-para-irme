# El MRO ES UNA ESPECIFICIDAD 
# D esta herando TANTGO B COMO C Y EN EL CASO DE QUE NO EXISTAN NINGUNA DE LAS DOS VAMOS A LA CLASE PADRE QU ES A D > B > C > A A SI SERIA LA RAMA 
class A:
    def hablar(self):
        print("Hola desde A")
        
class F:
    def hablar(self):
        print("Hola desde f")


class B(A):
    def hablar(self):
        print("Hola desde B")
        
class C(F):
    def hablar(self):
        print("Hola desde C")


class D(B,C):
    def hablar(self):
        print("Hola desde D")
        
d = D()

B.hablar(f)