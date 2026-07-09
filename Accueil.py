import streamlit as st

from utils import (
    cv_download_button,
    inject_css,
    load_projects,
    render_callout,
    render_feature_card,
    render_metric_card,
    render_page_header,
    render_project_card,
    render_section_heading,
)

st.set_page_config(
    page_title="Portfolio Data / BI — Henrique Da Costa",
    page_icon="📊",
    layout="wide",
)
inject_css()
projects = load_projects()

render_page_header(
    "Henrique Da Costa",
    "Expert-comptable | Data & Business Intelligence Analyst — un profil métier senior renforcé par la data.",
    eyebrow="Data Scientist RNCP niveau 7 · Parcours Business Intelligence Analyst 2025–2026",
    icon="📊",
    palette="blue",
)

st.markdown("### Fiabiliser les données, structurer l’analyse, éclairer la décision.")
st.write(
    "Expert-comptable de formation, diplômé Data Scientist RNCP niveau 7 et engagé dans un parcours "
    "Business Intelligence Analyst, je mobilise SQL, Python, Power BI, Streamlit et les outils de "
    "Business Intelligence pour transformer des données hétérogènes en analyses fiables, visuelles "
    "et exploitables."
)

metric_columns = st.columns(3)
with metric_columns[0]:
    render_metric_card("Expérience métier", "30 ans", "Expertise comptable, audit, conseil")
with metric_columns[1]:
    render_metric_card("Réalisations & preuves", "11 + P11", "10 projets OC + Judilibre + gestion projet")
with metric_columns[2]:
    render_metric_card("Positionnement", "Data / BI", "Double compétence métier & data")

st.write("")
value_columns = st.columns(3)
with value_columns[0]:
    render_feature_card(
        "🧭",
        "Culture métier & fiabilité",
        "Comprendre les enjeux économiques, financiers, réglementaires et organisationnels avant de produire les indicateurs.",
    )
with value_columns[1]:
    render_feature_card(
        "📈",
        "Compétences Data / BI",
        "Préparer, contrôler, analyser et visualiser les données avec SQL, Python, Power Query, Power BI et Streamlit.",
    )
with value_columns[2]:
    render_feature_card(
        "🎯",
        "Restitution décisionnelle",
        "Transformer une analyse en recommandation claire, argumentée et actionnable pour les métiers.",
    )

render_section_heading(
    "Projets phares",
    "Une sélection illustrant la chaîne complète : stratégie, préparation des données, BI, machine learning et application métier.",
)
featured_ids = ["P10", "P6", "P7", "P8", "P9", "JUD"]
featured = projects[projects["projet_id"].isin(featured_ids)].copy()
featured["order"] = featured["projet_id"].apply(
    lambda project_id: featured_ids.index(project_id) if project_id in featured_ids else 999
)
featured = featured.sort_values("order")

columns = st.columns(2)
for index, row in enumerate(featured.to_dict("records")):
    with columns[index % 2]:
        render_project_card(row)

render_section_heading("Ce que ce portfolio démontre")
render_callout(
    "Une chaîne complète de compétences : analyser un besoin métier, formaliser un cahier des charges, "
    "planifier un projet, fiabiliser les données, structurer les traitements, produire des analyses, "
    "construire des tableaux de bord, recommander et livrer des outils exploitables."
)
cv_download_button()

st.page_link(
    "pages/6_Gestion_du_projet_P11.py",
    label="Voir la démarche de gestion du projet P11",
    icon="🧭",
)
