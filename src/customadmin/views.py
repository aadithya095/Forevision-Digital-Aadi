from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def admin_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("customadmin:dashboard")

    context = {
            'login_form': form,
            }
    return render(request, 'customadmin/login.html', context=context)

@login_required
def admin_dashboard(request):
    user = request.user
    context = {
            'user': user,
            }
    return render(request, 'customadmin/dashboard.html', context=context)
