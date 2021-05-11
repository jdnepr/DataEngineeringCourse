import random as r


def get_jokes(number, flag=1):
    """ Function returns jokes created from three lists
        :number: amount of jokes to be created
        :flag: if 1 - repetition of words allowed, if 0 - repetition of words not allowed
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    size = len(nouns)
    if number > size and not flag:
        return print(f"Impossible to create phrases with non-repeated words. "
                     f"Please, chose number less than {size + 1}.")

    for i in range(number):
        idx_noun, idx_adv, idx_adj = r.randrange(size)

        noun = nouns[idx_noun]
        adverb = adverbs[idx_adv]
        adjective = adjectives[idx_adj]

        print(f'{noun} {adverb} {adjective}')

        if not flag and size:
            # replace selected element with the last element of the list
            # reduce size by one
            nouns[idx_noun] = nouns[size - 1]
            adverbs[idx_adv] = adverbs[size - 1]
            adjectives[idx_adj] = adjectives[size - 1]
            size -= 1


get_jokes(number=5, flag=0)

