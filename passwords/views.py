from django.shortcuts import render, redirect
from .forms import PasswordDataForm, HashPasswordForm, CheckPasswordForm, SavePasswordForm
from .services import PasswordService, Complexity, Length
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpRequest
from .models import GeneratedPassword

def index(request: HttpRequest):
    password = ''
    hashed_password = ''
    check_message = ''
    user_logged = False

    password_data_form = PasswordDataForm()
    hash_password_form = HashPasswordForm()
    check_password_form = CheckPasswordForm()

    if request.user.is_authenticated:
        user_logged = True

    if request.method == 'POST':
        if 'generate_password' in request.POST:
            password_data_form = PasswordDataForm(request.POST)
            
            if password_data_form.is_valid():
                complexity = Complexity[password_data_form.cleaned_data['complexity']]
                length = Length[password_data_form.cleaned_data['complexity']]

                password = PasswordService.generate_password(complexity, length)
        
        elif 'hash_password' in request.POST:
            hash_password_form = HashPasswordForm(request.POST)

            if hash_password_form.is_valid():
                password = hash_password_form.cleaned_data['password']
                hashed_password = PasswordService.hash_password(password)

        elif 'check_password' in request.POST:
            check_password_form = CheckPasswordForm(request.POST)

            if check_password_form.is_valid():
                plain_password = check_password_form.cleaned_data['plain_password']
                hashed_password_to_check = check_password_form.cleaned_data['hashed_password']

                if PasswordService.check_password(plain_password, hashed_password_to_check):
                    check_message = 'Las contraseñas coinciden.'
                else:
                    check_message = 'Las contraseñas no coinciden.'

        elif 'save_password' in request.POST:
            print(f'valor de password: {password}')
            request.session['password'] = request.POST.get('password')
            print(f'valor de password en sesion: {request.session.get('password')}')
            return redirect('save-password')

    return render(
        request, 'passwords/password_form.html', 
        {
            'passwordDataForm': password_data_form,
            'hashPasswordForm': hash_password_form,
            'checkPasswordForm': check_password_form,
            'password': password,
            'hashedPassword': hashed_password,
            'checkMessage': check_message,
            'user_logged': user_logged
        }
    )

def signup(request: HttpRequest):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def save_password(request: HttpRequest):
    password = request.session.get('password', '')

    if request.method == 'POST':
        form = SavePasswordForm(request.POST)

        GeneratedPassword.objects.create(
            user = request.user,
            password_name = request.POST.get('password_name'),
            password = request.POST.get('password')
        )

        messages.success(request, '¡Contraseña guardada con éxito!')

    else:
        form = SavePasswordForm(initial={'password': password})

    return render(request, 'passwords/save-password.html', {'form': form})
