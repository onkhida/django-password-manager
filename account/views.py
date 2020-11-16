from django.shortcuts import render
from managerapp.models import UserLoginDetails
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    saved_passwords = UserLoginDetails.objects.filter(user=request.user)
    return render(request, "account/dashboard.html", {'passwords':saved_passwords})
