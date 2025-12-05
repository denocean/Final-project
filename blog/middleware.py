from django.http import JsonResponse
import logging

def health_check(request):
    return JsonResponse({'status': 'ok'})

class SimpleLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('django.request')

    def __call__(self, request):
        response = self.get_response(request)
        self.logger.info(f"{request.method} {request.path} {response.status_code}")
        return response
