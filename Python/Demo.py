# if (5 > 3):
#     print(True)
# else:
#     print(False)


# for i in range(1,6):
#     print("Number is : ",i,"and cube of the ",i,"is : ",i*i*i)


# for i in range(1,6):
#     print()
#     for j in range(1,i+1):
#         print("*", end="")
# print()
# for i in range(1,6):
#     print()
#     for j in range(5,i-1):
#         print("*",end="")


# i=1
# while(i<=5):
#     print(i)
#     i+=1


# i=10
# while(i<=200):
#     print(i)
#     i+=10


# i=10
# while(i>0):
#     print(i)
#     i-=1


# i=5
# fact = 1
# while(i>0):
#     fact *= i
#     i-=1
# print(fact)


# def evenorodd(a):
#     if (a%2==0):
#         print("Even")
#     else:
#         print("ODd")
# a = int(input())
# evenorodd(a)


# def ranges(a,b):
#     for i in range(a,b+1):
#         print(i)
# a = int(input())
# b = int(input())
# ranges(a,b)


#Single inheritance

# class employee():
#     def status(self):
#         print("Working with project")
# class teamleader(employee):
#     def process(self):
#         print("Working and monitoring the workflow")
# obj = teamleader()
# obj.status() 

# Multiple inheritance

# class employee():
#     def work(self):
#         print("Working")
# class leader():
#     def status(self):
#         print("Monitoring and working")
# class manager(employee,leader):
#     def roll(self):
#         print("Identify client need and monitoring workflow")
# obj = manager()
# obj.status()
# obj.work()

# Multilevel Inheritance

# class grandpa():
#     def phone(self):
#         print("grandpa's phone")
# class father(grandpa):
#     def money(self):
#         print("Father's money")
# class son(father):
#     def laptop(self):
#         print("Son's Laptop")
# obj1 = son()
# obj1.laptop()
# obj1.money()

# obj2 = father()
# obj2.phone()



#Hierarchial Inheritance

# class dad():
#     def money(self):
#         print("This is Dad's money")
# class son1(dad):
#     pass
# class son2(dad):
#     pass
# class son3(dad):
#     pass

# s1 = son1()
# s1.money()

# s2 = son2()
# s2.money()

# s3 = son3()
# s3.money()



#Hibrite Inheritance

# class dad():
#      def money(self):
#          print("This is Dad's money")
# class land():
#     def imp(self):
#         print("Important land")
# class son1(dad,land):
#      pass
# class son2(dad):
#      pass
# class son3(dad):
#      pass

# s1 = son1()
# s1.money()
# s1.imp()

# s2 = son2()
# s2.money()

# s3 = son3()
# s3.money()


# super keyword

# class a():
#     def __init__(self):
#         print("A")
#     def display(self):
#         print("This is class A")
# class b(a):
    
#     def __init__(self):
#         super().__init__()
#         print("B")
#     def display(self):
#         print("This is class b")
# obj = b()


# Polymorphism

# def add(a,b,c=0):
#     print(a+b+c)
# add(1,2)
# add(1,2,3)


# Overriding

# class Animal:
#     def sound(self):
#         print("Animals make a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks")
# obj = Dog()
# obj.sound()


# Encapsulation

# class company():
#     def __init__(self):
#         self.__companyName = "Google" # private 
#         self._companyName = "Google" # protected
# c1 = company()
# print(c1._companyName)


# Exception Handiling

# try:
#     print(5/0)
# except Exception as e:
#     print(e)
# finally:
#     print("Done")



