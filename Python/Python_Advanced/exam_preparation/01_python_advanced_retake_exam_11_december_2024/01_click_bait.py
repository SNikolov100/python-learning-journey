from collections import deque

suggested_links = deque(map(int, input().split()))
featured_articles = [int(x) for x in input().split()]
target_engagement_value = int(input())
sequence_of_greater_elements = []
final_feed_collection = []


while suggested_links and featured_articles:
    link = suggested_links.popleft()
    article = featured_articles.pop()

    if link > article:                          # links
        sequence_of_greater_elements.append(link)
        remainder = link % article
        final_feed_collection.append(-abs(remainder))
        if remainder != 0:
            suggested_links.append(remainder * 2)

    elif article > link:                                       #article
        sequence_of_greater_elements.append(article)
        remainder = article % link
        final_feed_collection.append(abs(remainder))
        if remainder != 0:
            featured_articles.append(remainder * 2)

    else:
        final_feed_collection.append(0)


print(f"Final Feed: {', '.join(str(x) for x in final_feed_collection)}")
total_engagement_value = sum(x for x in final_feed_collection)
if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    print(f"Goal not achieved! Short by: {target_engagement_value - total_engagement_value}")



