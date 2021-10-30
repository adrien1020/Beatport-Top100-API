from django.http import JsonResponse, HttpResponse
from .models import DanceElectroPop
from .serializers import DanceElectroPopSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def dance_electro_pop_list(request):
    top_100 = DanceElectroPop.objects.all()
    if request.method == 'GET':
        serializer = DanceElectroPopSerializer(top_100, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DanceElectroPopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            content = serializer.data
            return JsonResponse(content, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def dance_electro_pop_detail(request, pk):
    try:
        detail = DanceElectroPop.objects.get(pk=pk)

    except DanceElectroPop.DoesNotExist:
        return JsonResponse(({'foo': 'bar'}))
        #return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DanceElectroPopSerializer(detail)
        return JsonResponse([serializer.data], safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DanceElectroPopSerializer(detail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        detail.delete()
        return HttpResponse(status=204)