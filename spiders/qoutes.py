from pathlib import Path
import scrapy
import requests


class QoutesSpider(scrapy.Spider):
    name = "qoutes"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }
            # page = response.url.split("/")[-2]
            # filename = f"quotes-{page}.html"
            # Path(filename).write_bytes(response.body)
            # self.log(f"Saved file {filename}")

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    # async def start(self):
    #     urls = [
    #         "https://quotes.toscrape.com/page/1/",
    #         "https://quotes.toscrape.com/page/2/",
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # async def check_http_status(url):
    #     try:
    #         response = requests.get(url, timeout=3)  # Set a timeout for the request
    #         return response.status_code

    #     except requests.exceptions.RequestException as e:
    #         print(f"Error checking {url}: {e}")
    #         return None

    # # async def start(self):
    # #     page = 1
    # #     while True:
    # #         urls = self.url+"/page/"+str(page)+"/"
    # #         yield scrapy.Request(url=urls, callback=self.parse)
    # #         page = page + 1
    
    # #     print("SCRAPPINGNYA EYOY")
    # #   if  response.css("div.qoutes::text").get() == NULL :

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f"quotes-{page}.html"
    #     Path(filename).write_bytes(response.body)
    #     self.log(f"Saved file {filename}")
    
    
    # while True :
    #     check_url = url+str(page)
    #     print(f"Checking {check_url} status", end="")
    #     if check_http_status(check_url) == 200 :
    #         print(" OK")
    #         checked_url.append(check_url)
    #         page = page + 1
    #     else :
    #         start_urls = checked_url

