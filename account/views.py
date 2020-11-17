from django.shortcuts import render, redirect
from managerapp.models import UserLoginDetails
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import CheckPasswordForm, UserRegistratonForm
from django.contrib import messages


# Create your views here.
@login_required
def dashboard(request):
    saved_passwords = UserLoginDetails.objects.filter(user=request.user).order_by('-id')
    return render(request, "account/dashboard.html", {'passwords':saved_passwords})

def credential_detail(request, id):
    show_password = False

    # if request.POST:
    #     form = CheckPasswordForm(request.POST)
    #     if form.is_valid:
    #         # check the password inputed against the original password
    #         pwd = form.cleaned_data('password')

    #         if request.user.check_password(pwd):
    #             show_password = True

    # else:
    #     form = CheckPasswordForm()

    credential = get_object_or_404(UserLoginDetails, id=id)

    if request.user == credential.user: # if the signed in user owns the credentials
        show_password = True 

    context = {
        'credential': credential,
        'show_password': show_password,
        # 'form':form,
    }

    return render(request, 'account/credential.html', context)

def register(request):
    if request.POST:
        user_form = UserRegistratonForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()

            messages.success(request, 'Login with your new account!')
            return redirect('login')

    else:
        user_form = UserRegistratonForm()

    return render(request, 'account/register.html', {'user_form':user_form})
