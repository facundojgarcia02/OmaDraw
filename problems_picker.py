import cloudscraper
from scrap import get_problems
import pandas as pd

#Scraper.
Scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 

urls = [{"url": "https://www.omaforos.com.ar/archivo.php?id=690", "certamen": "Intercolegial", "ano": 2022},
		{"url": "https://www.omaforos.com.ar/archivo.php?id=628", "certamen": "Intercolegial", "ano": 2021},
		]

i = 0

problems = [{
				"certamen":urls[i]["certamen"], 
				"ano": urls[i]["ano"], 
				"problems": get_problems(Scraper, urls[i]["url"]+str(level))
			} for level in [1,2,3]]

problem_dict = [{
				"Certamen": p["certamen"], 
				"Año": p["ano"],
				"Nivel": i+1,
				"Numero de problema": p["problems"][j][1],
				"Texto": p["problems"][j][2:]
			} for i, p in enumerate(problems) for j in range(3)]

df = pd.DataFrame(problem_dict)
df.to_csv("test.csv",index = False)