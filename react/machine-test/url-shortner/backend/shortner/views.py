import random
import string

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ShortURL
from .serializers import ShortURLSerializer


def generate_short_code():

    characters = string.ascii_letters + string.digits

    short_code = ''.join(
        random.choice(characters)
        for i in range(6)
    )

    return short_code


@api_view(['POST'])
def signup(request):

    username = request.data.get('username')

    password = request.data.get('password')

    if User.objects.filter(username=username).exists():

        return Response({
            'error': 'Username already exists'
        })

    User.objects.create_user(
        username=username,
        password=password
    )

    return Response({
        'message': 'User created successfully'
    })


@api_view(['POST'])
def login(request):

    username = request.data.get('username')

    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:

        return Response({
            'message': 'Login successful',
            'user_id': user.id,
            'username': user.username
        })

    return Response({
        'error': 'Invalid credentials'
    })


@api_view(['POST'])
def create_short_url(request):

    user_id = request.data.get('user_id')

    title = request.data.get('title')

    original_url = request.data.get('original_url')

    user = User.objects.get(id=user_id)

    user_urls_count = ShortURL.objects.filter(
        user=user
    ).count()

    if user_urls_count >= 5:

        return Response({
            'error': 'Maximum 5 URLs allowed'
        })

    short_code = generate_short_code()

    short_url = ShortURL.objects.create(
        user=user,
        title=title,
        original_url=original_url,
        short_code=short_code
    )

    serializer = ShortURLSerializer(short_url)

    return Response(serializer.data)


@api_view(['GET'])
def list_urls(request):

    user_id = request.GET.get('user_id')

    search = request.GET.get('search', '')

    urls = ShortURL.objects.filter(
        user_id=user_id
    )

    if search:

        urls = urls.filter(
            title__icontains=search
        )

    serializer = ShortURLSerializer(
        urls,
        many=True
    )

    return Response({
        'data': serializer.data,
        'total_pages': 1
    })


@api_view(['PUT'])
def update_url(request, id):

    short_url = ShortURL.objects.get(id=id)

    short_url.title = request.data.get('title')

    short_url.original_url = request.data.get('original_url')

    short_url.save()

    return Response({
        'message': 'URL updated successfully'
    })


@api_view(['DELETE'])
def delete_url(request, id):

    short_url = ShortURL.objects.get(id=id)

    short_url.delete()

    return Response({
        'message': 'URL deleted successfully'
    })