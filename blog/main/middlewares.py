from time import time

from .models import Log


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        st = time()
        utm = request.GET.get('utm')
        path = Log(path=request.path())
        path.save()
        if utm:
            time_exec = time() - st
            log = Log(utm=utm, time_exec=time_exec)
            log.save()
        else:
            ""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        ip_address = Log(ip_address=ip)
        ip_address.save()

        return response
