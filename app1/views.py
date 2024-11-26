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
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from .models import User  
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
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .forms import SignupForm
from .models import User, Location
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import SignupForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            uid = form.cleaned_data['userid']
            password = form.cleaned_data['password']
            
            # Try to get the user by the provided userid (assuming User model has a field 'id')
            try:
                user = User.objects.get(userid=uid)
            except User.DoesNotExist:
                messages.error(request, "Invalid credentials")
                return render(request, 'login.html', {'form': form})

            # Now, authenticate the user
            if user.check_password(password):
                context={"user":user}
            # Use the check_password method for hashed passwords
                return render(request, 'home.html',context)  # Pass 'uname' as a keyword argument
        # Redirect to home after successful login
            else:
                messages.error(request, "Invalid credentials")

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    if request.method == 'POST':
        logout(request)  
        return redirect('login')  # Redirect to 'some_page' after logout

    return render(request, 'home.html')


def signup(request):
    last_user_id = None  # Default to None, if no users are registered yet.

    # Fetch the last created user (most recent sign up)
   
    last_user_id = User.objects.last().userid + 1
    

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
            S=""
            N=""
            W=""
            D=""
            R=""

#   (, 'Aggricultural Officer'),
#         (', 'Farmer'),
#         (, 'Customer'),
#         (', 'Supplier'),
#         (, 'Neutroshonist'),
#         (', 'Wirehouse Manager'),
#         ('', 'Distributor Company'),
#         (', 'Reatailer')
            if user_choice == "a":
                A += user_choice
            elif user_choice == "f":
                F += user_choice
            elif user_choice == "s":
                S += user_choice
            elif user_choice == "n":
                N += user_choice  
            elif user_choice == "w":
                W += user_choice
            elif user_choice == "d":
                D += user_choice
            elif user_choice == "r":
                R += user_choice           
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
                s=S,
                n=N,
                w=W,
                c=C,
                d=D,
                r=R,
                a=A,
                location=location
            )

            try:
                user.save()
                A = ""
                F = ""
                C = ""
                S = ""
                N = ""
                W = ""
                D = ""
                R = ""

                # Redirect to a success page or login page
                return redirect('login')

            except IntegrityError as e:
                form.add_error(None, f"An error occurred while saving your account: {str(e)}")
                return render(request, 'signup.html', {'form': form, 'last_user_id': last_user_id})

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form, 'last_user_id': last_user_id})

