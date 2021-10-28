import scrapy
import os


class DetalhesSpider(scrapy.Spider):
    name = 'detalhes'
    allowed_domains = ['fundamentus.com.br/']

    tickers = ['FRTA3',' PSSA3','PTBL3','POSI3','PPLA11','PFRM3','QUAL3','RADL3','RAPT4','RCSL4','RNEW4','RNEW11','RDNI3',
                'RSID3','RAIL3','SBSP3','SAPR3','SAPR4','SAPR11','STBP3','SCAR3','SMTO3','SLED3','SLED4','SHUL4','SEER3',
                'CSNA3','SQIA3','SLCE3','SMLS3','SGPS3','SULA11','SUZB3','TAEE3','TAEE4','TAEE11','TASA3','TASA4','TECN3',
                'TCSA3','TCNO3','TCNO4','TGMA3','TELB3','TELB4','VIVT3','VIVT4','TEND3','TESA3','TIMP3','SHOW3','TOTS3',
                'TRPL3','TRPL4','TRIS3','TPIS3','TUPY3','UGPA3','UCAS3','UNIP3','UNIP6','USIM3','USIM5','VALE3','VLID3',
                'VVAR3','VIVA3','VIVR3','VULC3','WEGE3','WHRL4','WSON33','WIZS3','YDUQ3']
    
    start_urls= ['https://www.fundamentus.com.br/detalhes.php?papel='+str(i) for i in tickers]



    def parse(self, response):

        valores = response.css('span.txt::text').extract()
        setor_subsetor = response.css('span.txt a::text').extract()
        oscilacoes = response.css('font::text').extract()
       
        if len(valores) == 110:

            yield{

                "Papel" : valores[1],
                "Cotação" : valores[3].replace(",","."),
                "Tipo" : valores[5],
                "Data ult cot" : valores[7],
                "Empresa" : valores[9],
                "Min 52 sem" : valores[11].replace(",","."),
                "Setor" : setor_subsetor[0],
                "Max 52 sem" : valores[14].replace(",","."),
                "Subsetor" : setor_subsetor[1],
                "Vol $ méd (2m)" : valores[17].replace(",","."),

                "Valor de mercado" : valores[19].replace(".",""),
                "Últ balanço processado" : valores[21].replace(".",""),
                "Valor da firma" : valores[23].replace(".",""),
                "Nro. Ações" : valores[25].replace(".",""),

                "Dia" : oscilacoes[0].replace(",","."),
                "P/L" : valores[30].replace(",","."),
                "LPA" : valores[32].replace(",","."),
                "Mês" : oscilacoes[1].replace(",","."),
                "P/VP" : valores[35].replace(",","."),
                "VPA" : valores[37].replace(",","."),
                "30 dias" : oscilacoes[2].replace(",","."),
                "P/EBIT" : valores[40].replace(",","."),
                "Marg. Bruta" : valores[42].replace(",","."),
                "12 meses" : oscilacoes[3].replace(",","."),
                "PSR" : valores[45].replace(",","."),
                "Marg. EBIT" : valores[47].replace(",","."),
                "2021" : oscilacoes[4].replace(",","."),
                "P/Ativos" : valores[50].replace(",","."),
                "Marg. Líquida" : valores[52].replace(",","."),
                "2020" : oscilacoes[5].replace(",","."),
                "P/Cap. Giro" : valores[55].replace(",","."),
                "EBIT / Ativo" : valores[57].replace(",","."),
                "2019" : oscilacoes[6].replace(",","."),
                "P/Ativ Circ Liq" : valores[60].replace(",","."),
                "ROIC" : valores[62].replace(",","."),
                "2018" : oscilacoes[7].replace(",","."),
                "Div. Yield" : valores[65].replace(",","."),
                "ROE" : valores[67].replace(",","."),
                "2017" : oscilacoes[8].replace(",","."),
                "EV / EBITDA" : valores[70].replace(",","."),
                "Liquidez Corr" : valores[72].replace(",","."),
                "2016" : oscilacoes[9].replace(",","."),
                "EV / EBIT" : valores[75],
                "Div Br/ Patrim" : valores[77].replace(",","."),
                "2015" : "NaN",
                "Cres. Rec (5a)" : valores[79].replace(",","."),
                "Giro Ativos" : valores[81].replace(",","."),
                
                "Ativo" : valores[84].replace(".",""),
                "Depósitos": "NaN" ,
                "Cart. de Crédito": "NaN" ,
                "Dív. Bruta" : valores[86].replace(".",""),
                "Disponibilidades" : valores[88].replace(".",""),
                "Dív. Líquida" : valores[90].replace(".",""),
                "Ativo Circulante" :valores[92].replace(".",""),
                "Patrim. Líq" : valores[94].replace(".",""),
                                    
                "Receita Líquida_12meses" : valores[99].replace(".",""),
                "Receita Líquida_3meses" : valores[101].replace(".",""),
                "EBIT_12meses" : valores[103].replace(".",""),
                "EBIT_3meses" : valores[104].replace(".",""),
                "Result Int Financ_12meses": "NaN" ,
                "Result Int Financ_3meses": "NaN" ,
                "Rec Serviços_12meses": "NaN" ,
                "Rec Serviços_3meses": "NaN" ,
                "Lucro Líquido_12meses" : valores[107].replace(".",""),
                "Lucro Líquido_3meses" : valores[109].replace(".",""),


                
                }

                   
             
            
        elif len(valores) == 106:

            yield{

                "Papel" : valores[1],
                "Cotação" : valores[3].replace(",","."),
                "Tipo" : valores[5],
                "Data ult cot" : valores[7],
                "Empresa" : valores[9],
                "Min 52 sem" : valores[11].replace(",","."),
                "Setor" : setor_subsetor[0],
                "Max 52 sem" : valores[14].replace(",","."),
                "Subsetor" : setor_subsetor[1],
                "Vol $ méd (2m)" : valores[17].replace(",","."),

                "Valor de mercado" : valores[19].replace(".",""),
                "Últ balanço processado" : valores[21].replace(".",""),
                "Valor da firma" : valores[23].replace(".",""),
                "Nro. Ações" : valores[25].replace(".",""),

                "Dia" : oscilacoes[0].replace(",","."),
                "P/L" : valores[30].replace(",","."),
                "LPA" : valores[32].replace(",","."),
                "Mês" : oscilacoes[1].replace(",","."),
                "P/VP" : valores[35].replace(",","."),
                "VPA" : valores[37].replace(",","."),
                "30 dias" : oscilacoes[2].replace(",","."),
                "P/EBIT" : valores[40].replace(",","."),
                "Marg. Bruta" : valores[42].replace(",","."),
                "12 meses" : oscilacoes[3].replace(",","."),
                "PSR" : valores[45].replace(",","."),
                "Marg. EBIT" : valores[47].replace(",","."),
                "2021" : oscilacoes[4].replace(",","."),
                "P/Ativos" : valores[50].replace(",","."),
                "Marg. Líquida" : valores[52].replace(",","."),
                "2020" : oscilacoes[5].replace(",","."),
                "P/Cap. Giro" : valores[55].replace(",","."),
                "EBIT / Ativo" : valores[57].replace(",","."),
                "2019" : oscilacoes[6].replace(",","."),
                "P/Ativ Circ Liq" : valores[60].replace(",","."),
                "ROIC" : valores[62].replace(",","."),
                "2018" : oscilacoes[7].replace(",","."),
                "Div. Yield" : valores[65].replace(",","."),
                "ROE" : valores[67].replace(",","."),
                "2017" : oscilacoes[8].replace(",","."),
                "EV / EBITDA" : valores[70].replace(",","."),
                "Liquidez Corr" : valores[72].replace(",","."),
                "2016" : oscilacoes[9].replace(",","."),
                "EV / EBIT" : valores[75],
                "Div Br/ Patrim" : valores[77].replace(",","."),
                "2015" : "NaN",
                "Cres. Rec (5a)" : valores[79].replace(",","."),
                "Giro Ativos" : valores[81].replace(",","."),
                
                "Ativo" : valores[84].replace(".",""),
                "Depósitos": valores[86].replace(".",""), 
                "Cart. de Crédito": valores[88].replace(".","") ,
                "Dív. Bruta" : "NaN",
                "Disponibilidades" : "NaN",
                "Dív. Líquida" : "NaN",
                "Ativo Circulante" : "NaN",
                "Patrim. Líq" : valores[90].replace(".",""),
                                    
                "Receita Líquida_12meses" : "NaN" ,
                "Receita Líquida_3meses" : "NaN" ,
                "EBIT_12meses" : "NaN" ,
                "EBIT_3meses" : "NaN" ,
                "Result Int Financ_12meses": valores[95].replace(".","") ,
                "Result Int Financ_3meses": valores[97].replace(".","") ,
                "Rec Serviços_12meses": valores[99].replace(".","") ,
                "Rec Serviços_3meses": valores[101] ,
                "Lucro Líquido_12meses" : valores[103].replace(".",""),
                "Lucro Líquido_3meses" : valores[105].replace(".",""),  

                }

