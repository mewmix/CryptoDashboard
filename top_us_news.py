from gnews import GNews

google_news = GNews()
us_news = google_news.get_news('United States')
title = us_news[0]["title"]
url = us_news[0]["url"]
publisher = us_news[0]["publisher"]
date = us_news[0]["published date"]
print(f"The top US Story is {title}")
print(f"{url}")
print(f"{date}")