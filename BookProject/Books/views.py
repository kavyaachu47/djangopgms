from django.shortcuts import render,redirect
from Books.forms import BookCreateForm,BookUpdate
from Books.models import Book
# Create your views here.
#create a book
def bookCreate(request):
    template_name="bookcreate.html"
    form=BookCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            # book_name=form.cleaned_data.get("book_name")
            # author=form.cleaned_data.get("author")
            # price=form.cleaned_data.get("price")
            # pages=form.cleaned_data.get("pages")
            #
            # obj=Book(book_name=book_name,author=author,price=price,pages=pages)
            # obj.save()
            form.save() # list all books
            return redirect("listbook")
        else:
            context={}
            context["form"]=form
            return render(request, template_name, context)
    return render(request,template_name,context)



#listing  books
def listbook(request):
    template_name = "listbook.html"
    qs = Book.objects.all()
    context = {}
    context["books"] = qs
    return render(request, template_name, context)
#detail view of a particular books
def viewBook(request,pk):
    template_name="viewpage.html"
    qs=Book.objects.get(id=pk)
    context={}
    context["book"]=qs
    return render(request,template_name,context)
#delete
def deletebook(request,pk):

    Book.objects.get(id=pk).delete()
    return redirect("listbook")
#update
def updatebook(request,pk):
    book=Book.objects.get(id=pk)
    form=BookCreateForm(instance=book)
    context={}
    context["form"]=form

    if request.method=="POST":
        form=BookUpdate(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbook")
    return render(request,"updatebook.html",context)

