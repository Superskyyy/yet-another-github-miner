import pickle

from utils.pretty_print import pretty_print

with open('spider/first_batch_1000_bestmatch.pkl', 'rb') as data:
    loaded = pickle.load(data)
    pretty_print(loaded)
    # all 194 urls
    # for key in loaded:
    #     print(key)

    # print([key for key in loaded])

    # print(loaded.values())

    import itertools

    flat_vals = list(itertools.chain.from_iterable(loaded.values()))

