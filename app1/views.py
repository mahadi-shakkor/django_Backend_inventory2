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
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process the form data and save it (e.g., create user or store data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user_choice = form.cleaned_data['Choosed_User_Type']  # Corrected field name
            
            # Here, you could save the user in the database or perform further actions
            
            print(f"Saving user: {user_choice}, {first_name}, {last_name}, {email}, {phone}, {password}")
          
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
            user = User(
            name=first_name +" "+ last_name,
            email=email,
            password=password,
            f="Y",  # Example value
            s="N",  # Example value
            n="Y",  # Example value
            w="N",  # Example value
            c="Y",  # Example value
            d="N",  # Example value
            r="Y",  # Example value
            a="N",  # Example value
            location=location
            )
        
        # Save the User instance
            user.save()
            # Redirect to a success page or login page
            return redirect('login')  # Assuming you have a 'login' route

    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

