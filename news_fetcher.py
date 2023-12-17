import re
import feedparser
import requests
from bs4 import BeautifulSoup
from newspaper import Article


def fetch_image(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        image = soup.find('meta', property='og:image')
        if image:
            return image['content']
        return 'Could not provide image'
    except Exception as e:
        print(f"Error fetching image from URL: {url} - {e}")
        return ''


def fetch_description(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        first_paragraph = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', article.text)[0]
        first_sentence = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', first_paragraph)[0]
        return first_sentence.strip()
    except Exception as e:
        print(f"Error extracting article with newspaper3k: {e}")
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            paragraphs = soup.find_all("p")

            if paragraphs:
                for paragraph in paragraphs:
                    first_sentence = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph.get_text())[0]
                    if 'cookies' not in first_sentence and 'ad blocker' not in first_sentence:
                        return ' '.join(filter(None, map(lambda x: x.strip(), first_sentence.splitlines())))
                return "No suitable sentence found"
            else:
                return "Unable to extract the first sentence"
        except Exception as ex:
            print(f"Error extracting article with BeautifulSoup: {ex}")
            return None

def fetch_news(keyword, max_articles=10):
    all_news = []

    feed = feedparser.parse(f'https://news.google.com/rss/search?q={keyword}')

    for idx, entry in enumerate(feed.entries):
        if idx >= max_articles:
            break

        title = entry.get('title', '')
        article_url = entry.get('link', '')
        source_name = title.split('-')[-1].strip() if '-' in title else ''
        title_parts = title.split('-')
        if len(title_parts) > 1:
            title = '-'.join(title_parts[:-1]).strip()

        image_url = fetch_image(article_url)

        summary = fetch_description(article_url)

        news_info = {
            'title': title,
            'description': summary,
            'image_url': image_url,
            'article_url': article_url,
            'source': source_name
        }

        all_news.append(news_info)

    return all_news


keyword_to_search = "biology"
news_list = fetch_news(keyword_to_search, max_articles=10)

for news in news_list:
    print("Title:", news['title'])
    print("Description:", news['description'])
    print("Article URL:", news['article_url'])
    print("Source:", news['source'])
    print("Image URL:", news['image_url'])
    print("\n")
