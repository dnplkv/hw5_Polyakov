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
        logger = Log()
        logger.save()
        if request.method == 'GET':
            path = request.path
            user_ip = get_ip_adress(request)
            utm = request.GET.get('utm')
            time_ex = time() - st
            logger = Log(utm=str(utm), time_exec=time_ex, user_ip=user_ip, path=path)
            logger.save()
        return response


def get_ip_adress(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
