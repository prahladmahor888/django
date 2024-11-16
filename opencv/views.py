from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForms
from .models import createuser, UploadImage, cardEvent, userInfo
from django.core.mail import send_mail
from django.conf import settings
from PIL import Image
import random, pytesseract, cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\drbra\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


# Create your views here.

def home(request):
    if request.method == "POST":
        userid = request.user 
        fname = request.user.first_name
        lname = request.user.last_name      
        image = request.FILES['file']

        myimage = Image.open(image)
        text = pytesseract.image_to_string(myimage)

        userImage = UploadImage(first_name=fname, last_name=lname, userid=userid, image=image)
        userImage.save()
        # myimage = cv2.imread(image)
        # show = cv2.imshow('img', myimage)
        return render(request, "home.html", {'text': text})
    img = UploadImage.objects.all().order_by("-id")
    card = cardEvent.objects.all().order_by("-id")
    return render(request, "home.html", {"img": img, "card": card})

def docs(request):
    return render(request, "docs.html")

def examples(request):
    return render(request, "example.html")

def user_register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        sendotp = random.randint(111111,999999)

        context = {
            'first_name': fname,
            'last_name': lname,
            'username': username,
            'email': email,
            'password': password,
            'sendotp': sendotp
        }
        # Send email OTP
        send_mail(
            'Email Verification OTP',
            f'Welcome {fname} {lname}\nYour OTP for email verification is: {sendotp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return render(request, "otp.html", context)        
    
    return render(request, "signup.html")

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        #username = User.objects.get(email=email.lower()).username
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have logged in!")
        
            return render(request, "home.html")           
            
        else:
            messages.success(request, "Login Failed try again")
            return redirect("login")

    return render(request, "login.html", {})

def reset_pass(request):
    if request.method == 'POST':
        username = request.POST['username']
            
        # if username == user:
        return render(request, "newpassword.html", {'username': username})
        # else: 
        #     return redirect('reset')
    return render(request, "reset.html")

def about(request):
    return render(request, "about.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def new_pass(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    if (password == repassword):
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        return render(request, "login.html", {"msg": True})
    else:
        return render(request, "newpassword.html", {"msg": True})
    

def otp(request):
    if request.method == "POST":
        otp1 = request.POST['otp1']
        otp2 = request.POST['otp2']
        otp3 = request.POST['otp3']
        otp4 = request.POST['otp4']
        otp5 = request.POST['otp5']
        otp6 = request.POST['otp6']
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        sendotp = request.POST['sendotp']

        verifyotp = otp1 + otp2 + otp3 + otp4 + otp5 + otp6

        if sendotp == verifyotp:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            return redirect("login")
        else:
            return render(request, "otp.html", {'message': False})
    return render(request, "otp.html")

def profile(request):
    return render(request, "profile.html")

def editProfile(request):
    if request.method == "POST":
        username = request.user
        userImage = request.FILES['profileimage']
        userAbout = request.POST['userAbout']
        user = userInfo(username=username, userAbout=userAbout, userImage=userImage)
        user.save()
        profile = userInfo.objects.order_by('-id')
        return render(request, 'profile.html',{"profile": profile})
    profile = userInfo.objects.order_by('-id')
    return render(request, "edit_profile.html", {"profile": profile})