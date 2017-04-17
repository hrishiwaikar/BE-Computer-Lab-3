from django.shortcuts import render
from django.http import HttpResponse
from . import boothsprogram

app_name ='booth'
# Create your views here.
def index(request):
    return render(request,'booth/index.html')

def calculate(request):
    first_number = request.POST['firstnumber']
    second_number = request.POST['secondnumber']
    #prod=int(first_number)*int(second_number)

    contextdetails=boothsprogram.boothmultiplication(first_number,second_number)
    loopcount = len(contextdetails['steplist'])
    messagelist = contextdetails['messagelist']
    steplist = contextdetails['steplist']
    combined = zip(messagelist,steplist)
    context={

        'number1':first_number,
        'number2':second_number,
        'product':contextdetails['ans'],
        'bin1':contextdetails['m'],
        'bin2':contextdetails['r'],
        'A':contextdetails['A'],
        'P':contextdetails['P'],
        'S':contextdetails['S'],
        'combined':combined,
        'finalbinans':contextdetails['finalbinans'],
        'range':range(loopcount)
    }
    return render(request,'booth/calculate.html',context)

