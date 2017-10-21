from django.core.paginator import Paginator, InvalidPage, EmptyPage


def pagination(queryset, per_page=20, page=1):
    paginator = Paginator(queryset, per_page)

    try:
        page = int(page)
    except ValueError:
        page = 1

    try:
        items = paginator.page(page)
    except (EmptyPage, InvalidPage):
        items = paginator.page(paginator.num_pages)

    return items
