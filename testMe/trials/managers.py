from django.db.models import Manager
from django.apps import apps
from django.conf import settings
from categories.models import Category


class TestManager(Manager):

    def create(
            self, *,
            category=None,
            questions=[],
            **kwargs
    ):
        Question = apps.get_model("questions", "Question")
        Answer = apps.get_model("answers", "Answer")
        category = category

        instance = super().create(
            name=kwargs.get("name"),
            passing_score=kwargs.get("passing_score"),
            category=category[0]
        )
        # import pdb;pdb.set_trace()
        for question in questions:
            question_instance = Question.objects.create(
                name=question["name"],
                description=question["description"],
                test=instance
            )
            for answer in question["answers"]:
                Answer.objects.create(
                    description=answer["description"],
                    is_correct=answer["is_correct"],
                    question=question_instance
                )

        return instance
