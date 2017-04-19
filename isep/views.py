#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .forms import AddForm_OTP
from .forms import AddForm_Cas
import random

# Create your views here.

def func_home(request):
	string = "WELCOME TO MYSITE!"	
	return render(request, 'home.html', {'xxx': string})

def func_OTP(request):
    global Ans_str
    if request.method != 'POST': 
        form = AddForm_OTP()
        Mes_str = ''
        Ans_str = ''
        Key_str = ''
        for x in range(5):
            rdm = random.randint(0, 1)
            rdk = random.randint(0, 1)
            if rdm == 0:
		            tmp1 = 0
		            Mes_str = Mes_str + '0'
            else :
                    tmp1 = 1
                    Mes_str = Mes_str + '1'
	
            if rdk == 0:			
                    tmp2 = 0		
                    Key_str = Key_str + '0'
            else :
		            tmp2 = 1
		            Key_str = Key_str + '1' 
            tmp = tmp1 ^ tmp2
            Ans_str = Ans_str + str(tmp)
        return render(request, 'isep/otp.html', {'Mes_str': Mes_str, 'Key_str': Key_str, 'form': form})
    else :
		form = AddForm_OTP(request.POST)
		if form.is_valid():
			usr_ans = form.cleaned_data['usr_ans']
			return render(request, 'isep/otp_rslt.html', {'Ans_str': Ans_str, 'usr_ans': usr_ans})

#def func_OTP_Result(request):
#    if request.method == 'POST':
#		form = AddForm_OTP(request.POST)
#		if form.is_valid():
#			usr_ans = form.cleaned_data['usr_ans']
#			return render(request, 'isep/otp_rslt.html', {'Ans_str': Ans_str, 'usr_ans': usr_ans})






def func_Cas(request):
    form = AddForm_Cas()
    return render(request, 'isep/cas.html', {'form': form})

def func_Cas_Result(request):
    if request.method == 'POST':
		form = AddForm_Cas(request.POST)
		if form.is_valid():
			    a = form.cleaned_data['a']
			    b = form.cleaned_data['b']
                string = str(int(a)+int(b))
                return render(request, 'isep/cas_rslt.html', {'string': string})
        
           

