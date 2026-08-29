from news.news_api_client import NewsAPIClient

client = NewsAPIClient()

data = client.search_articles("India")


print("status:",data["status"])
print("Number of articles:", len(data["articles"]))

for article in data["articles"][:5]:
    print()
    print("Title:", article["title"])
    print("Source:", article["source"]["name"])
    print("Published:", article["publishedAt"])