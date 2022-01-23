from django.db.models import Manager
from django.apps import apps
from django.conf import settings
from categories.models import Category


class QuestionManager(Manager):
    def create(
        self, *,
        answers=[],
        name=None,
        test=None,
        description=None,
        **kwargs
    ):
        Answer = apps.get_model("answers", "Answer")
        instance = super().create(
            name=name,
            test=test,
            description=name,
        )
        for answer in answers:
            Answer.objects.create(
                question=instance,
                description=answer["description"],
                is_correct=answer["is_correct"]
            )
        return instance

