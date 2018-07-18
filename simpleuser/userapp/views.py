from .models import User
from .serializers import UserSerializer
from django.utils.six import BytesIO
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
# Create your views here.


@api_view(['GET'])
@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def index(request):
    if request.method == 'GET':
        if request.accepted_renderer.format == 'html':
            return Response({}, template_name='index.html')
        return Response("URL Not Found", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def user_list(request, format=None):
    """
    """
    if request.method == 'GET':
        if request.accepted_renderer.format == 'html':
            users = User.objects.all()
            return Response({'users': users}, template_name='user_list.html')
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        json = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            users = JSONParser().parse(stream)

            latest = User.objects.latest('created_at')

            return Response({'users': users}, status=status.HTTP_201_CREATED, template_name='user_list.html')
        return redirect('list_users')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def user_detail(request, user_id, format=None):
    """
    Retrieve, update or delete a user.
    """
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if request.accepted_renderer.format == 'html':
            serializer = UserSerializer(user)
            return Response({'user': serializer.data},
                            template_name='user_detail.html')

        serializer = UserSerializer(user)
        return Response(serializer.data)
