#Story based program 
#ramesh and suresh wants to go goa. Here goa is class. 
class goa:
      #created variables 
      name = "Baha"
      car = "tata"
      #created places to like 
      def beach(self):   
            print("Hey! you are in beach")
      def park(self):
            print("You are driving a car!")

#How they go goa like below. You just call function -> object created 
ramesh = goa()
suresh = goa()

#Now you go to the particular place
print(ramesh.name)
print(suresh.car)
print(ramesh.beach())
print(suresh.park())

#program 1
class class_name:
        a=10 #define variable if needed

        def function(self):
            print("This is function")   #define the function

print(class_name.function(1))

#program 2
class myclass:
      a = 30 
      def mul(x):
            print(x*x)
print(myclass.mul(10)) # output 100

#Object inside the program 
object=myclass()
print(object.a)