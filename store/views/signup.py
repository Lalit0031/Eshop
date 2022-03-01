from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    @staticmethod
    def get(request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get("firstname")
        last_name = postData.get("lastname")
        phone = postData.get("phone")
        email = postData.get("email")
        password = postData.get("password")

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    @staticmethod
    def validateCustomer(customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 character long or more"
        elif not customer.last_name:
            error_message = "Last Name Required !!"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 character long or more"
        elif not customer.phone:
            error_message = "Phone number Required !!"
        elif len(customer.phone) < 10:
            error_message = "Phone number must be 10 character long"
        elif len(customer.password) < 6:
            error_message = "Password must be at least 6 character long or more"
        elif len(customer.email) < 5:
            error_message = "Email must be 5 character long"
        elif customer.isExists():
            error_message = "Email Address Already Registered...!!"

        return error_message
