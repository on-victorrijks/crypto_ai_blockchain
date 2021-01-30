from django.shortcuts import render


def index(request):
    context = {
        'menuItems': [
            {
            'title': 'Hello',
            'link': 'Linked'
            }
        ]
    }
    return render(request, 'index.html', context)