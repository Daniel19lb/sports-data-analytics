import ScraperFC as sfc
import pandas as pd

sofascore = sfc.Sofascore()
Liga = sofascore.get_match_dicts('24/25', 'Italy Serie A')


for partido in Liga[:5]:
    print(partido)


