import random as r


def get_jokes(number):
    """ Function returns jokes created from three lists
        :number: amount of jokes to be created
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(number):
        print(f'{r.choice(nouns)} {r.choice(adverbs)} {r.choice(adjectives)}')


get_jokes(2)



