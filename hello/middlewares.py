from django.http import JsonResponse


class HealthCheckMiddleware(object):
    def process_request(self, request):
        if request.path == '/health-check':
            return JsonResponse(dict(status='healthy'))
