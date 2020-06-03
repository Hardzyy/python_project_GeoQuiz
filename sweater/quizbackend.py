import random
import itertools

def get_random(obj):
    count = 1
    while True:
        if obj.query.get(count) is not None:
            count += 1
        else:
            break
    arrange = range(1, count)
    id_answers_prep = list(itertools.permutations(arrange, 4))
    id_answers = list(id_answers_prep[random.choice(range(len(id_answers_prep)))])
    id_right = random.choice(id_answers)
    country = obj.query.get(id_right)
    right_name = country.name
    random.shuffle(id_answers)
    answers = []
    answers.append(right_name)
    for i in id_answers:
        answers.append(obj.query.get(i).capital)
    return answers
