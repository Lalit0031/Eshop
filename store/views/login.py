from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    return_url = None

    @staticmethod
    def get(request):
        Login.return_url = request.GET.get('return-url')
        return render(request, 'login.html')

    @staticmethod
    def post(request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.get_customer_by_email(email)

        error_message = None

        print("Email :", email)
        print("Password: ", password)
        print("Customer: ", customer)

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                print("password is correct")
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect("homepage")
            else:
                error_message = "Password is invalid!"
        else:
            error_message = "Email is invalid!"
        print("Email : ", email, "| Password: ", password)
        return render(request, 'login.html', {'error': error_message})
