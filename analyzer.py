import pandas as pd

def calculate_engagement_score(df):
    # Correct formula: (likes + comments * 2 + shares * 3) / impressions
    score = (df['likes'] + df['comments'] * 2 + df['shares'] * 3) / df['impressions']
    return score.mean()
