from django.db import models


class Question(models.Model):
    test = models.ForeignKey(
        "trials.Test",
        on_delete=models.SET_NULL,
        null=True,
        related_name="questions"
    )
    name = models.CharField(max_length=200, default="")
    description = models.TextField()

    def get_answers_secret(self):
        return [
            answer.get_secret_answer()
            for answer in self.answers.all()
        ]
