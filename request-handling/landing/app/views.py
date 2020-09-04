from collections import Counter

from django.http import HttpResponse
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing = request.GET.get('from-landing')
    counter_click[from_landing] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    landing = request.GET.get('ab', 'original')
    counter_show[landing] += 1
    if landing == 'test':
        return render_to_response('landing_alternate.html')
    return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # НЕ НУЖНО - проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    try:
        test = counter_click.get('test') / counter_show.get('test')
        origin = counter_click.get('original') / counter_show.get('original')
        return render_to_response('stats.html', context={
        'test_conversion': round(test, 1),
        'original_conversion': round(origin, 1),
        })
    except TypeError or ValueError as e:
        msg = f'Не хватает просмотров по landing {counter_show} или не было переходов {counter_click}- {e}'
        return HttpResponse(msg)
