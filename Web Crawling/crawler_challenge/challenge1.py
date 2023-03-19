import scrapy


class ChallengeSpider(scrapy.Spider):
    name = "challenge"
    allowed_domains = ["laws.bahamas.gov.bs"]
    start_urls = ["http://laws.bahamas.gov.bs/cms/en/legislation/acts.html"]

    """
    -------- Challenge 1 (Must be completed) --------
    Scrape the table for acts starting with the letter 'A' only 
    from the table found on the below page:
    http://laws.bahamas.gov.bs/cms/en/legislation/acts.html
    
    Fill in the appropriate sections with your code to make the spider functional.
    Save your spider output by running it with the following command:
    
    `scrapy crawl challenge -o output.json`
    (Make sure you are in the directory which contains scrapy.cfg when running this)

    NOTE: If you wish to use XPATH queries instead of CSS selectors
    you may modify the code and do so.

    -------- Challenge 2 --------
    Having completed challenge 1, modify the code so that it does the following:
    - asynchronously crawls through all tables (A-Z) only using scrapy.
    - you are free to add any additional functions, methods and imports.
    
    -------- Challenge 3 --------
    Having completed challenge 2, modify the code so that it does the following:
    - when the spider is idle and gets a signal that there is nothing left to scrape, order the items in the 
      same way as they appear in the table before the final yield. 
      (WARNING: this is not the same as ordering by title alphabetically).
    - the above process should occur BEFORE the JSON file is output. (Do not modify or read in the JSON file).
    - you are free to add any additional functions, methods and imports.
 
    Challenges 2 & 3 do not need to be completed.
    If you get stuck or run out of time,
    please write your ideas on how you think they may be solved.
 
     *** Please do not spend more than 2 hours in total for all challenges. ***
    """

    def parse(self, response):
        # 1. Write a CSS selector that finds all of the table rows
        # css_selector = "<ENTER YOUR CSS SELECTOR HERE>"
        xpath_selector = "//table[@class='table table-bordered table-hover table-condensed']/tbody/tr"
        #rows = response.css(css_selector)
        rows = response.xpath(xpath_selector)
        for row in rows:
            # 2. Extract the title of the document link from the row
            #title = row.css("<ENTER YOUR CSS SELECTOR HERE>").get()
            title =  row.xpath(".//td[2]/a/text()").get()
            # 3. Extract the URL (href attribute) of the document link in the row  
            # 4. Ensure that the source_url is complete, i.e starts with "http://laws.bahamas.gov.bs"
            source_url = response.urljoin(row.xpath(".//td[2]/a/@href").get())
            # 5. Extract the date from the row and 
            # # 6. Clean up the date text by stripping any blank spaces that appear before and after it.
            date =row.xpath("normalize-space(.//td[4]/text())").get()
            yield {
                "title": title,
                "source_url": source_url,
                "date": date
            }
        # next_page = response.xpath("//a[@class='nextPage']/@href").get()

        # if next_page:
        #     yield scrapy.Request(url=next_page,callback=self.parse)
