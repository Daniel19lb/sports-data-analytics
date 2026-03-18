# 🏆 Sports Data Analytics

Sistema de análisis estadístico deportivo desarrollado con Python y Power BI, 
orientado a identificar patrones de rendimiento en partidos de fútbol y básquet 
para la toma de decisiones basada en datos.

## 📌 Descripción

Este proyecto extrae, procesa y visualiza estadísticas de partidos de 10 ligas 
deportivas internacionales usando web scraping automatizado. Cada liga cuenta con 
su propio dashboard interactivo en Power BI con métricas diferenciadas por 
primer tiempo y tiempo completo.

## ⚽ Ligas Analizadas

| Liga | País |
|---|---|
| Premier League | Inglaterra |
| La Liga | España |
| BundesLiga | Alemania |
| Serie A | Italia |
| Ligue 1 | Francia |
| Champions League | Mundial |
| Liga Portugal | Portugal |
| Super League | Grecia |
| NBA | EEUU |
| A League | Australia |

## 📊 Métricas por Dashboard

- Goles (Local, Visitante, Total)
- Corners (Primer tiempo y tiempo completo)
- Tarjetas amarillas y rojas
- Tiros a puerta
- Filtros interactivos por equipo Local/Visitante
- Para ligas de básquet (Q1, primer tiempo)

## 🛠️ Stack Tecnológico

- **Python** → Extracción y procesamiento de datos
- **ScraperFC** → Web scraping desde SofaScore
- **Pandas** → Limpieza y transformación de datos
- **Excel/CSV** → Almacenamiento de datos por liga
- **Power BI** → Dashboards interactivos publicados en Power BI Fabric

## 📁 Estructura del Proyecto
```
sports-data-analytics/
│
├── scripts/
│   ├── leagues/          → Scripts individuales por liga
│   └── run_pipeline_Leagues_Football.py  → Orquestador principal
│
├── data/                 → Datasets procesados por liga (Excel/CSV)
│
└── dashboards/           → Dashboards Power BI (.pbix) por liga
```

## ⚙️ ¿Cómo funciona?

1. El orquestador `run_pipeline_Leagues_Football.py` ejecuta todos los scripts
2. Cada script extrae estadísticas de la temporada actual y anterior desde SofaScore
3. Los datos se almacenan en Excel/CSV en la carpeta `data/`
4. Los dashboards de Power BI se actualizan con los nuevos datos

## ⚠️ Nota

SofaScore implementa medidas de seguridad que pueden bloquear el scraper 
después de varias ejecuciones consecutivas. Se recomienda espaciar las 
ejecuciones para evitar bloqueos temporales.

## 👤 Autor

**Herles Daniel Lopez Bancho**  
Data Analyst BI | Estudiante Ing. de Sistemas  
[LinkedIn](https://linkedin.com/in/daniel-lopez-572680194)
