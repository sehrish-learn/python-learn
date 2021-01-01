def test_num(limit):
    for num in range (0, limit+1):
        prime=0
        for i in range(2, num+1):
            if(num % i==0):
             prime += 1
        #print(prime)
        if(prime == 1):
            print(num, "prime")
        #else:
        #    print(num, "Not prime")
limit=(int(input()))
test_num(limit)




lower = 2
upper = 10
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           


           def test_num(limit):
    for num in range(1, 10):
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                print(num)
                break
        prime=0
limit=(int(input()))
test_num(limit)





num=max(4, 23)
print("The maximum number is:",num)






def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
print(fizz_buzz(3))




def fizz_buzz(input):
    if input % 5 == 0:
        return "Buzz"
print(fizz_buzz(5))




def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
print (fizz_buzz(15))





def fizz_buzz(input):
    if (input % 3==0) and (input % 5==0):
        return "FizzBuzz"
    else:
        return input
print(fizz_buzz(23))




def speed_check(speed):
    if speed<= 70:
        return "Ok"
    else:
        speed1=(speed-70)//5
        if speed<=12:
            return(f"Point: {speed1}")
        else:
            return "license suspended"
enter=speed_check(int(input("Enter speed:")))
print(enter)



def shoeNumbers(limit):
    for i in range(0, num +1):
        if i % 2==o:
            print(str(i),"Even")
        else:
            print(str(i),"Odd")
number=int(input)
showNumbers(number)