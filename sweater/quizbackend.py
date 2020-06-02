import random

from sweater.models import country_capital_easy


def get_random(obj):
    count = 1
    while True:
        if country_capital_easy.query.get(count) is not None:
            count += 1
        else:
            break
    count -= 1
    arange = range(1, count+1)
    id_answers = random.choices(arange, k=count)
    id_right = random.choice(id_answers)
    country = country_capital_easy.query.get(id_right).name
    answers = []
    answers[0] = country
    for i in range(1, count+1);
        answers[i] = country_capital_easy.query.get(i).capital
