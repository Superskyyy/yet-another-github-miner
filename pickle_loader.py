import pickle

from utils.pretty_print import pretty_print

with open('spider/first_batch_1000_bestmatch.pkl', 'rb') as data:
    loaded = pickle.load(data)
    pretty_print(loaded)
