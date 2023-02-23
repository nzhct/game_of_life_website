from django.shortcuts import render


def about(request):
    return render(request, 'abouttemplates/about.html')


def contacts(request):
    return render(request, 'abouttemplates/contacts.html')

def secret(request):
    return render(request, 'abouttemplates/secret.html')
