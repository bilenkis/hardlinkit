from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
import os

from django import forms
from os.path import join

from .models import dirTree

# import the logging library
import logging

def dirindex(request):

    # Get an instance of a logger
    logger = logging.getLogger(__name__)

    collection = os.getenv('COLLECTION', default = '/data')
    ind = 0
    for root, dirs, files in os.walk(collection):
        for d in dirs:
             obj, created = dirTree.objects.get_or_create(
                name=d,
                defaults={
                  'path': root,
                  'parent': ind,
                  'ftype': 'd',
                },
             )
        for f in files:
#             try:
#               dirobj = dirTree.objects.get(path__exact=root,ftype__exact='d')
#               dirid = dirobj.id
#               logger.error(dirid)
#             except dirTree.DoesNotExist:
#               dirid = 0
#               logger.error(dirid)
             obj, created = dirTree.objects.get_or_create(
                name=f,
                defaults={
                  'path': root,
                  'parent': ind,
                  'ftype': 'f',
                },
             )
        ind += 1

    obj_list_from_db = dirTree.objects.order_by('id')

    context = {
        'obj_list_from_db': obj_list_from_db,
    }

    return render(request, 'filebrowser/filetree.html', context)


def start(request):
  return render(request, 'filebrowser/start.html')

def filebrowser(request):
  return render(request, 'filebrowser/filebrowser.html')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

#def dirindex(request):
#
#    # Get an instance of a logger
#    logger = logging.getLogger(__name__)
#
#    collection = os.getenv('COLLECTION', default = '/data')
#    ind = 0
#    for root, dirs, files in os.walk(collection):
#        for d in dirs:
#             obj, created = dirTree.objects.get_or_create(
##                path=join(root,d),
#                path=root,
#                defaults={
#                'name': d,
#                'parent': ind,
#                'ftype': 'd',
#                 },
#             )
##            p = dirTree(name=d,path=join(root,d),parent=ind,ftype='d')
##            p.save()
#
#        for f in files:
##             logger.error(root)
#             try:
#               dirobj = dirTree.objects.get(path__exact=root,ftype__exact='d')
#               dirid = dirobj.id
#               logger.error(dirid)
#             except dirTree.DoesNotExist:
#               dirid = 0
#               logger.error(dirid)
#             obj, created = dirTree.objects.get_or_create(
##                path=join(root,f),
#                path=root,
#                defaults={
#                'name': f,
#                'parent': dirid,
#                'ftype': 'f',
#                 },
#             )
#            #p.save()
#
#        ind += 1
#
#    obj_list_from_db = dirTree.objects.order_by('id')
#
#    context = {
#        'obj_list_from_db': obj_list_from_db,
#    }
#
#    return render(request, 'filebrowser/filetree.html', context)



#    question = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choise = question.choise_set.get(pk=request.POST['choise'])
#    except (KeyError, Choise.DoesNotExist):
#        context = {
#            'question': question,
#            'error_message': "You didn't select a choise.",
#        }
#        return render(request, 'polls/detail.html', context)
#    else:
#        selected_choise.votes += 1
#        selected_choise.save()
#        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
