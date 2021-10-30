from django.http import JsonResponse, HttpResponse
from .models import BassClub
from .serializers import BassClubSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def bass_club_list(request):
    top_100 = BassClub.objects.all()
    if request.method == 'GET':
        serializer = BassClubSerializer(top_100, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BassClubSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            content = serializer.data
            return JsonResponse(content, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def bass_club_detail(request, pk):
    try:
        detail = BassClub.objects.get(pk=pk)

    except BassClub.DoesNotExist:
        return JsonResponse(({'foo': 'bar'}))
        #return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BassClubSerializer(detail)
        return JsonResponse([serializer.data], safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BassClubSerializer(detail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        detail.delete()
        return HttpResponse(status=204)