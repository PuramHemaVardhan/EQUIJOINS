from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(job=ACCOUNTING)
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)