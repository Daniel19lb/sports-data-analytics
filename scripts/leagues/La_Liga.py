import requests
import ScraperFC as sfc

def check_sofascore_api_ok():
    url = "https://api.sofascore.com/api/v1/unique-tournament/8/seasons/"
    r = requests.get(url, timeout=20)
    if r.status_code == 403:
        raise SystemExit(
            f"Sofascore API bloqueó (403 Forbidden). Respuesta: {r.text[:120]}"
        )
    r.raise_for_status()

check_sofascore_api_ok()

sofascore = sfc.Sofascore()
Liga = sofascore.get_match_dicts('24/25', 'Spain La Liga')
