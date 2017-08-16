from django.shortcuts import render
from django.http import Http404
from people.models import Person
from .forms import PostForm
from django.shortcuts import redirect

def index(request):
    persons =  Person.objects.all()
    return render(request, 'people/index.html',{
        'persons' : persons,
    })

def list_detail(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404('This Person does not exist')
    return render(request, 'people/list.html', {
        'person' : person,
    })
    
def list_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('list_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'people/list_edit.html', {'form': form})





