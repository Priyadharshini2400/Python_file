class mobile_shop:
    shop_name="ABC_shop"
    location="Tambaram"
    obj_list=[]
    brand_list=set()
    color_list=set()
    price_list=set()
    def __init__(self,brand,color,model,price):
        self.brand=brand
        self.color=color
        self.model=model
        self.price=price
        mobile_shop.obj_list.append(self)
        mobile_shop.brand_list.add(brand)
        mobile_shop.color_list.add(color)
        mobile_shop.price_list.add(price)
    def display(self):
        print(f'The brand is {self.brand}')
        print(f'The color is {self.color}')
        print(f'The model is {self.model}')
        print(f'The price is {self.price}')
    
    @classmethod
    def shop_display(cls):
        print(f'The shop_name is {cls.shop_name}')
        print(f'The location is {cls.location}')
    @classmethod
    def display_brand(cls):
        for brand in cls.brand_list:
            print(f'--------------{brand}---------------')
            for mobile in cls.obj_list:
                if mobile.brand==brand:
                    mobile.display()
                    print()
    @classmethod
    def color_display(cls):
        for color in cls.color_list:
            print(f'................{color}.................')
            for mobile in cls.obj_list:
                if mobile.color==color:
                    mobile.display()
                    print()
    @classmethod
    def price_display(cls):
        for price in sorted(cls.price_list):
            print(f'*****************Rs.{price}*******************')
            for mobile in cls.obj_list:
                if mobile.price==price:
                    mobile.display()
                    print()
    @classmethod
    def particular_brand(cls):
        brand=input(("Enter a brand  :  "))
        for mobile in cls.obj_list:
            if mobile.brand==brand:
                mobile.display()
                print()
                
        
        
m1=mobile_shop("redmi","blue",'redmi note 9',15000)
m2=mobile_shop("moto","pink",'moto5',18000)
m3=mobile_shop("samsung","orange",'samsung galaxy5',25000)
m4=mobile_shop("oppo","red",'oppo real',20000)
m5=mobile_shop("apple","black",'iphone pro',150000)
m6=mobile_shop("vivo","white",'vivo lite',45000)
m7=mobile_shop("redmi","brown",'redmi note 5',15000)
m8=mobile_shop("moto","blue",'moto 4',25000)
m9=mobile_shop("samsung","red",'samsung galaxy ultra',45000)
m10=mobile_shop("vivo","pink",'vivo pro',15000)


#m1.display()
#m1.display_brand()
#mobile_shop.shop_display()
#mobile_shop.color_display()
#m1.price_display()
m1.particular_brand()
