from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]

from utils import (
    cv_download_button,
    inject_css,
    load_projects,
    render_feature_card,
    render_metric_card,
    render_page_header,
    render_section_heading,
)

st.set_page_config(page_title="Livrables & preuves", page_icon="📁", layout="wide")
inject_css()
df = load_projects()

render_page_header(
    "Livrables & preuves",
    "Relier chaque compétence annoncée à une réalisation, un support ou un fichier concret.",
    eyebrow="Projet → méthode → livrable → preuve",
    icon="📁",
    palette="amber",
)

metrics = st.columns(4)
with metrics[0]:
    render_metric_card("Réalisations documentées", "11 + P11", "P1 à P10 · Judilibre · gestion projet")
with metrics[1]:
    render_metric_card("Formats", "10+", "PDF, SQL, PBIX, Excel, notebook, code source…")
with metrics[2]:
    render_metric_card("CV", "Disponible", "Téléchargement direct")
with metrics[3]:
    render_metric_card("Confidentialité", "Contrôlée", "Secrets et données sensibles exclus")

render_section_heading("Typologie des preuves")
columns = st.columns(3)
with columns[0]:
    render_feature_card("📊", "Présentations", "Contexte, méthode, résultats, recommandations et soutenance.")
with columns[1]:
    render_feature_card("💻", "Notebooks & scripts", "Traitements Python, requêtes SQL, contrôles et documentation technique.")
with columns[2]:
    render_feature_card("📈", "Dashboards & applications", "Power BI, Streamlit, captures d’écran et démonstrations métier.")

render_section_heading(
    "Matrice des livrables",
    "Cette matrice offre une vue consolidée des preuves disponibles pour chaque projet. "
    "Les téléchargements détaillés sont accessibles depuis la page Projets OpenClassrooms.",
)

deliverables_summary = {
    "P1": "Cadrage du parcours · auto-évaluation · synthèse visuelle",
    "P2": "Données NBA · rapport Excel · présentation",
    "P3": "Sources CSV · requêtes SQL · documentation technique",
    "P4": "Données anonymisées · rapport RGPD · recommandations",
    "P5": "Base SQLite · script SQL · dossier technique · présentation",
    "P6": "Données sources · notebook · présentation · visuels",
    "P7": "Données · modèle Power BI · tableau de bord · méthodologie",
    "P8": "Données · notebook ML · présentation · visuels",
    "P9": "Base SQLite · audit SQL · rapport · tableau de bord Power BI",
    "P10": "Données · questionnaire · notebook · présentation · Power BI",
    "JUD": "Code source · guide d’installation · captures · démonstration PDF",
}

formats_summary = {
    "P1": "PDF",
    "P2": "XLSX · PPTX · PDF",
    "P3": "CSV · PPTX · PDF · ZIP",
    "P4": "CSV · XLSX · PDF · ZIP",
    "P5": "SQLite · SQL · PPTX · PDF · ZIP",
    "P6": "XLSX · IPYNB · PDF · ZIP",
    "P7": "XLSX · PBIX · PDF · ZIP",
    "P8": "CSV · IPYNB · PPTX · PDF · ZIP",
    "P9": "SQLite · SQL · PBIX · PDF · ZIP",
    "P10": "CSV · XLSX · IPYNB · PPTX · PBIX · PDF · ZIP",
    "JUD": "Python · ZIP · PDF · PNG",
}

view = df[
    [
        "projet_id",
        "categorie",
        "mise_en_avant",
    ]
].copy()

view["Livrables principaux"] = view["projet_id"].map(deliverables_summary)
view["Formats disponibles"] = view["projet_id"].map(formats_summary)

view = view[
    [
        "projet_id",
        "categorie",
        "Livrables principaux",
        "Formats disponibles",
        "mise_en_avant",
    ]
]

view.columns = [
    "Projet",
    "Domaine",
    "Livrables principaux",
    "Formats disponibles",
    "Mise en avant",
]

st.dataframe(
    view,
    width="stretch",
    hide_index=True,
)

st.page_link(
    "pages/3_Projets_OpenClassrooms.py",
    label="Consulter les fiches projets et leurs téléchargements",
    icon="📚",
)


render_section_heading(
    "P11 — Gestion du projet portfolio",
    "Les livrables du P11 sont regroupés dans une page dédiée afin de démontrer la démarche complète : cadrage, planification, mock-ups, dashboards Power BI et documentations.",
)

p11_columns = st.columns(4)
with p11_columns[0]:
    render_feature_card("🔎", "Analyse du besoin", "Comprendre Aéroworld, les parties prenantes, les contraintes et les critères de réussite.")
with p11_columns[1]:
    render_feature_card("📘", "Cahier des charges", "Transformer le besoin en périmètre, exigences, livrables et recette.")
with p11_columns[2]:
    render_feature_card("📅", "Gantt", "Planifier les 70 heures de mission du 20 juin au 20 juillet 2026.")
with p11_columns[3]:
    render_feature_card("🧠", "Carte mentale", "Structurer la vision globale du portfolio et des preuves attendues.")

st.page_link(
    "pages/6_Gestion_du_projet_P11.py",
    label="Accéder à la page Gestion du projet P11",
    icon="🧭",
)

render_section_heading("CV")
cv_download_button()

render_section_heading("Sécurité & confidentialité")
st.markdown(
    """
    - Ne publier aucune donnée personnelle ou confidentielle  
    - Ne jamais publier de clé API, secret OAuth ou identifiant technique  
    - Exclure `.venv/`, `.streamlit/secrets.toml`, `.env` et les fichiers d’identifiants  
    - Anonymiser les captures et ne conserver que les livrables utiles à la démonstration
    """
)
