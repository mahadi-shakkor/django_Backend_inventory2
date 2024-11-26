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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process the form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user_choice = form.cleaned_data['Choosed_User_Type']

            # Check if the email already exists in the User model
            if User.objects.filter(email=email).exists():
                # If email exists, show an error message and prevent saving
                form.add_error('email', 'This email address is already registered.')
                return render(request, 'signup.html', {'form': form})

            # Otherwise, proceed to save the new user
            A = ""
            F = ""
            C = ""

            if user_choice == "a":
                A += user_choice
            elif user_choice == "f":
                F += user_choice
            else:
                C += user_choice

            # Location details (you can adjust this as needed)
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

            # Create a new User object and save it
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
                user.save()  # Save the user to the database
                A = ""
                F = ""
                C = ""

                # Redirect to a success page or login page
                return redirect('login')  # Assuming you have a 'login' route

            except IntegrityError as e:
                # Catch any database errors related to unique constraints or other issues
                form.add_error(None, f"An error occurred while saving your account: {str(e)}")
                return render(request, 'signup.html', {'form': form})

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

