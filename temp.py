import requests
from mastodon import Mastodon
import csv
from pandas import json_normalize
import pandas as pd

url_endpoint = "/api/v1/trends/tags"

mastodon = Mastodon(api_base_url='https://mastodon.social')
response = mastodon.trending_tags()

activities = mastodon.instance_activity()[:12]

for item in activities:
    item['week'] = item['week'].strftime('%Y-%m-%d %H:%M:%S')
print(activities)

df = pd.DataFrame(activities)

# Save to CSV
df.to_csv('activities.csv', index=False)

# Normalize the JSON data into a flat table



# Assuming 'response' is your API response
# trends = response  # Replace with your actual response variable

# # Normalize the JSON data into a flat table
# df = json_normalize(trends, 'history', ['name', 'url'], 
#                     record_prefix='history_')

# # Save to CSV
# df.to_csv('trends.csv', index=False)

