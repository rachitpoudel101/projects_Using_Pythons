import hashlib

class UrlShortener:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "http://short.url/"

    def shorten_url(self, original_url):
        hash_value = hashlib.md5(original_url.encode()).hexdigest()[:6]
        short_url = self.base_url + hash_value
        self.url_mapping[short_url] = original_url
        return short_url

    def expand_url(self, short_url):
        original_url = self.url_mapping.get(short_url)
        return original_url

#Example
url_shortener = UrlShortener()

original_url = input("enter url here: ")
short_url = url_shortener.shorten_url(original_url)

print(f"Original URL: {original_url}")
print(f"Short URL: {short_url}")

expanded_url = url_shortener.expand_url(short_url)
print(f"Expanded URL: {expanded_url}")