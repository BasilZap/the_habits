from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """ Пагинатор с выводом по 5 привычек на страницу """
    page_size = 5
    page_size_query_param = 'page_size'

