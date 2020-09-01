from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse
from searchengine import listservice
from searchPDF import settings
import os

# Create your views here.
def listPDF(request):

    search = request.GET.get('search')

    if search is None:
        return render(request, 'search.html')

    pdf_any = []
    context = {}

    keys_and = search.split("AND")
    list_of_best_pdfs = listservice.getBestFiles(keys_and)
    list_of_any_pdfs = listservice.getAnyFiles(keys_and)

    keys_or = search.split("OR")
    list_of_or_pdfs = listservice.getAnyFiles(keys_or)

    if keys_and[0] == '' and keys_or[0] == '':
        context = {
            'empty': "Please enter a keyword"
        }
        return render(request, 'search.html', context)

    if len(keys_and) >= 1 and len(keys_or) == 1:
        context['keys'] = keys_and
    else:
        context['keys'] = keys_or


    for fileany in list_of_any_pdfs:
        flag = True
        for filebest in list_of_best_pdfs:
            if filebest == fileany:
                flag = False
        if flag == True:
            pdf_any.append(fileany)

    if not list_of_best_pdfs and not list_of_any_pdfs and not list_of_or_pdfs:
        context['notmatch'] = "No results found"
    else:
        if list_of_best_pdfs:
            context['bestfiles'] = list_of_best_pdfs
            context['bestresult'] = True
            context['bestsize'] = len(list_of_best_pdfs)

        if list_of_or_pdfs:
            context['bestfiles'] = list_of_or_pdfs
            context['bestresult'] = True
            context['bestsize'] = len(list_of_or_pdfs)

        if pdf_any:
            context['anyfiles'] = pdf_any
            context['anyresult'] = True
            context['anysize'] = len(pdf_any)

    return render(request, 'search.html', context)


def getPDF(request, filename):
    try:
        path = os.path.join(settings.STATIC_ROOT + '/Data', filename)
        return FileResponse(open(path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def handler400(request, exception=None):
    return render(request, 'error.html', status=404)

