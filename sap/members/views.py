from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            nxt = request.GET.get("next", None)
            if nxt is None:
                return redirect('inicio')
            else:
                return redirect(nxt)
        else:
            messages.success(request,("Hubo un error de logueo prueba nuevamente!"))
            return redirect('login')
    else:
        return render(request,'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("Salió de su cuenta!"))
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password )
            login(request,user)
            messages.success(request,('Usted fue registrado con exito!'))
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'authenticate/register_user.html', {'form':form})
