from django.http import JsonResponse, HttpResponse
from .models import JackinHouse
from .serializers import JackinHouseSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def jackin_house_list(request):
    top_100 = JackinHouse.objects.all()
    if request.method == 'GET':
        serializer = JackinHouseSerializer(top_100, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JackinHouseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            content = serializer.data
            return JsonResponse(content, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def jackin_house_detail(request, pk):
    try:
        detail = JackinHouse.objects.get(pk=pk)

    except JackinHouse.DoesNotExist:
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
        serializer = JackinHouseSerializer(detail)
        return JsonResponse([serializer.data], safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = JackinHouseSerializer(detail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        detail.delete()
        return HttpResponse(status=204)
