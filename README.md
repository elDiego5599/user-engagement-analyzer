# User Engagement Analyzer

This project provides a simple script to calculate user engagement scores based on interaction data.

## Functionality

The `analyzer.py` script contains a function, `calculate_engagement_score`, which reads data from `engagement_data.csv` and computes a weighted average score.

### Data Schema (`engagement_data.csv`)

| Column      | Type    | Description                               |
|-------------|---------|-------------------------------------------|
| post_id     | integer | Unique identifier for the post.           |
| user_id     | string  | Identifier for the user who made the post.|
| likes       | integer | Number of likes received.                 |
| comments    | integer | Number of comments received.              |
| shares      | integer | Number of shares.                         |
| impressions | integer | Total number of times the post was seen.  |

## Usage

The script is intended for internal data analysis and reporting.
