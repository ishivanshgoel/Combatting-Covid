from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# user info model
from .models import UserInfo
from .models import Plasma, Oxygen, Pharma

# helper functions
from .Helpers.Statesdata import Statesdata
import json
import datetime

# helpers
available_drugs = ["Tocilizumab", "Remdesivir",
                       "Favipiravir", "Fabiflu 200 MG"]
    
st = Statesdata()
states = st.getStates()

# convert time to integer
def to_str(dt_time):
    return str(10000000*dt_time.year + 1000000*dt_time.month + 100000*dt_time.day + 10000*dt_time.hour + 10000*dt_time.minute + 1000*dt_time.second + 100*dt_time.microsecond)

def gen_id(user, name, state, ty,contact):
    time = datetime.datetime.now()
    return hash(str(user) + str(name) + str(state) + str(ty) + str(contact) + to_str(time))


# all login views
def loginview(request):
    '''
    if request is POST then verify the credentials of the user and redirect to their respective location based on their user type
    else redirect to '/'
    '''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            u = authenticate(request, username=email, password=password)
        except:
            return HttpResponse('Some Error Occured')
        if u is not None:
            login(request, u)
            return redirect(user)
        else:
            return HttpResponse('Invalid username/ password')

    else:
        return HttpResponse("Not Allowed")

# user view - display after login
@login_required
def user(request):
    '''
    user
    '''
    return render(request, "user/oxygen.html")


@login_required
def plasma(request):
    global states
    plasma = Plasma.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            p = Plasma()
            p.user = request.user
            p.name = request.POST['name']
            p.state = request.POST['state']
            p.city = request.POST['city']
            p.donortype = request.POST['donortype']
            p.contact = request.POST['contact']
            p.id = gen_id(p.user, p.name, p.state, 'plasma', p.contact)
            p.save()
            print(p)
            messages.success(request, 'Thankyou for sharing the information.')
        except:
            messages.error(request, 'Error!!')
        return render(request, "user/plasma.html", {
            'states': states,
            "plasma" : plasma
        })
    else:
        return render(request, "user/plasma.html", {
            'states': states,
            "plasma" : plasma
        })


@login_required
def oxygen(request):
    global states
    oxygen = Oxygen.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            Oxy = Oxygen()
            Oxy.user = request.user
            Oxy.name = request.POST['name']
            Oxy.state = request.POST['state']
            Oxy.city = request.POST['city']
            Oxy.contact = request.POST['contact']
            Oxy.address = request.POST['address']
            Oxy.id = gen_id(Oxy.user, Oxy.name, Oxy.state, 'oxygen', Oxy.contact)
            Oxy.save()
            messages.success(request, 'Thankyou for sharing the information.')
        except:
            messages.error(request, 'Error!!')
        return render(request, "user/oxygen.html", {
            'states': states,
            'oxygen' : oxygen
        })

    else:
        return render(request, "user/oxygen.html", {
            'states': states,
            'oxygen' : oxygen
        })


@login_required
def hospital(request):
    '''
    user
    '''
    print(request.user)
    return render(request, "user/hospital.html")


@login_required
def pharma(request):
    global available_drugs, states
    pharma = Pharma.objects.filter(user=request.user)

    if request.method == 'POST':
        try:
            p = Pharma()
            p.user = request.user
            p.name = request.POST['name']
            p.state = request.POST['state']
            p.city = request.POST['city']
            p.contact = request.POST['contact']
            p.address = request.POST['address']
            p.available_drugs = request.POST.getlist('checks[]')
            p.id = gen_id(p.user, p.name, p.state, 'pharma', p.contact)
            p.save()
            messages.success(request, 'Thankyou for sharing the information.')
        except:
            messages.error(request, 'Error!!')

        return render(request, "user/pharma.html", {
            'states': states,
            "drugs":available_drugs,
            "pharma":pharma
        })
    else:
        return render(request, "user/pharma.html", {
            'states': states,
            "drugs":available_drugs,
            "pharma":pharma
        })


### Helper Routes ###
def getDistricts(request):
    '''
    get all districts
    '''
    try:
        state = request.GET.getlist('state')[0]
        st = Statesdata()
        data = st.getDistricts(state)
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')
    except:
        return HttpResponse('Error')
