from pprint import *

class Product:
    def __init__(self,n, w, c):
        if isinstance(n,str):
            self.name = n
        else:
            raise TypeError('Параметр n должен иметь тип str !!!')
        if isinstance(w, float) or isinstance(w, int):
            self.weight = float(w)
        else:
            raise TypeError('Параметр w должен иметь тип float !!!')
        if isinstance(c, str):
            self.category = c
        else:
            raise TypeError('Параметр c должен иметь тип str !!!')
    def __str__(self):
        return f'{self.name} {self.weight} {self.category}'

class Shop:
    def __init__(self,f_name='shop_product.txt'):
        self.file_name=f_name
        open(self.file_name,'a').close()
    def get_product_name(self):
        set_of_name=set()
        file=open(self.file_name,'r')
        for s in file:
            x=s.split()
            set_of_name.add(x[0])
        file.close()
        return  set_of_name
    def get_products(self):
        file = open(self.file_name, 'r')
        x=''
        for s in file:
            x += s
        file.close()
        return x
    def add(self,*products):
        s = self.get_product_name()
        file = open(self.file_name,'a')
        for p in products:
            if p.name in s:
                print(f'Продукт {p.name} уже есть в магазине')
            else:
                s.add(p.name)
                file.write(str(p)+'\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


