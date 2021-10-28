import scrapy


class ResultadoSpider(scrapy.Spider):
    name = 'resultado'
    allowed_domains = ['fundamentus.com.br/resultado.php']
    start_urls = ['http://fundamentus.com.br/resultado.php/']


    def parse(self, response):

        valores = response.xpath('//*[@id="resultado"]/tbody/tr/td/text()').getall()
        nomes = response.css('tbody tr td a::text').extract()

        for j in range(len(valores)):
           valores[j] =  valores[j].replace(",",".").replace("%","").replace(".","")

        listasDivididas = [valores[i:i+20] for i in range(0,len(valores),20)] #gerar lista dividida
        
        for i in range(len(listasDivididas)):
    

            
            try:
                yield{
                    
                    'Papel': nomes[i],
                    'Cotação': float(listasDivididas[i][0])/100, 
                    'P/L': float(listasDivididas[i][1])/100,
                    'P/VP': float(listasDivididas[i][2])/100,
                    'PSR': float(listasDivididas[i][3])/1000,
                    'Div.Yield%': float(listasDivididas[i][4])/100, 
                    'P/Ativo': float(listasDivididas[i][5])/1000,
                    'P/Cap.Giro' : float(listasDivididas[i][6])/100,
                    'P/EBIT': float(listasDivididas[i][7])/100, 
                    'P/Ativ Circ.Liq': float(listasDivididas[i][8])/100, 
                    'EV/EBIT': float(listasDivididas[i][9])/100, 
                    'EV/EBITDA%': float(listasDivididas[i][10])/100, 
                    'Mrg Ebit%': float(listasDivididas[i][11])/100, 
                    'Mrg. Líq.': float(listasDivididas[i][12])/100, 
                    'Liq. Corr.': float(listasDivididas[i][13])/100, 
                    'ROIC%': float(listasDivididas[i][14])/100, 
                    'ROE%': float(listasDivididas[i][15])/100, 
                    'Liq.2meses': float(listasDivididas[i][16])/100, 
                    'Patrim. Líq': float(listasDivididas[i][17])/100, 
                    'Dív.Brut/ Patrim.': float(listasDivididas[i][18])/100, 
                    'Cresc. Rec.5a%': float(listasDivididas[i][19])/100,
                }
            except:

               pass
            
