from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import SignupForm

def login_page(request):
    return render(request, 'accounts/login.html')
# -------------------------------
# ROLE REDIRECT
# -------------------------------
def redirect_user_by_role(user):
    if user.is_superuser or user.is_staff:
        return '/'
    if user.role == 'farmer':
        return '/dashboard/farmer/'
    if user.role == 'supplier':
        return '/dashboard/supplier/'
    if user.role == 'provider':
        return '/dashboard/provider/'
    return '/'

# -------------------------------
# LOGIN
# -------------------------------
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        # Clear demo mode when a real user logs in
        self.request.session.pop('demo', None)
        return super().form_valid(form)

    def get_success_url(self):
        return redirect_user_by_role(self.request.user)

# -------------------------------
# DEMO LOGIN (KEY FIX)
# -------------------------------
def demo_login(request):
    request.session.flush()
    request.session['demo'] = True
    return redirect('home')
