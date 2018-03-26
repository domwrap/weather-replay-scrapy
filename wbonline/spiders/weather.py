# -*- coding: utf-8 -*-
import scrapy


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['online.whistlerblackcomb.com/weather']
    # start_urls = ['http://online.whistlerblackcomb.com/weather/']

    def start_requests(self):
        return [scrapy.FormRequest( "http://online.whistlerblackcomb.com/weather/default.aspx"
            ,formdata={
                'ddlBC':    '-1'
                , 'ddlWH':  '210'
                , '__EVENTVALIDATION': '/wEWEgKZzPSCDgLxwOHCAgLyr4evDgLY7uz4CQLY7uj4CQLY7uT4CQLY7pz7CQLZ7uT4CQLowL2tAgLrr9vADgKr15biBwKEjYGIBgKi5f2UCgKRqdvUCwL8k7miBgKSqdvUCwLB7siUCQLA7rSXCQ+HdH8zGpxF+ouN3/VbAfE4j0xz'
                , '__VIEWSTATEGENERATOR': '232CF4DB'
                , '__VIEWSTATE': '/wEPDwUJNDI4MjUwMDMzD2QWAgIDD2QWBgIBDxBkZBYBZmQCAw8QZGQWAWZkAgUPZBYCAgcPPCsADQBkGAEFBmd2TGlzdA9nZNBS115qwy1nqFiQb/AmAV2bLLGv'
            }
            # , headers={
                # 'Content-Type': 'application/x-www-form-urlencoded'
            # }
            , callback=self.parse
            )]

    def parse(self, response):
        self.log("\n")

        for row in response.css('tr[class*=GridRow]'):
            data = row.css("td::text").extract()
            # psum = row.css('td.span::text')
            # self.log( psum );
            export = {
                'date':         data[0]
                , 'temp':       data[1]
                , 'wind_avg':   data[2]
                , 'wind_max':   data[3]
                , 'wind_dir':   data[4]
                , 'humidity':   data[5]
                , 'pressure':   data[6]
                , 'snow_bse':   data[7]
                , 'snow_new':   data[8].replace('\n', '').replace('\r', '').replace('  ', '')
                , 'precip':     data[9].replace('\n', '').replace('\r', '').replace('  ', '')
            }
            self.log( export )

        self.log("\n")
