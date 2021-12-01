from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=100)
    passing_score = models.PositiveSmallIntegerField()

    def get_score(self, answers):
        """
        [
            {
                "question": 1,
                "answer": 1
            },
            {
                "question": 2,
                "answer": 1
            }
        ]
        """
        points = 0
        for answer in answers:
            question = self.questions.get(id=answer["question"])
            if question.answers.get(id=answer["answer"]).is_correct:
                points += question.points
        return points
