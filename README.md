# Fundamentus com framework scrapy

Crawler do site Fundamentus.com com o uso do framework scrapy, tanto da aba detalhada como a de resumo.

***Baixa informacões que os outros scrapys do fundamentus não realizam.***

Para iniciar, dentro da pasta fundamentus digite: scrapy crawl detalhes -O nomedoarquivocriado.csv  ou scrapy crawl resultado -O nomedoarquivocriado.csv

Não é um codigo elegante, mas funcional, realiza o scrapy de forma rapida.

As informacões baixadas são:

           columns = ['Papel', 'Cotação', 'Tipo', 'Data ult cot', 'Empresa', 'Min 52 sem',
                      'Setor', 'Max 52 sem', 'Subsetor', 'Vol $ méd (2m)', 'Valor de mercado',
                      'Últ balanço processado', 'Valor da firma', 'Nro. Ações',

                      'Dia', 'P/L',
                      'LPA', 'Mês', 'P/VP', 'VPA', '30 dias', 'P/EBIT', 'Marg. Bruta',
                      '12 meses', 'PSR', 'Marg. EBIT', '2021', 'P/Ativos', 'Marg. Líquida',
                      '2020', 'P/Cap. Giro', 'EBIT / Ativo', '2019', 'P/Ativ Circ Liq',
                      'ROIC', '2018', 'Div. Yield', 'ROE', '2017', 'EV / EBITDA',
                      'Liquidez Corr', '2016', 'EV / EBIT', 'Div Br/ Patrim', '2015',
                      'Cres. Rec (5a)', 'Giro Ativos',

                      'Ativo',
                      'Dív. Bruta',
                      'Disponibilidades',
                      'Dív. Líquida',
                      'Ativo Circulante',               
                      'Depósitos',
                      'Cart. de Crédito',
                      'Patrim. Líq',

                      'Receita Líquida_12meses',         
                      'Receita Líquida_3meses', 'EBIT_12meses', 'EBIT_3meses',
                      'Lucro Líquido_12meses', 'Lucro Líquido_3meses']
                      
                      e mais algumas informações...
           
 Realizei este projeto com o fim de aprendizado e por não encontrar no github nenhum scrapy que pegue todas as informaçoes que eu precisava como setores e subsetores para
 realizar modelos KNN e KMC de machine learning. 
