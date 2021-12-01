from django.db import models
from django.db.models import Q
from django.db.models import UniqueConstraint


class Answer(models.Model):
    question = models.ForeignKey(
        "questions.Question",
        on_delete=models.CASCADE,
        null=False,
        related_name="answers"
    )
    description = models.TextField()
    is_correct = models.BooleanField(default=False)

    def get_secret_answer(self):
        return {
            "id": self.id,
            "description": self.description,
        }

    class Meta:
        constraints = [UniqueConstraint(
            fields=["question"],
            condition=Q(is_correct=True),
            name="only_one_correct_answer"
        )]
