from django.http import HttpResponse
from book.models import BlockedUsers


class IpBlockMiddleWare():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request.user.login_try_count
        if request.META.get('REMOTE_ADDR') in BlockedUsers.objects.values_list("address", flat=True):
            return HttpResponse("Your ip address blocked")
        response = self.get_response(request)
        return response
