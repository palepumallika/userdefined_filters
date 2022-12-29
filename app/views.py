from django.shortcuts import render

# Create your views here.
def filters(request):
   import datetime
   dt=datetime.date.today()
   d={'data':'Hai DJANgo and PYThon','dt':dt,'c':1}
   return render(request,'filters.html',d)

def userdefinedfilters(request):
    d={'data':'HI Python HoW R yoU'}
    return render(request,'userdefinedfilters.html',d)