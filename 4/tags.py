import os
from collections import Counter
import urllib.request
import re

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    blogs = []
    content = f.read().lower()
    exp = ("<category>(.*?)</category")
    pattern = re.compile(exp, re.IGNORECASE )
    for match in pattern.finditer(content):
        blogs.append(match.group(1))
        

count = Counter(blogs)

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    return count.most_common(n)
    pass   

