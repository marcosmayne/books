from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,

)

from main.forms import (
    GenreForm,
    AuthorForm,
    PublisherForm,
    BookForm,
)

from main.models import (
    Genre,
    Author,
    Publisher,
    Book
)

from django.http import Http404, HttpResponseRedirect
from PIL import Image, ImageChops, ImageFilter

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

#=================================================================================

def home_view(request):
    return render(request, 'main/home.html')

#=================================================================================
# GENRE

def genre_list_view(request):
    # genre_list,
    # GET /genre/
    # Obter todos os models (queryset), adicionar variável no contexto e renderizar o template main/genre/list.html

    # pega todos os generos no bd e retorna numa queryset
    genre_list = Genre.objects.order_by('name').all()
    genre_count = Genre.objects.count()
    # disponibiliza a queryset no template atraves da variavel context dict
    context = {'genre_list': genre_list, 'genre_count': genre_count}

    # envia a variavel context para o template
    return render(request, 'main/genre/list.html', context)


def genre_detail_view(request, id):
    # GET /genre/<int:id>
    # Obter apenas o model por <id>, adicionar variável no contexto e renderizar o template main/genre/detail.html
    genre = get_object_or_404(Genre, id=id)
    context = {'genre' : genre}
    return render(request, 'main/genre/detail.html', context)


#@login_required(login_url='/user/login/', redirect_field_name=None)
def genre_create_view(request):
    # GET /genre/create
    # Criar o form vazio, adicionar variável no contexto e renderizar o template main/genre/create.html
    if request.method == "GET":
        form = GenreForm()
        context = {'form': form}
        return render(request, 'main/genre/create.html', context)

    # POST /genre/create
    # Criar o form com os dados do request.POST, verifica se o form é válido, salva o formulário com os dados e
    # redireciona para a view genre_detail
    if request.method == "POST":
        # cria uma instância de formulário e a preenche com os dados da requisição
        form = GenreForm(request.POST)
        # verifica se o formulário é válido (retorna True)
        if form.is_valid():
            # processa os dados no dicionário form.cleaned_data conforme necessário
            form.save()
            # redireciona para uma nova URL
            return redirect('genre_list')
        else:
            context = {"form": form}
            return render(request, 'main/genre/create.html', context)

#@login_required(login_url='/user/login/', redirect_field_name=None)
def genre_update_view(request, id):
    # GET /genre/<int:id>/update
    # Obter o model por id, criar o form com instance=model, adicionar a variavel no contexto e renderizar o
    # template main/genre/update.html
    if request.method == "GET":
        genre = Genre.objects.get(id=id)
        form = GenreForm(instance=genre)
        context = {'form': form}
        return render(request, 'main/genre/update.html', context)

    # POST /genre/<int:id>/update
    # Obter o model por id, criar o form com instance=model, verificar se o form é válido, salvar o formulário
    # e redirecionar para a view genre_detail
    else:
        genre = Genre.objects.get(id=id)
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')


#@login_required(login_url='/user/login/', redirect_field_name=None)
def genre_delete_view(request, id):
    # GET /genre/<int:id>/delete
    # Obter o model por id, adicionar a variável no contexto e renderizar o template main/genre/delete.html,
    # no template criar um form vazio apenas com uma mensagem de confirmação para apagar o model e um botão submit.
    if request.method == "GET":
        genre = Genre.objects.get(id=id)
        context = {'genre': genre}
        return render(request, 'main/genre/delete.html', context)

    # POST /genre/<int:id>/delete
    # Obter o model por id, deletar o model e redirecionar para a view genre_list
    else:
        genre = Genre.objects.get(id=id)
        genre.delete()
        return redirect('genre_list')

#=================================================================================
# AUTHOR

def author_list_view(request):
    author_list = Author.objects.order_by('name').all()
    author_count = Author.objects.count()
    context = {'author_list': author_list, 'author_count': author_count}
    return render(request, 'main/author/list.html', context)


def author_detail_view(request, id):
    author = get_object_or_404(Author, id=id)
    context = {'author' : author}
    return render(request, 'main/author/detail.html', context)


def author_create_view(request):
    if request.method == "GET":
        form = AuthorForm()
        context = {'form': form}
        return render(request, 'main/author/create.html', context)

    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
        else:
            context = {"form": form}
            return render(request, 'main/author/create.html', context)


