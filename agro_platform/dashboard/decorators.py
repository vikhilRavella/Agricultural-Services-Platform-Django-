from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.session.get('demo'):
                return view_func(request, *args, **kwargs)

            if not request.user.is_authenticated:
                return redirect('login')

            if request.user.role != role and not request.user.is_staff:
                return HttpResponseForbidden("Access denied")

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def demo_block_post(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('demo') and request.method == 'POST':
            return HttpResponseForbidden("Demo mode: actions disabled")
        return view_func(request, *args, **kwargs)
    return wrapper
