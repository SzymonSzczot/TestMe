from django.db.models import QuerySet


class UserQuerySet(QuerySet):

    def activated(self, **kwargs):
        return self.filter(is_activated=True)