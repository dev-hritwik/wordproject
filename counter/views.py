from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'counter/home.html')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    dictionary = {}
    for w in words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
    return render(request,'counter/count.html',{'fulltext':fulltext , 'count':len(words),'dictionary':dictionary.items()})
 


