import streamlit as st

from utils import (
    cv_download_button,
    inject_css,
    render_callout,
    render_contact_card,
    render_feature_card,
    render_page_header,
    render_section_heading,
)

st.set_page_config(page_title="Contact & objectifs", page_icon="✉️", layout="wide")
inject_css()

render_page_header(
    "Contact & objectifs professionnels",
    "Mettre une double compétence métier et Data / BI au service de la fiabilité, du pilotage et de la transmission.",
    eyebrow="Conseil · Analyse · Business Intelligence · Formation",
    icon="✉️",
    palette="indigo",
)

render_section_heading("Positionnement recherché")
render_callout(
    "Intervenir comme consultant-formateur Data & BI ou Business Intelligence Analyst, "
    "en capitalisant sur plus de 30 ans d’expérience en expertise comptable, audit, "
    "conseil et formation.",
    accent="#4f46e5",
)

render_section_heading("Missions ciblées")
roles = [
    "Consultant Data / BI",
    "Business Intelligence Analyst",
    "Data Analyst — finance & gestion",
    "Consultant reporting & pilotage",
    "Formateur Data / BI",
]
st.markdown(
    " ".join(f'<span class="badge">{role}</span>' for role in roles),
    unsafe_allow_html=True,
)

render_section_heading("Types d’intervention")
intervention_columns = st.columns(4)
with intervention_columns[0]:
    render_feature_card(
        "🧭",
        "Cadrer",
        "Traduire un besoin métier en objectifs, indicateurs et livrables mesurables.",
    )
with intervention_columns[1]:
    render_feature_card(
        "🛡️",
        "Fiabiliser",
        "Contrôler, nettoyer, documenter et sécuriser les données utilisées.",
    )
with intervention_columns[2]:
    render_feature_card(
        "📊",
        "Piloter",
        "Construire des analyses, reportings et tableaux de bord orientés décision.",
    )
with intervention_columns[3]:
    render_feature_card(
        "🎓",
        "Transmettre",
        "Former les utilisateurs et faciliter l’appropriation des méthodes et des outils.",
    )

render_section_heading("Environnements où mon profil crée de la valeur")
environment_columns = st.columns(3)
with environment_columns[0]:
    render_feature_card(
        "💶",
        "Métiers du chiffre",
        "Cabinets d’expertise comptable, audit, directions financières et contrôle de gestion.",
    )
with environment_columns[1]:
    render_feature_card(
        "🏢",
        "PME, ETI & conseil",
        "Organisations souhaitant fiabiliser leurs données et mieux piloter leur activité.",
    )
with environment_columns[2]:
    render_feature_card(
        "🔄",
        "Formation & transformation",
        "Montée en compétence, appropriation des outils et accompagnement au changement.",
    )

render_section_heading("Ma valeur ajoutée")
value_columns = st.columns(3)
with value_columns[0]:
    render_feature_card(
        "🧠",
        "Comprendre le métier",
        "Identifier rapidement les enjeux économiques, réglementaires et opérationnels.",
    )
with value_columns[1]:
    render_feature_card(
        "🔍",
        "Sécuriser l’analyse",
        "Expliciter les hypothèses, contrôler la cohérence et documenter les traitements.",
    )
with value_columns[2]:
    render_feature_card(
        "🗣️",
        "Rendre la décision accessible",
        "Vulgariser les résultats et produire des recommandations directement actionnables.",
    )

render_section_heading("Coordonnées professionnelles")
contact_col1, contact_col2 = st.columns([2, 1])

with contact_col1:
    render_contact_card(
        [
            ("Nom", "Henrique Da Costa"),
            ("Positionnement", "Expert-comptable | Data & Business Intelligence Analyst"),
            ("Localisation", "Clermont-Ferrand, France"),
            ("E-mail", "henrique.dacosta@orange.fr"),
            ("Téléphone", "06 28 33 79 32"),
        ]
    )

with contact_col2:
    st.markdown("#### Document professionnel")
    cv_download_button()

st.caption(
    "Coordonnées publiées pour les échanges professionnels relatifs aux missions "
    "de conseil, d’analyse, de Business Intelligence et de formation."
)

render_section_heading("Message de conclusion")
render_callout(
    "De la donnée brute à la décision : comprendre le métier, fiabiliser l’information "
    "et transmettre des résultats utiles.",
    accent="#0891b2",
)
