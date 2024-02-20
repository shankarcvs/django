from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet,Snippett
from .serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        snippetts = Snippett.objects.all()
        serializer1 = SnippetSerializer(snippets, many=True)
        serializer = SnippetSerializer(snippetts, many=True)
        return JsonResponse({'one':serializer1.data,'two':serializer.data} ,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, language):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        #snippet = get_object_or_404(Snippet, name=name)
        snippet = Snippet.objects.filter(language=language).order_by('-id')
        #snippet = [snippets for snippets in snippet]

    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)