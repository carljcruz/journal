from django.shortcuts import render


# homepage
def homepage(request):
    template_name = 'notes/home.html'
    context = {
        'Hello': 'Hello'
    }
    return render(request ,template_name, context=context)