def author_update_view(request, id):
    if request.method == "GET":
        author = Author.objects.get(id=id)
        form = AuthorForm(instance=author)
        context = {'form': form}
        return render(request, 'main/author/update.html', context)

    else:
        author = Author.objects.get(id=id)
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')


def author_delete_view(request, id):
    if request.method == "GET":
        author = Author.objects.get(id=id)
        context = {'author': author}
        return render(request, 'main/author/delete.html', context)

    else:
        author = Author.objects.get(id=id)
        author.delete()
        return redirect('author_list')


#=================================================================================
# PUBLISHER

def publisher_list_view(request):
    publisher_list = Publisher.objects.order_by('name').all()
    publisher_count = Publisher.objects.count()
    context = {'publisher_list': publisher_list, 'publisher_count': publisher_count}
    return render(request, 'main/publisher/list.html', context)


def publisher_detail_view(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    context = {'publisher' : publisher}
    return render(request, 'main/publisher/detail.html', context)


def publisher_create_view(request):
    if request.method == "GET":
        form = PublisherForm()
        context = {'form': form}
        return render(request, 'main/publisher/create.html', context)

    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
        else:
            context = {"form": form}
            return render(request, 'main/publisher/create.html', context)


def publisher_update_view(request, id):
    if request.method == "GET":
        publisher = Publisher.objects.get(id=id)
        form = PublisherForm(instance=publisher)
        context = {'form': form}
        return render(request, 'main/publisher/update.html', context)

    else:
        publisher = Publisher.objects.get(id=id)
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')


def publisher_delete_view(request, id):
    if request.method == "GET":
        publisher = Publisher.objects.get(id=id)
        context = {'publisher': publisher}
        return render(request, 'main/publisher/delete.html', context)

    else:
        publisher = Publisher.objects.get(id=id)
        publisher.delete()
        return redirect('publisher_list')

#=================================================================================
# BOOK

def book_list_view(request):
    book_list = Book.objects.all().order_by('title')
    context = {'book_list': book_list}
    return render(request, 'main/book/list.html', context)


def book_detail_view(request, id):
    book = get_object_or_404(Book, id=id)
    context = {'book' : book}
    return render(request, 'main/book/detail.html', context)


def book_create_view(request):
    if request.method == "GET":
        form = BookForm()
        context = {'form': form}
        return render(request, 'main/book/create.html', context=context)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            context = {"form": form}
            return render(request, 'main/book/create.html', context=context)


def book_update_view(request, id):
    if request.method == "GET":
        book = Book.objects.get(id=id)
        form = BookForm(instance=book)
        context = {'form': form}
        return render(request, 'main/book/update.html', context=context)

    else:
        book = Book.objects.get(id=id)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book.image = form.cleaned_data["image"]
            if not book.image:
                book.image = "images/no_image.png"
            print(book.image)
            form.save()
            return redirect('book_list')


def book_delete_view(request, id):
    if request.method == "GET":
        book = Book.objects.get(id=id)
        context = {'book': book}
        return render(request, 'main/book/delete.html', context=context)

    else:
        book = Book.objects.get(id=id)
        # remove image book
        book.image.delete(save=True)
        book.delete()
        return redirect('book_list')


def book_image_upload_view(request, id):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/book")

    else:
        form = BookForm()
    return render (request, 'main/book/list.html', {'form':form})

#=================================================================================
"""
# USER

def user_list_view(request):
    user_list = User.objects.all()
    return render(request, 'main/user/list.html', {'user_list': user_list})


def user_detail_view(request, id):
    try:
        user = User.objects.get(id=id)
        return render(request, 'main/user/detail.html', {
            'user_model': user
        })
    except User.DoesNotExist:
        raise Http404


def user_create_view(request):

    if request.method == 'GET':
        # create an empty form
        user_create_form = UserCreateForm()
        return render(request, 'main/user/create.html', {'form': user_create_form})

    if request.method == 'POST':
        # check if the form is valid
        user_create_form = UserCreateForm(request.POST or None)
        if user_create_form.is_valid():
            user_create_form.save()
            return redirect('/user/login/')
        else:
            # form is invalid!
            return render(request, 'main/user/create.html', {'form': user_create_form})

def user_login_view(request):

    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'main/user/login.html', {
            'form': form
        })

    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        return render(request, 'main/user/login.html', {'form': form})


def user_logout_view(request):
    logout(request)
    return redirect('/')
"""
