from django.shortcuts import render, redirect
from django.contrib.auth import login,aauthenticate,logout
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    message = request.session.pop('logout_message', None)  # Recupera y elimina el mensaje después de mostrarlo
    form = CustomUserLoginForm(data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')

    return render(request, "login.html", {"form": form, "message": message})


@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    request.session['logout_message'] = {
        "type": "info",
        "message": "Se ha cerrado sesión exitosamente",
        "code": 200,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8MIbugIhZBykSmQcR0QPcfnPUBOZQ6bm35w&s"
    }
    return redirect('login')