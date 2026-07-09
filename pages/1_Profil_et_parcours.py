import streamlit as st

from utils import (
    cv_download_button,
    inject_css,
    render_callout,
    render_feature_card,
    render_metric_card,
    render_page_header,
    render_section_heading,
    render_timeline_card,
)

st.set_page_config(page_title="Profil & parcours", page_icon="👤", layout="wide")
inject_css()

render_page_header(
    "Profil & parcours",
    "Une trajectoire construite à la croisée de l’expertise comptable, de la transmission et de la Data / BI.",
    eyebrow="Un profil métier senior, renforcé par la data",
    icon="👤",
    palette="indigo",
)

metrics = st.columns(4)
with metrics[0]:
    render_metric_card("Expertise métier", "30 ans", "Expertise comptable, audit, fiscalité")
with metrics[1]:
    render_metric_card("Expérience en formation", "20+ ans", "Transmission et vulgarisation")
with metrics[2]:
    render_metric_card("Diplôme data", "RNCP niveau 7", "Data Scientist — 2021")
with metrics[3]:
    render_metric_card("Parcours actuel", "Data / BI", "Business Intelligence Analyst")

render_section_heading(
    "Mon fil conducteur",
    "Le même réflexe traverse mon parcours : comprendre, contrôler, expliquer et rendre utile.",
)
render_callout(
    "Comprendre le besoin métier → fiabiliser les données → structurer l’analyse → restituer clairement → éclairer la décision.",
    accent="#4f46e5",
)

render_section_heading("Parcours professionnel")
left, right = st.columns(2)
with left:
    render_timeline_card(
        "Fév. 2023 — fév. 2025",
        "Expert-comptable — AGC Lozère",
        "Responsabilités d’expertise comptable, analyse, conseil et contrôle dans un environnement multi-agences.",
        "#2563eb",
    )
    render_timeline_card(
        "2017 — 2022",
        "Direction de cabinets & conseil-formation",
        "Direction de structures, management, organisation et missions de consultant-formateur indépendant.",
        "#4f46e5",
    )
    render_timeline_card(
        "2002 — 2016",
        "Expert-comptable indépendant & formateur",
        "Accompagnement de TPE, missions comptables et fiscales, formation professionnelle et conseil.",
        "#0f766e",
    )
with right:
    render_timeline_card(
        "1994 — 2002",
        "Expert-comptable & commissaire aux comptes",
        "Audit, expertise comptable et direction d’un cabinet d’une dizaine de collaborateurs.",
        "#b45309",
    )
    render_timeline_card(
        "1985 — 1994",
        "Premières expériences professionnelles",
        "Parcours opérationnel comprenant quatre années comme contremaître d’une équipe de dix ouvriers.",
        "#64748b",
    )

render_section_heading("Formations structurantes")
formation_columns = st.columns(2)
with formation_columns[0]:
    render_timeline_card("2025 — 2026", "Business Intelligence Analyst — OpenClassrooms", "Parcours orienté SQL, Python, Power BI, tableaux de bord, gouvernance et recommandation business.", "#2563eb")
    render_timeline_card("2021", "Data Scientist — OpenClassrooms / CentraleSupélec", "Diplôme RNCP niveau 7 : statistiques, machine learning, Python, modélisation et approche projet.", "#4f46e5")
with formation_columns[1]:
    render_timeline_card("Depuis 2021", "Perfectionnement Data Science & Business Intelligence", "Approfondissement continu de Python, SQL, Power BI, machine learning, Streamlit et outils de pilotage décisionnel.", "#0891b2")
    render_timeline_card("2006", "Master Droit des affaires et fiscalité", "Faculté de droit de Clermont-Ferrand — validation des acquis de l’expérience.", "#0f766e")
    render_timeline_card("1999 / 2004", "DEA Sciences de gestion & Diplôme d’expertise comptable", "Socle supérieur en gestion, audit, comptabilité, fiscalité et conseil.", "#b45309")

render_section_heading("Ce qui me différencie")
value_columns = st.columns(3)
with value_columns[0]:
    render_feature_card("🏛️", "Culture métier", "Finance, gestion, fiscalité, audit, contrôle, conformité et compréhension des enjeux dirigeants.")
with value_columns[1]:
    render_feature_card("🔎", "Exigence de fiabilité", "Contrôles de cohérence, traçabilité, documentation des traitements et prudence d’interprétation.")
with value_columns[2]:
    render_feature_card("🎓", "Restitution pédagogique", "Capacité à vulgariser des analyses complexes et à accompagner des publics non techniques.")

render_section_heading("Domaines d’intervention privilégiés")
render_callout(
    "Finance et contrôle de gestion · expertise comptable et audit · reporting de gestion · pilotage de la performance · "
    "conformité et qualité des données · tableaux de bord dirigeants · automatisation d’analyses métier."
)
cv_download_button()
