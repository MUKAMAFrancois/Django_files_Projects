from django.shortcuts import render
from django.contrib.postgres.search import( 
    SearchVector,
    SearchRank,
    SearchQuery)
from book.models import Book
from book.forms import PostSearchForm

# Create your views here.

def post_search(request):
    form=PostSearchForm
    user_data=None
    results=[]
    if 'q' in request.GET:
        form=PostSearchForm(request.GET)
        if form.is_valid():
            user_data=form.cleaned_data['q']
          #  results=Book.objects.filter(title__icontains=data)
            results=Book.objects.annotate(search=SearchVector('title','authors')).filter(search=user_data) # search multiple fields
           
           
         #   vector=SearchVector('title')
          #  query=SearchQuery(user_data)
           # results=Book.objects.annotate(rank=SearchRank(vector,query)).order_by('-rank')# returns ranked results

          
           # SearchRank Weights
           #.....
           #A>B>C>D  # with which you give more importance, like abstract and body

           # vector=SearchVector('title', weight='A') +SearchVector('authors', weight='B')
           # query=SearchQuery(user_data)
           # results=Book.objects.annotate(rank=SearchRank(vector,query)).order_by('-rank')# returns ranked results

                # By Trigam Similarity
            from django.contrib.postgres.search import TrigramSimilarity,TrigramDistance
           # results=Book.objects.annotate(similarity=TrigramSimilarity('title',user_data),).filter(similarity__gte=0.1).order_by('-similarity')
          #  results=Book.objects.annotate(distance=TrigramDistance('title',user_data),).filter(distance__lte=0.5).order_by('distance')

        


          



    return render(request,'book/search-form.html',{'form':form, 'results':results, 'user_data':user_data})


