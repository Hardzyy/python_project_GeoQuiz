import random
import itertools


def get_random(obj):
    count = 1
    while True:
        if obj.query.get(count) is not None:
            count += 1
        else:
            break
    arrange = list(range(1, count))
    id_right = random.choice(arrange)
    del arrange[id_right-1]
    id_answers_prep = list(itertools.permutations(arrange, 3))
    id_answers = list(id_answers_prep[random.choice(range(len(id_answers_prep)))])
    id_answers.append(id_right)
    country = obj.query.get(id_right)
    random.shuffle(id_answers)
    answers = []
    answers.append(country)
    for i in id_answers:
        answers.append(obj.query.get(i))
    return answers
