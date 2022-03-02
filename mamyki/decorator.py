from django.shortcuts import redirect

def logged_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/login')
    return wrapper_func


def guest_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/dashboard')
    return wrapper_func


def allowed_user(role=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in role:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/dashboard')
        return wrapper_func
    return decorator
