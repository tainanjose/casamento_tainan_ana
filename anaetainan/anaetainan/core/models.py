from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "done": self.done,
        }


class QuizResult(models.Model):
    nome = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.nome} ({self.time}): {self.score}/7"
