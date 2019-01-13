from django.shortcuts import render
from exampleapp.forms import RegistrationForm
# Create your views here.

def index(request):
    return render(request,"exampleapp/index.html")


def register(request):

    registration = False
    if request.method == "POST":
        register_form = RegistrationForm(data = request.POST)

        if register_form.is_valid():
            register=register_form.save(commit=False)
            if "Profilepic" in request.FILES:
                print("found it")
                register.Profilepic = request.FILES["Profilepic"]
                register.save()
            register.save()
            registration = True
        else:
            print(register_form.errors)
    else:
        register_form = RegistrationForm()

    return render(request,"exampleapp/registration.html",context={"registration":registration,"register_form":register_form})
