from django.shortcuts import render
import os

def dirindex(request):
    rootDir = '/Users/bilen/music'
    dirnameTree = []
    subdirTree = []
    fileTree = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        subdirTree.append(subdirList)
        fileTree.append(fileList)

    for i, v in enumerate(subdirTree):
        subdirIndex.append(i)

    context = {
        'subdirIndex': subdirIndex,
        'subdirTree': subdirTree,
        'fileTree': fileTree,
    }
    return render(request, 'filebrowser/filetree.html', context)
