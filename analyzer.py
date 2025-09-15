import pandas as pd

def calculate_engagement_score(df):
    score = (df['likes'] + df['comments'] * 2) / df['impressions']
    return score.mean()
