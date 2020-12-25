from django.shortcuts import render

cards = [
    {
        'id': 1,
        'title': "mi primer app",
        'info': "django y boostrap",
        # 'tags': ['backend', 'django', 'css', 'jinja']
    },
    {
        'id': 2,
        'title': "mi primer api",
        'info': "flask y sqlalchemy",
        # tags': ['backend', 'flask', 'restful', 'api']
    },
    {
        'id': 3,
        'title': "mi primer website",
        'info': "reactjs  y bulma",
        # 'tags': ['backend', 'frontend', 'css', 'responsive']
    }
]


long = len(cards)


def home(request):
    return render(
                request,
                'landing/app.html',
                {'cards': cards, 'range': range(long)})
