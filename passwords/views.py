from django.shortcuts import render
from .forms import PasswordDataForm, HashPasswordForm, CheckPasswordForm
from .services import PasswordService, Complexity, Length

def index(request):
    password = ''
    hashed_password = ''
    check_message = ''

    password_data_form = PasswordDataForm()
    hash_password_form = HashPasswordForm()
    check_password_form = CheckPasswordForm()

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

    return render(
        request, 'passwords/password_form.html', 
        {
            'passwordDataForm': password_data_form,
            'hashPasswordForm': hash_password_form,
            'checkPasswordForm': check_password_form,
            'password': password,
            'hashedPassword': hashed_password,
            'checkMessage': check_message
        }
    )

