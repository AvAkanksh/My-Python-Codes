import scrapy
from scrapy import FormRequest
from scrapy.utils.response import open_in_browser
import csv
import time

class HallTickets(scrapy.Spider):
    name = 'halltickets'
    start_urls = ['https://bse.telangana.gov.in/SSCHTMARCH23/RegDefault.aspx']
    def parse(self,response):
        # print(response.css('#drpDistrict option').xpath("@value").extract())
        for district in response.css('#drpDistrict option').xpath('@value').extract():
            if(district=='21'):
                data = {'drpDistrict':district}
                yield FormRequest.from_response(response,formdata=data,callback=self.step2)
        
    def step2(self,response):
        # print(response.css('#drpSchools option').xpath("@value").extract())
        for school in response.css('#drpSchools option').xpath('@value').extract():
            if(school == '31014'):
                data = {'drpSchools':school}
                yield FormRequest.from_response(response,formdata=data,callback=self.step3)
    
    def step3(self,response):
        district = response.css("#drpDistrict [selected='selected']::text").extract_first()
        school = response.css("#drpSchools [selected='selected']::text").extract_first()
        names = response.css("#drpName option::text").extract()
        hallTicketNumbers = response.css("#drpName option").xpath("@value").extract()
        # print(district,"\t",school)
        # with open('output.csv', 'a') as f:
        #     for key,value in zip(hallTicketNumbers,names):
        #         writer = csv.writer(f)
        #         writer.writerow([key,value,school,district])
        for name  in hallTicketNumbers :
            data = {'drpName':name,
                'dd':'01',
                'mm':'01',
                'yy':'1970',
                # 'btnDownload':'Download HallTicket'
                }
            yield FormRequest.from_response(response,formdata=data,callback=self.step4)
    def step4(self,reponse):
        photoSrc = reponse.css("#imgPhoto").xpath("@src").extract_first()
        signSrc = reponse.css("#imgSignature").xpath("@src").extract_first()
        print(photoSrc)
        print(signSrc)
        # time.sleep(2)