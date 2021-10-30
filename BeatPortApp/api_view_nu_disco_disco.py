from django.http import JsonResponse, HttpResponse
from .models import NuDiscoDisco
from .serializers import NuDiscoDiscoSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def nu_disco_disco_list(request):
    top_100 = NuDiscoDisco.objects.all()
    if request.method == 'GET':
        serializer = NuDiscoDiscoSerializer(top_100, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NuDiscoDiscoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            content = serializer.data
            return JsonResponse(content, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def nu_disco_disco_detail(request, pk):
    try:
        detail = NuDiscoDisco.objects.get(pk=pk)

    except NuDiscoDisco.DoesNotExist:
        return JsonResponse({
                                "errors": [
                                  {
                                    "status": 404,
                                    "message": "The request cannot be completed because it does not exist.",
                                    "reason": "The per page may not be greater than 100."
                                  }
                                ]
                            })

    if request.method == 'GET':
        serializer = NuDiscoDisco(detail)
        return JsonResponse([serializer.data], safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NuDiscoDiscoSerializer(detail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        detail.delete()
        return HttpResponse(status=204)
