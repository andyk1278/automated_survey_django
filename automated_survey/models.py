from django.db import models
from django.core.exceptions import ValidationError

class Survey(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Question(models.Model):
    TEXT = 'text'
    YES_NO = 'yes-no'
    NUMERIC = 'numeric'

    QUESTION_KIND_CHOICES = (
        (TEXT, 'Text'),
        (YES_NO, 'Yes or no'),
        (NUMERIC, 'Numeric')
    )

    body = models.CharField(max_length=255)
    kind = models.CharField(max_length=255, choices=QUESTION_KIND_CHOICES)
    survey = models.ForeignKey(Survey)

    def __str__(self):
        return self.body

class QuestionResponse(models.Model):
    response = models.CharField(max_length=255)
    call_sid = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.response

    def as_dict(self):
        return {
                'body': self.question.body,
                'kind': self.question.kind,
                'response': self.response,
                'call_sid': self.call_sid,
                'phone_number': self.phone_number,
                }