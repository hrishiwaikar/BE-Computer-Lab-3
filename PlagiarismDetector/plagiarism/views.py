from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm,TestForm
from .plagchecker import plagiarismchecker
# Create your views here.
def index(request):
    if request.method == 'POST':
        myform = MyForm(request.POST)
        testform=TestForm(request.POST)
        showoutput = True

        if myform.is_valid() and testform.is_valid():
            targettext=testform.cleaned_data['testText']
            text1=myform.cleaned_data['textbox1']
            text2=myform.cleaned_data['textbox2']
            text3 = myform.cleaned_data['textbox3']

            percentages=plagiarismchecker(text1,text2,text3,targettext)
            #print 'Hahaha'
            print percentages['percentage1']
            context={
                'myform':myform,
                'showoutput':showoutput,
                'percentage1':percentages['percentage1'],
                'percentage2': percentages['percentage2'],
                'percentage3': percentages['percentage3'],
                'testform':testform,
            }
            return render(request,'homepage.html',context)
    else:
        #simply GET method , should show this when first time accessed the page
        myform = MyForm()
        testform = TestForm()

        showoutput=False
        context={
            'myform':myform,
            'showoutput':showoutput,
            'testform':testform,
        }
        return render(request,'homepage.html',context)

