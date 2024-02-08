from django.http import JsonResponse
from rest_framework import status


def validate_object(model_class, uid, object_name):
    try:
        return model_class.objects.get(uid=uid)
    except model_class.DoesNotExist:
        return JsonResponse({'error': f'{object_name} does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
