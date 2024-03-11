# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Question
# import pandas as pd
# import os
# from django.conf import settings
#
#
# @receiver(post_save, sender=Question)
# def export_question_data(sender, instance, **kwargs):
#     all_questions = Question.objects.all()
#     df = pd.DataFrame(list(all_questions.values()))
#     df[['question_text', 'answer']].to_csv(os.path.join(settings.DATA_DIR,'all_questions.txt'), sep='\t', index=False)

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Question
from django.conf import settings
import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Question


@receiver(post_save, sender=Question)
def export_question_data(sender, instance, **kwargs):
    question = instance
    file = os.path.join(settings.DATA_DIR, 'all_questions.txt')
    with open(file, 'a') as file:
        file.write(f"Question: {question.question_text}\n")
        file.write(f"Answer: {question.answer}\n\n")


