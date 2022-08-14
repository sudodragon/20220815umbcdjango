from django.conf import settings
import random

with open("../../../DATA/words.txt") as words_in:
    WORDS = [w.rstrip() for w in words_in]

def random_word(request):
    return {
        'RANDOM_WORD': random.choice(WORDS)
    }

def secret_word(request):
    return {
        'SECRET_WORD': settings.SECRET_WORD
    }

def dump_request(request):
    return {
        'REQUEST_DUMP': [
            (r, type(getattr(request, r)).__name__)
            for r in dir(request)
            if not r.startswith('_')
        ]
    }
