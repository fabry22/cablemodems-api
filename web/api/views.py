from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import DocsisUpdate
from api.serializers import DocsisUpdateSerializer

@api_view(['GET', 'POST'])
def docsisupdate_list(request, format=None):
    """
    List all docsisupdate, or create a new docsisupdate.
    """
    if request.method == 'GET':
        docsisupdates = DocsisUpdate.objects.all()
        serializer = DocsisUpdateSerializer(docsisupdates, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DocsisUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def docsisupdate_detail(request, pk, format=None):
    """
    Retrieve, update or delete a docsisupdate.
    """
    try:
        docsisupdate = DocsisUpdate.objects.get(pk=pk)
    except DocsisUpdate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DocsisUpdateSerializer(docsisupdate)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DocsisUpdateSerializer(docsisupdate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        docsisupdate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)