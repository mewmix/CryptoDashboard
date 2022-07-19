from gnews import GNews
import random
google_news = GNews()
us_news = google_news.get_news('United States')

count = len(us_news)

# Create a random number between 1 and count
random_number = random.randint(1, count) 
# Get the random news story
random_story = us_news[random_number] 
# Print the random story
print(f"Story# {random_number} of {count} -  {random_story['title']}")
print(random_story['description'])