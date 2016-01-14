from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, View
from forms import RegistrationForm
from django.shortcuts import render

class Login(FormView):

    form_class = AuthenticationForm 
    template_name = "happyhour/user_login.html"
    redirect_to = settings.LOGIN_REDIRECT_URL 

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return HttpResponseRedirect(self.redirect_to)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(Login, self).dispatch(request, *args, **kwargs)

class AdminLogin(Login):

    form_class = Login.form_class
    template_name = "happyhour/admin_login.html"
    redirect_to = settings.LOGIN_REDIRECT_URL_ADMIN

    def form_valid(self, form):
        if form.cleaned_data['username'] != "mochiolive_admin":
            return render(self.request, self.template_name, {'is_not_staff': True, 'form': form})
        return super(AdminLogin, self).form_valid(form)    

    def form_invalid(self, form):
        if form.cleaned_data['username'] != "mochiolive_admin":
            return render(self.request, self.template_name, {'is_not_staff': True, 'form': form})
        return super(AdminLogin, self).form_invalid(form)

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminLogin, self).dispatch(request, *args, **kwargs)


class Logout(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

class RegisterUser(FormView):
    form_class = RegistrationForm
    template_name = "happyhour/register.html"
    success_url = "/register-success/user/"

    def form_valid(self, form):
        form.save()
        return super(RegisterUser, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


