from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages

from core.models import drugs
from core.tasks import send_mail_func ,send_sms


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def home(request):
    send_mail_func.delay()
    send_sms.delay()
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/aboutus.html')

def booking(request):
    

    if request.method == 'POST':

        drug=drugs()
        company = request.POST.get('name')
        email = request.POST.get('email')
        mobile=request.POST.get('mobile')
        drugname= request.POST.get('dname')
        state= request.POST.get('state')
        exp=request.POST.get('expdate')
        manu=request.POST.get('mgfdate')
        packmaterial= request.POST.get('pack')

        drug.company=company
        drug.email=email
        drug.mobile=mobile
        drug.name=drugname
        drug.state=state
        drug.packmaterial=packmaterial
        drug.mfg=manu
        drug.expirydate=exp
        drug.save();

        messages.success(request, 'Contact request submitted successfully.')

    return render(request, 'core/appointment.html')

def send_mail_to_all(request):
    send_mail_func.delay()
    send_sms.delay()
    return HttpResponse("sent")
