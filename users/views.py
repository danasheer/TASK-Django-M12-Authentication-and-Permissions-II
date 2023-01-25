from django.shortcuts import render, redirect
from users.forms import RegisterForm


# Create your views here.
def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('home')
    context={
        "person":form
    }
    return render(request, 'regester.html',context)
