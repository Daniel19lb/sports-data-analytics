import ScraperFC as sfc
import pandas as pd

sofascore = sfc.Sofascore()
Liga = sofascore.get_match_dicts('24/25', 'Champions League')

lista_gol_local_pt = []; lista_gol_visitante_pt = []; lista_gol_total_pt = []
lista_gol_local_partido = []; lista_gol_visitante_partido = []; lista_gol_total_partido = []
lista_club_local= []; lista_club_visitante= []; lista_partidos = []
lista_tiros_local = []; lista_tiros_visitante = []; lista_tiros_total = []
lista_tarjetas_local = []; lista_tarjetas_visitante = []; lista_tarjetas_total = []
lista_corners_local_pt = []; lista_corners_visitante_pt = []; lista_corners_pt = []
lista_corners_local_st = []; lista_corners_visitante_st = []; lista_corners_st = []
lista_corners_local_partido=[]; lista_corners_visitante_partido= []; lista_corners_partido = []
lista_remates_local = []; lista_remates_visitante = []; lista_remates_totales = []

for partido in Liga:
    df_partido = pd.DataFrame(partido)
    if not df_partido.empty:
        id_partido = partido['id']
        estadisticas_goles = sofascore.get_match_dict(id_partido)
        if not partido.get('homeScore') or not partido.get('awayScore'):
            continue
        if 'homeScore' in estadisticas_goles:
            if 'period1' in estadisticas_goles['homeScore']:
                gol_local_pt = estadisticas_goles['homeScore']['period1']
            if 'normaltime' in estadisticas_goles['homeScore']:
                gol_local_partido = estadisticas_goles['homeScore']['normaltime']
  
        if 'awayScore' in estadisticas_goles:
            if 'period1' in estadisticas_goles['awayScore']:
                gol_visitante_pt = estadisticas_goles['awayScore']['period1']
            if 'normaltime' in estadisticas_goles['awayScore']:
                gol_visitante_partido = estadisticas_goles['awayScore']['normaltime']
        gol_total_pt = gol_local_pt + gol_visitante_pt
        gol_total_partido = gol_local_partido + gol_visitante_partido
        estadisticas_generales = sofascore.scrape_team_match_stats(id_partido)
        df = pd.DataFrame(estadisticas_generales)
        #Aplicar esta regla después del dataframe
        if 'name' in df.columns:
            filtro_corners_primera_mitad = df[(df['name'] == 'Corner kicks') & (df['period'] == '1ST')]
            filtro_corners_segunda_mitad = df[(df['name'] == 'Corner kicks') & (df['period'] == '2ND')]
            filtro_corners_totales = df[(df['name'] == 'Corner kicks') & (df['period'] == 'ALL')]
            filtro_tiros_a_puerta = df[(df['name'] == 'Shots on target') & (df['period'] == 'ALL')]
            filtro_remates_totales = df[(df['name'] == 'Total shots') & (df['period'] == 'ALL')]
            filtro_tarjetas = df[(df['name'] == 'Yellow cards') & (df['period'] == 'ALL')]
    
        if filtro_corners_primera_mitad.empty:
            corners_local_pt = 0
            corners_visitante_pt = 0
        else:
            corners_local_pt = filtro_corners_primera_mitad['home'].iloc[0]
            corners_visitante_pt = filtro_corners_primera_mitad['away'].iloc[0]
        corners_pt = int(corners_local_pt) + int(corners_visitante_pt)
    
        if filtro_corners_segunda_mitad.empty:
            corners_local_st = 0
            corners_visitante_st = 0
        else:
            corners_local_st = filtro_corners_segunda_mitad['home'].iloc[0]
            corners_visitante_st = filtro_corners_segunda_mitad['away'].iloc[0]
            corners_st = int(corners_local_st) + int(corners_visitante_st)
    
        if filtro_corners_totales.empty:
            corners_local_partido = 0
            corners_visitante_partido = 0
        else:
            corners_local_partido = filtro_corners_totales['home'].iloc[0]
            corners_visitante_partido = filtro_corners_totales['away'].iloc[0]
            corners_partido = int(corners_local_partido) + int(corners_visitante_partido)

        if filtro_tiros_a_puerta.empty:
            tiros_a_puerta_local= 0
            tiros_a_puerta_visitante = 0
            tiros_a_puerta_total = 0
        else:
            tiros_a_puerta_local = filtro_tiros_a_puerta['home'].iloc[0]
            tiros_a_puerta_visitante = filtro_tiros_a_puerta['away'].iloc[0]
            tiros_a_puerta_total = int(tiros_a_puerta_local) + int(tiros_a_puerta_visitante)
        
        if filtro_remates_totales.empty:
            remates_totales_local = 0
            remates_totales_visitante = 0
            remates_totales = 0
        else:
            remates_local = filtro_remates_totales['home'].iloc[0]
            remates_visitante = filtro_remates_totales['away'].iloc[0]
            remates_totales = int(remates_local) + int(remates_visitante)
            
        if filtro_tarjetas.empty:
            tarjetas_local = 0
            tarjetas_visitante = 0
            tarjetas_total = 0
        else:
            tarjetas_local = filtro_tarjetas['home'].iloc[0]
            tarjetas_visitante = filtro_tarjetas['away'].iloc[0]
            tarjetas_total = int(tarjetas_local) + int(tarjetas_visitante)
    
        Local = partido['homeTeam']['name']
        Visitante = partido['awayTeam']['name']

        lista_gol_local_pt.append(gol_local_pt); lista_gol_visitante_pt.append(gol_visitante_pt); lista_gol_total_pt.append(gol_total_pt)
        lista_gol_local_partido.append(gol_local_partido); lista_gol_visitante_partido.append(gol_visitante_partido); lista_gol_total_partido.append(gol_total_partido)
        lista_club_local.append(Local); lista_club_visitante.append(Visitante)
        lista_corners_local_pt.append(int(corners_local_pt)); lista_corners_visitante_pt.append(int(corners_visitante_pt)); lista_corners_pt.append(corners_pt)
        lista_corners_local_st.append(int(corners_local_st)); lista_corners_visitante_st.append(int(corners_visitante_st)); lista_corners_st.append(corners_st)
        lista_corners_local_partido.append(int(corners_local_partido)); lista_corners_visitante_partido.append(int(corners_visitante_partido)); lista_corners_partido.append(corners_partido)
        lista_tiros_local.append(int(tiros_a_puerta_local)); lista_tiros_visitante.append(int(tiros_a_puerta_visitante)); lista_tiros_total.append(tiros_a_puerta_total)
        lista_remates_local.append(int(remates_local)); lista_remates_visitante.append(int(remates_visitante)); lista_remates_totales.append(remates_totales)
        lista_tarjetas_local.append(int(tarjetas_local)); lista_tarjetas_visitante.append(int(tarjetas_visitante)); lista_tarjetas_total.append(int(tarjetas_total))
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
#Creando Data Frame para llevar las nuevas columnas ordenadas
df_stats_match = pd.DataFrame({
    'Gol 1er Local': lista_gol_local_pt,
    'Gol 1er Visitante': lista_gol_visitante_pt,
    'Gol 1er Total': lista_gol_total_pt,
    'Gol partido Local': lista_gol_local_partido,
    'Gol partido Visitante': lista_gol_visitante_partido,
    'Gol partido Total': lista_gol_total_partido,
    'Corner 1er Local': lista_corners_local_pt,
    'Corner 1er Visitante': lista_corners_visitante_pt,
    'Corner 1er Total': lista_corners_pt,
    'Corner 2nd Local': lista_corners_local_st,
    'Corner 2nd Visitante': lista_corners_visitante_st,
    'Corner 2nd Total': lista_corners_st,
    
    'Club Local': lista_club_local,
    'Club Visitante': lista_club_visitante,
    
    'Corner partido Local': lista_corners_local_partido,
    'Corner partido Visitante': lista_corners_visitante_partido,
    'Corner partido Total': lista_corners_partido,
    'Tarjetas Local': lista_tarjetas_local,
    'Tarjetas Visitante': lista_tarjetas_visitante,
    'Tarjetas Total': lista_tarjetas_total,
    'Tiros a puerta Local': lista_tiros_local,
    'Tiros a puerta Visitante': lista_tiros_visitante,
    'Tiros a puerta Total': lista_tiros_total,
    'Remates Local': lista_remates_local,
    'Remates Visitante': lista_remates_visitante,
    'Remates Totales': lista_remates_totales,
})


#Trasladando el Data Frame a excel
print(df_stats_match)
df_stats_match.to_excel('Champions League.xlsx', index_label='Id Partido', sheet_name='Partidos')
