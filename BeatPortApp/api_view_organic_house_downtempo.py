from django.http import JsonResponse, HttpResponse
from .models import OrganicHouseDownTempo
from .serializers import OrganicHouseDownTempoSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def organic_house_downtempo_list(request):
    top_100 = OrganicHouseDownTempo.objects.all()
    if request.method == 'GET':
        serializer = OrganicHouseDownTempoSerializer(top_100, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrganicHouseDownTempoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            content = serializer.data
            return JsonResponse(content, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def organic_house_downtempo_detail(request, pk):
    try:
        detail = OrganicHouseDownTempo.objects.get(pk=pk)

    except OrganicHouseDownTempo.DoesNotExist:
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
        serializer = OrganicHouseDownTempoSerializer(detail)
        return JsonResponse([serializer.data], safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrganicHouseDownTempoSerializer(detail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        detail.delete()
        return HttpResponse(status=204)
