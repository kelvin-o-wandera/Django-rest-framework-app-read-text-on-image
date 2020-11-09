from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberPaginationDataOnly(PageNumberPagination):

    def next_link(self):
        if not self.page.has_next():
            return 0
        return self.get_next_link()

    def previous_link(self):
        if not self.page.has_previous():
            return 0
        return self.get_previous_link()

    def get_paginated_response(self, data):

        return Response({
            'next': self.next_link(),
            'previous': self.previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })
