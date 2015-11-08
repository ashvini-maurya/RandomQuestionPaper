__author__ = 'ashvini'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RandomQuestionPaper.settings')

import django
django.setup()

from paper.models import Question, Category, Subject

def populate():
    easy_cat = add_cat('Easy')

    add_page(cat=easy_cat,
             question="Question #1",
             subject="Divide Rs.500 among Suresh and Awanti in the ratio 3 : 7")

    add_page(cat=easy_cat,
             question="Question #2",
             subject="The sum of two integers is 17. If one of them is -35, find the other.")

    medium_cat = add_cat('Medium')

    add_page(cat=medium_cat,
             question="Question #1",
             subject="Draw a rough sketch of a quadrilateral PQRS. Draw its diagonals. Name them.")

    add_page(cat=medium_cat,
             question="Question #2",
             subject="Write the fraction 3/8 as a decimal number")

    hard_cat = add_cat("Hard")

    add_cat(cat=hard_cat,
            question="Question #1",
            subject="If two adjacent sides of a rectangle are 4x + 7y and 3y - x, find its perimeter.")

    add_cat(cat=hard_cat,
            question="Question #2",
            subject="Namita travells 20km 50m everyday. Out of this she travells 10km 200m by bus and the rest by auto.\
                How much distance does she travells by auto?")

    for c in Category.objects.all():
        for p in Question.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, question, subject):
    q = Question.objects.get_or_create(category=cat, question=question, subject=subject)[0]
    q.question=question
    q.save()
    return q

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def add_cat(name):
    s = Subject.objects.get_or_create(name=name)[0]
    return s

if __name__ == "__main__":
    print "Starting Paper poplation script..."
    populate()