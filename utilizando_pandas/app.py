import pandas as pd
tabelas = pd.read_html("https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria")
tabela = tabelas[0]
tabela_filtrada = tabela[["Diretor(a)", "Bilheteria (US$)"]]
tabela_filtrada["Bilheteria (US$)"] = tabela_filtrada["Bilheteria (US$)"].str.replace(" ", "").astype("int64")
print(tabela_filtrada)