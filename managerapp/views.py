from django.shortcuts import render
from .forms import CredentialForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from .models import UserLoginDetails
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def new(request):
    if request.POST:
        form = CredentialForm(request.POST)

        if form.is_valid():
            theform = form.save(commit=False)
            theform.user = request.user
            theform.save()
            return redirect('dashboard') # send the user to the dashboard

    else:
        form = CredentialForm()

    return render(request, 'managerapp/new.html', {'form': form})

@login_required
def update(request, id):
    credential = get_object_or_404(UserLoginDetails, id=id)

    form = CredentialForm(request.POST or None, instance=credential)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'managerapp/update.html', {'form': form})

@login_required
def delete(request, id):
    credential = get_object_or_404(UserLoginDetails, id=id)

    if request.POST:
        credential.delete() # delete the credential

        return redirect('dashboard')

    return render(request, 'managerapp/delete.html', {'credential':credential})

