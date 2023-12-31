from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.conf import settings

def get_users(request):
    express_api_proxy_url = settings.EXPRESS_API_PROXY_URL
    response = requests.get(f'{express_api_proxy_url}/users')
    
    if response.status_code == 200:
        users = response.json()
        return render(request, 'users.html', {'users': users})
    else:
        return JsonResponse({'error': 'Failed to fetch users from Express API'}, status=500)
