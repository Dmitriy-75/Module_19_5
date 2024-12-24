from django.shortcuts import render
from .models import Game, Buyer, News
from django.http import HttpResponse
from django.core.paginator import Paginator



# Create your views here.


# Добавить вью news, которая будет возвращать отрендеренный 'news.html' и контекст, содержащий поле news - объект страницы,
# полученный с помощью Paginator из модуля django.core.paginator, как в примере из видео-урока.


def news(request):
    news = News.objects.all()
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_news = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': page_news})

def menu(request):
    title = "Игровая платформа"
    text = "Главная страница"
    context = {
        "title": title,
        "text": text
    }
    return render(request, 'main_page.html', context)


def basket(request):
    text1 = "Корзина"
    text2 = "Извините, Ваша корзина пуста"

    context = {
        "text1": text1,
        "text2": text2
    }
    return render(request, 'basket.html', context)


def shop(request):
    games = Game.objects.all()

    context = {
        "games": games,
    }
    return render(request, 'shop.html', context)


def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        balance = request.POST.get('balance')
        age = request.POST.get('age')

        for i in users:
            if i.name == username:
                info['error'] = 'Пользователь уже  существует'

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'

        if not info:
            info['hello'] = f'Приветствуем, {username}!'
            Buyer.objects.create(name=username, balance=balance, age=age)

        print(f'username={username}')
        print(f'password={password}')
        print(f'{balance}')
        print(f'age={age}')

        return render(request, "registration_page.html", info)

    return render(request, "registration_page.html", info)























