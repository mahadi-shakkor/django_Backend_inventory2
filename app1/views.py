from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from .models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after successful login
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

# Home View (Protected by login_required)
@login_required
def home(request):
    return render(request, 'home.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username,password)
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to a home page or dashboard
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
from .models import Location
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import User, Location

from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import User, Location

from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import User, Location

def signup(request):
    last_user_id = None  # Default to None, if no users are registered yet.

    # Fetch the last created user (most recent sign up)
    last_user = User.objects.last()
    if last_user:
        last_user_id = last_user.userid+1

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process the form data and save the new user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user_choice = form.cleaned_data['Choosed_User_Type']

            # Check if the email already exists in the User model
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email address is already registered.')
                return render(request, 'signup.html', {'form': form, 'last_user_id': last_user_id})

            A = ""
            F = ""
            C = ""

            if user_choice == "a":
                A += user_choice
            elif user_choice == "f":
                F += user_choice
            else:
                C += user_choice

            # Location details (can be customized)
            location = Location(
                latitude=12.9716,
                longitude=77.5946,
                street="MG Road",
                city="Bangalore",
                state="Karnataka",
                country="India",
                postalcode="560001",
                altitude=920,
                timezone="Asia/Kolkata"
            )
            location.save()

            # Create and save the new user
            user = User(
                name=first_name + " " + last_name,
                email=email,
                password=password,
                f=F,
                s="",
                n="",
                w="",
                c=C,
                d="",
                r="",
                a=A,
                location=location
            )

            try:
                user.save()
                A = ""
                F = ""
                C = ""

                # Redirect to a success page or login page
                return redirect('login')

            except IntegrityError as e:
                form.add_error(None, f"An error occurred while saving your account: {str(e)}")
                return render(request, 'signup.html', {'form': form, 'last_user_id': last_user_id})

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form, 'last_user_id': last_user_id})

