from django.shortcuts import render
from django.http import HttpResponse
from .models import Driver_detail






def detail(request):
	all_detail= Driver_detail.objects.all()
	context={'all_detail':all_detail}
	return render(request,'Dashboard/index.html',context)