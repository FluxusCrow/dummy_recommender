'''
dummy recommender recommending random movies
'''

import pandas as pd


def recommend_random(movies, k=10):
    """
    Dummy recommender that recommends a list of random movies. Ignores the actual query.
    """
    return movies['title'].sample(k).to_list()
