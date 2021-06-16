from googlesearch import search

google_query = input('¿Qué desea buscar?\n>>> ')
results = input('Número de resultados\n>> ')

for i in search(google_query, num_results = 100, lang = 'es', proxy = None):
    print(i)
