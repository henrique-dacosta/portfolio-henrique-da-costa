import streamlit as st

from utils import inject_css, render_callout, render_page_header, render_section_heading, render_skill_card

st.set_page_config(page_title="Compétences", page_icon="🧰", layout="wide")
inject_css()

render_page_header(
    "Compétences",
    "Des compétences étayées par des réalisations et des livrables concrets.",
    eyebrow="Expertise métier · Data · Business Intelligence",
    icon="🧰",
    palette="teal",
)

render_callout(
    "Mon approche combine compréhension métier, qualité des données, maîtrise des outils et restitution orientée décision.",
    accent="#0f766e",
)

skills = [
    ("🎯", "Analyse métier & aide à la décision", "Cadrage du besoin, KPI, analyse des risques, recommandations et restitution aux décideurs.", "P10, P5, P7", ["KPI", "Scoring", "SWOT", "PESTEL"]),
    ("🗄️", "SQL & bases relationnelles", "Modélisation, jointures, agrégations, contrôle des clés, grain analytique et documentation.", "P3, P5, P9", ["SQL", "SQLite", "DBeaver", "Jointures"]),
    ("🐍", "Python & analyse exploratoire", "Nettoyage, transformation, jointures contrôlées, visualisations, indicateurs et automatisation.", "P6, P8, P10", ["Python", "Pandas", "EDA", "Data cleaning"]),
    ("📊", "Business Intelligence & Power BI", "Power Query, modèles relationnels, DAX, tableaux de bord, alertes et filtres décisionnels.", "P7, P9", ["Power BI", "Power Query", "DAX", "Dashboard"]),
    ("🛡️", "Qualité, RGPD & gouvernance", "Anonymisation, contrôle qualité, minimisation, traçabilité et maîtrise du risque de ré-identification.", "P4, P6, P9", ["RGPD", "Anonymisation", "Qualité", "Gouvernance"]),
    ("🤖", "Machine learning", "Régression, comparaison de modèles, clustering, métriques et contrôle de la plausibilité métier.", "P8", ["Scikit-learn", "PyCaret", "LightGBM", "K-Means"]),
    ("📈", "Data visualisation & storytelling", "Choix des visuels, hiérarchisation, synthèse et construction d’un récit analytique clair.", "P2, P7, P10", ["Dataviz", "Storytelling", "Excel", "Power BI"]),
    ("🔌", "Applications interactives & API", "Développement Streamlit, appels REST, authentification, filtres, exports et gestion des erreurs.", "Judilibre Explorer", ["Streamlit", "API REST", "Requests", "Exports"]),
    ("⚖️", "Expertise métier", "Finance, audit, fiscalité, contrôle, conformité, pédagogie et accompagnement du changement.", "Compétence transversale", ["Finance", "Audit", "Fiscalité", "Formation"]),
    ("🗂️", "Gestion de projet & documentation", "Cadrage, planification, traçabilité, documentation technique et accompagnement des utilisateurs.", "P1, P4, P6, P7, P9, P10", ["Cadrage", "Planification", "Documentation", "Accompagnement"]),
]

render_section_heading("Familles de compétences")
columns = st.columns(2)
for index, (icon, title, text, proof, badges) in enumerate(skills):
    with columns[index % 2]:
        render_skill_card(icon, title, text, proof, badges)


render_section_heading(
    "Soft skills & posture consultant Data",
    "Des compétences comportementales mobilisées pour transformer un besoin métier en livrable exploitable."
)

soft_skills = [
    (
        "🎧",
        "Écoute & reformulation",
        "Comprendre le besoin métier, clarifier les attentes et traduire une problématique en objectifs d’analyse.",
        "Cadrage P11, cahier des charges, analyse du besoin client",
        ["Besoin métier", "Reformulation", "Cadrage", "Priorisation"],
    ),
    (
        "🛡️",
        "Rigueur & fiabilité",
        "Contrôler les données, expliciter les hypothèses et sécuriser les traitements avant restitution.",
        "Projets SQL, RGPD, Power BI et analyses documentées",
        ["Contrôle", "Traçabilité", "Hypothèses", "Qualité"],
    ),
    (
        "🧩",
        "Esprit de synthèse",
        "Structurer l’information pour produire des messages clairs, hiérarchisés et directement exploitables.",
        "Restitutions projet, tableaux de bord, recommandations",
        ["Synthèse", "Clarté", "Hiérarchisation", "Décision"],
    ),
    (
        "🎓",
        "Pédagogie",
        "Rendre les analyses, tableaux de bord et outils compréhensibles pour des utilisateurs non techniques.",
        "Documentation, vidéo de formation, accompagnement utilisateur",
        ["Transmission", "Vulgarisation", "Formation", "Support"],
    ),
    (
        "🚀",
        "Autonomie & livraison",
        "Conduire un projet de bout en bout : cadrage, conception, développement, documentation et mise en ligne.",
        "Portfolio P11, GitHub, Streamlit Community Cloud",
        ["Autonomie", "Livraison", "Déploiement", "Recettage"],
    ),
    (
        "🤝",
        "Orientation client",
        "Concevoir des livrables utiles, accessibles et adaptés au contexte professionnel du destinataire.",
        "Portfolio public, navigation par preuves, liens et téléchargements",
        ["Utilisateur", "Accessibilité", "Utilité", "Impact"],
    ),
]

soft_columns = st.columns(2)
for index, (icon, title, text, proof, badges) in enumerate(soft_skills):
    with soft_columns[index % 2]:
        render_skill_card(icon, title, text, proof, badges)


render_section_heading("Ma chaîne de valeur")
render_callout(
    "Fiabiliser les données → analyser les signaux → visualiser les résultats → formuler une décision → accompagner les utilisateurs.",
    accent="#0891b2",
)
