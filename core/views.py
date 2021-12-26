from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from core.models import Tweet, HashTag


# Create your views here.


def splash(request):
    return render(request, 'splash.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'splash.html', {})


def signup(request):
    user = User.objects.create_user(username=request.POST['username'],
                                    password=request.POST['password'])
    login(request, user)
    return redirect('home')


def home(request):
    for hashtag in HashTag.objects.all():
        if hashtag.tweet.count() is 0:
            hashtag.delete()
    context = {'Tweets': reversed(Tweet.objects.all()), 'HashTags': HashTag.objects.all()}
    return render(request, 'home.html', context)


def post(request):
    if request.method == "POST":
        body = request.POST["body"]
        author = request.user
        tweet = Tweet.objects.create(body=body, author=author)
        if body.find('#') != -1:
            curr = body.find('#')
            if curr != 0:
                if body[curr - 1] != ' ':
                    return redirect('home')
            hashtag = ''
            while body[curr] != ' ':
                hashtag = hashtag + body[curr]
                curr = curr + 1
                if curr >= len(body):
                    break
            if (len(hashtag) == 1) or (len(hashtag) > 139):
                return redirect('home')
            if not HashTag.objects.filter(hashtag=hashtag).exists():
                hashtag_object = HashTag.objects.create(hashtag=hashtag, tag=hashtag[1:len(hashtag)])
                hashtag_object.tweet.add(tweet)
                hashtag_object.save()
            else:
                hashtag_created = HashTag.objects.get(hashtag=hashtag)
                hashtag_created.tweet.add(tweet)
                hashtag_created.save()
    return redirect('home')


def like(request, id):
    tweet = Tweet.objects.get(id=id)
    if request.user.id in tweet.people:
        tweet.likes -= 1
        tweet.people.remove(request.user.id)
    elif request.user.id not in tweet.people:
        tweet.likes += 1
        tweet.people.append(request.user.id)
    tweet.save()
    if request.path == '/home/like/' + id:
        return redirect('home')
    elif request.path == '/profile/like/' + id:
        return redirect('profile', tweet.author.id)


def profile(request, id):
    if id == '-2':
        return redirect('home')
    if request.method == "GET":
        username = User.objects.get(id=id).username
        context = {'Tweets': reversed(Tweet.objects.filter(author=id)), 'name': username}
        return render(request, 'profile.html', context)


def hashtag(request, tag):
    if tag == '-2':
        return redirect('home')
    if request.method == "GET":
        context = {'HashTags': HashTag.objects.get(tag=tag).tweet.all(), 'tag': HashTag.objects.get(tag=tag).hashtag,
                   'fulltag': HashTag.objects.get(tag=tag).tag}
        return render(request, 'hashtag.html', context)


def logout(request):
    return redirect('splash')


def hashtaglike(request, id, tag):
    tweet = Tweet.objects.get(id=id)
    if request.user.id in tweet.people:
        tweet.likes -= 1
        tweet.people.remove(request.user.id)
    elif request.user.id not in tweet.people:
        tweet.likes += 1
        tweet.people.append(request.user.id)
    tweet.save()
    return redirect('hashtag', tag)


def delete(request, id):
    tweet = Tweet.objects.get(id=id)
    tweet.delete()
    if request.path == '/home/delete/' + id:
        return redirect('home')
    elif request.path == '/profile/delete/' + id:
        return redirect('profile', tweet.author.id)


def hashtagdelete(request, id, tag):
    tweet = Tweet.objects.get(id=id)
    tweet.delete()
    return redirect('hashtag', tag)