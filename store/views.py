from django.db.models import query

from django.http import request
from django.shortcuts import render
from .forms import DonorForm
from store import forms
from .models import Donors

# Create your views here.

def addDonation(request):
    form = DonorForm(request.POST)
    if request.method=='POST' and form.is_valid():
        form.save()
    
    context = {
        'form':form
    }
    
    return render(request, 'newdonation.html', context)


def donorRecords(request):
    data = Donors.objects.all()
    if 'search' in request.GET:
        search = request.GET['search']
        data = Donors.objects.filter(Mobile_Number__icontains=search)
    if not data.exists():
        data = Donors.objects.filter(Document_ID__icontains=search)
    if not data.exists():
        return render(request,'entries.html', { 'empty':'No Records Found'})
    return render(request, 'entries.html',{'donor':data })


def showStore(request):
    data = Donors.objects.all()
    bloodgrouparray=[0,0,0,0,0,0,0,0]
    
    for i in range(0,Donors.objects.count()):
        if(Donors.objects.values('BLOOD_GROUP')[i]['BLOOD_GROUP']=='A+'):
            bloodgrouparray[0]+=1
        if(Donors.objects.values('BLOOD_GROUP')[i]['BLOOD_GROUP']=='A-'):
            bloodgrouparray[1]+=1
        if(Donors.objects.values('BLOOD_GROUP')[i]['BLOOD_GROUP']=='B+'):
            bloodgrouparray[2]+=1
        if(Donors.objects.values('BLOOD_GROUP')[i]['BLOOD_GROUP']=='B-'):
            bloodgrouparray[3]+=1
        if(Donors.objects.values('BLOOD_GROUP')[i]['BLOOD_GROUP']=='AB+'):
            bloodgrouparray[4]+=1
        if(Donors.objects.values('BLOOD_GROUP')[i]['BLOOD_GROUP']=='AB-'):
            bloodgrouparray[5]+=1
        if(Donors.objects.values('BLOOD_GROUP')[i]['BLOOD_GROUP']=='O+'):
            bloodgrouparray[6]+=1
        if Donors.objects.values('BLOOD_GROUP')[i]['BLOOD_GROUP']=='AB-':
            bloodgrouparray[7]+=1
    length=len(bloodgrouparray)
    plasma = 0
    newDonors = 0
    for i in bloodgrouparray:
        if i==1:
            newDonors+=1
    for i in bloodgrouparray:
        plasma+=i
    last_donation_object = Donors.objects.latest('date')
    print('Working on it....')
    print(last_donation_object)
    context={
        'last_donation':last_donation_object,
        'newDonor':newDonors,
        'plasma':plasma,
        'length':length,
        'data':data,
        'bloodgrouparray':bloodgrouparray
    }
    
    
    return render(request,'store.html',context)