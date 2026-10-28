
from django.shortcuts import render
import re

def login(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        pattern = r'^[A-Za-z][A-Za-z0-9_]{2,14}$'

        if not re.match(pattern, username):
            message = "Invalid username"
        elif len(password) < 6:
            message = "Password must contain at least 6 characters"
        else:
            message = "Login successful"

    return render(request, "login.html", {"message": message})
