from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Movie

# Create your views here.
@login_required(login_url='/login/')
def register_movie(request):
    movie_id = request.GET.get('id')
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        if movie.user == request.user:
            return render(request, 'register-movie.html', {'movie':movie})
    return render(request, 'register-movie.html')

@login_required(login_url='/login/')
def set_movie(request):
    title = request.POST.get('title')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    description = request.POST.get('description')
    photo = request.FILES.get('file')
    movie_id = request.POST.get('movie-id')
    user = request.user
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        if user == movie.user:
            movie.genre = genre
            movie.score = score
            movie.title = title
            movie.description = description
            if photo:
                movie.photo = photo
            movie.save()
    else:
        movie = Movie.objects.create(genre=genre, score=score, title=title, description=description, photo=photo, user=user)
    url = '/movie/detail/{}/'.format(movie.id)
    return redirect(url)

@login_required(login_url='/login/')
def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    if movie.user == request.user:
        movie.delete()
    return redirect('/')



@login_required(login_url='/login/')
def list_all_movies(request):
    movie = Movie.objects.filter(active=True)
    return render(request, 'list.html', {'movie':movie})

def list_user_movies(request):
    movie = Movie.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'movie':movie})

def movie_detail(request, id):
    movie = Movie.objects.get(active=True, id=id)
    return render(request, 'movie.html', {'movie':movie})

def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha invalido.')
    return redirect('/login/')

    