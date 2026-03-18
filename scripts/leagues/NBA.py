import ScraperFC as sfc
import pandas as pd

sofascore = sfc.Sofascore()
NBA_oficial = sofascore.get_match_dicts('23/24', 'NBA')
NBA_oficial2 = sofascore.get_match_dicts('24/25', 'NBA')

lista_local = []
lista_puntos_local_pp = [];  lista_puntos_visitante_pp = []
lista_puntos_pp = []; lista_puntos_pt = []; lista_visitante = []
lista_local_pts_pt = []; lista_visitante_pts_pt = []

for Partido in NBA_oficial:
    df_nba_ofi = pd.DataFrame(Partido)
    if not df_nba_ofi.empty:
        id_partido = Partido['id']
        link = sofascore.get_match_url_from_id(id_partido)
        estadisticas = sofascore.get_match_dict(id_partido)
        puntos_local_pp = estadisticas['homeScore']['period1']
        puntos_visitante_pp = estadisticas['awayScore']['period1']
        puntos_pp = puntos_local_pp + puntos_visitante_pp
        puntos_local_sp = estadisticas['homeScore']['period2']
        puntos_visitante_sp = estadisticas['awayScore']['period2']
        puntos_sp = puntos_local_sp + puntos_visitante_sp
        
        local_pts_pt = puntos_local_pp + puntos_local_sp
        visitante_pts_pt = puntos_visitante_pp + puntos_visitante_sp
        puntos_pt = puntos_pp + puntos_sp
        
        Local = Partido['homeTeam']['name']
        Visitante = Partido['awayTeam']['name']
        
        lista_puntos_local_pp.append(int(puntos_local_pp)); lista_puntos_visitante_pp.append(int(puntos_visitante_pp))
        lista_puntos_pp.append(int(puntos_pp)); lista_puntos_pt.append(int(puntos_pt))
        lista_local.append(Local); lista_visitante.append(Visitante)
        lista_local_pts_pt.append(int(local_pts_pt)); lista_visitante_pts_pt.append(int(visitante_pts_pt))
        
for Partido2 in NBA_oficial2:
    df_nba_ofi2 = pd.DataFrame(Partido2)
    if not df_nba_ofi2.empty:
        id_partido = Partido2['id']
        link = sofascore.get_match_url_from_id(id_partido)
        estadisticas = sofascore.get_match_dict(id_partido)
        puntos_local_pp = estadisticas['homeScore']['period1']
        puntos_visitante_pp = estadisticas['awayScore']['period1']
        puntos_pp = puntos_local_pp + puntos_visitante_pp
        puntos_local_sp = estadisticas['homeScore']['period2']
        puntos_visitante_sp = estadisticas['awayScore']['period2']
        puntos_sp = puntos_local_sp + puntos_visitante_sp
        
        local_pts_pt = puntos_local_pp + puntos_local_sp
        visitante_pts_pt = puntos_visitante_pp + puntos_visitante_sp
        puntos_pt = puntos_pp + puntos_sp
        
        Local = Partido2['homeTeam']['name']
        Visitante = Partido2['awayTeam']['name']
        
        lista_puntos_local_pp.append(int(puntos_local_pp)); lista_puntos_visitante_pp.append(int(puntos_visitante_pp))
        lista_puntos_pp.append(int(puntos_pp)); lista_puntos_pt.append(int(puntos_pt))
        lista_local.append(Local); lista_visitante.append(Visitante)
        lista_local_pts_pt.append(int(local_pts_pt)); lista_visitante_pts_pt.append(int(visitante_pts_pt))
        
df_game_nba = pd.DataFrame({
    'Local': lista_local,
    'Visitante': lista_visitante,
    'Local Primer Periodo': lista_puntos_local_pp,
    'Visitante Primer Periodo': lista_puntos_visitante_pp,
    'Primer Periodo': lista_puntos_pp,
    'Local Primer Tiempo': lista_local_pts_pt,
    'Visitante Primer Tiempo': lista_visitante_pts_pt,
    'Primer Tiempo': lista_puntos_pt,
})

print(df_game_nba)
df_game_nba.to_excel('NBA.xlsx', index_label='Id Partido', sheet_name='Partidos NBA')
