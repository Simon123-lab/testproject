from django.shortcuts import render,redirect
from django.contrib.messages import constants as messages

# take input from the user

def home(request):
    return render(request,'index.html')

def index(request):
    print("test")
    if request.method=='POST':
        print("check")
        ch=request.POST['armstrong']
        number=int(ch)
        num = number


        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10

        # display the result
        if num == sum:
            return render(request,'check.html')
        else:
            return render(request,'notcheck.html')

    else:
        return render(request, 'armstrong.html')

