from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render, get_object_or_404, redirect
from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def home(request):
    question = Question.objects.new()
    paginator, page = Paginator(request, question)
    render(request, 'qa/home.html', {
        'question': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular(request):
    question = Question.objects.popular()
    paginator, page = Paginator(request, question)
    render(request, 'qa/popular.html', {
        'question': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def question(request, pk=id):
    question = get_object_or_404(Question, id=pk)
    return render(request, 'qa/question.html', {
        'question': question,
    })


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page
