import scrapy
import json
import csv

class QuotesSpider(scrapy.Spider):
    name="quotes"
    def start_requests(self):
        urls=["https://www.imdb.com/calendar/?ref_=nv_mv_cal"]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)
    def parse(self,response):
    #     import pdb;pdb.set_trace()
        # Name=response.css('a::text').extract()
        Name=response.xpath('//*[@id="main"]/ul/li/a/text()').extract()
        # Name=response.xpath('c').extract()
        # Name=response.xpath('//a/text()').getall()
        # data={information:Name}
        # with open ('StateData.json','w')as f:
        #     json.dump(data,f,indent=4)
        states=['information']

        with open('statedata.csv','w') as f:
            for state in Name:

                f.write(state)
                f.write("\n")



