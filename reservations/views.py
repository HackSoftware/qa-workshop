from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Property, Reservation, Guest


@csrf_exempt
def nuke(request):
    if request.method != "POST":
        return JsonResponse({'message': "Only POST requests are allowed!"}, status=405)

    user = request.user

    if user.is_anonymous:
        return JsonResponse({'message': "You must be logged in to nuke your data!"}, status=403)

    Property.objects.filter(owner=user).delete()
    Reservation.objects.filter(owner=user).delete()
    Guest.objects.filter(owner=user).delete()

    return JsonResponse({'message': "Data nuked!"})
