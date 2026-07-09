from pathlib import Path

import streamlit as st

from utils import (
    inject_css,
    load_projects,
    render_badges,
    render_callout,
    render_feature_card,
    render_metric_card,
    render_page_header,
    render_section_heading,
    split_badges,
)

ROOT = Path(__file__).resolve().parents[1]
JUD_ASSET_DIR = ROOT / "assets" / "projets" / "JUD"

st.set_page_config(page_title="Judilibre Explorer", page_icon="⚖️", layout="wide")
inject_css()

df = load_projects()
row = df[df["projet_id"] == "JUD"].iloc[0]

render_page_header(
    "Judilibre Explorer",
    "Rechercher, qualifier, consulter et exporter des décisions de jurisprudence depuis une interface métier.",
    eyebrow="Projet personnel signature · Python · Streamlit · API REST",
    icon="⚖️",
    palette="slate",
)

render_badges(split_badges(row["competences"]), limit=10)
st.write("")

metrics = st.columns(4)
with metrics[0]:
    render_metric_card("Modes de recherche", "3", "OR · AND · EXACT")
with metrics[1]:
    render_metric_card("Filtres métier", "4+", "Juridiction, chambre, dates, volume")
with metrics[2]:
    render_metric_card("Formats d’export", "5", "CSV, Excel, Word, PDF, ZIP")
with metrics[3]:
    render_metric_card("Secrets embarqués", "0", "Configuration via Streamlit secrets")

render_section_heading("Valeur métier")
render_callout(
    "Réduire le temps consacré à la recherche documentaire, structurer les métadonnées "
    "des décisions et produire des exports immédiatement exploitables pour l’analyse.",
    accent="#0f172a",
)

feature_columns = st.columns(3)
with feature_columns[0]:
    render_feature_card(
        "🔎",
        "Recherche plein texte",
        "Requêtes par mots-clés avec opérateurs OR, AND ou expression exacte.",
    )
with feature_columns[1]:
    render_feature_card(
        "🧭",
        "Qualification des résultats",
        "Filtres par juridiction, chambre, période, volume et score de pertinence.",
    )
with feature_columns[2]:
    render_feature_card(
        "📦",
        "Production documentaire",
        "Résultats et décisions exportables dans cinq formats opérationnels.",
    )

render_section_heading("Parcours utilisateur")
journey_columns = st.columns(5)
journey_steps = [
    ("1", "Formuler la requête"),
    ("2", "Appliquer les filtres"),
    ("3", "Explorer les résultats"),
    ("4", "Consulter la décision"),
    ("5", "Exporter"),
]
for column, (number, label) in zip(journey_columns, journey_steps):
    with column:
        render_metric_card(f"Étape {number}", label, "Parcours guidé")

value_tab, features_tab, robustness_tab, publication_tab = st.tabs(
    [
        "Contexte & résultat",
        "Fonctionnalités",
        "Robustesse & limites",
        "Publication & sécurité",
    ]
)

with value_tab:
    st.markdown("#### Contexte")
    st.write(row["contexte"])

    st.markdown("#### Problématique")
    st.info(row["problematique"])

    st.markdown("#### Résultat")
    st.success(row["resultats"])

with features_tab:
    st.markdown(
        """
        - recherche plein texte via l’API Judilibre / PISTE ;
        - filtres par juridiction, chambre, période et volume ;
        - pagination et affichage tabulaire des décisions ;
        - récupération du texte complet à partir de l’identifiant ;
        - résumé heuristique et mise en cache ;
        - exports CSV, Excel, Word, PDF et ZIP.
        """
    )

    st.markdown("#### Stack technique")
    st.write(row["outils"])

with robustness_tab:
    st.markdown("#### Diagnostic d’un incident externe")
    st.write(
        "La taxonomie répondait correctement dans la sandbox, tandis que l’endpoint "
        "de recherche retournait une erreur serveur. Des appels directs ont permis "
        "d’isoler l’incident hors de l’application avant la bascule vers l’API PISTE "
        "de production."
    )

    st.markdown("#### Points de robustesse")
    st.markdown(
        """
        - délais d’attente définis sur les appels HTTP ;
        - gestion des réponses vides et des erreurs d’API ;
        - limitation du nombre de résultats chargés ;
        - cache des recherches et des décisions ;
        - génération du ZIP limitée à la page affichée.
        """
    )

    render_callout(
        "Compétence démontrée : distinguer une erreur applicative, un problème "
        "d’authentification et une indisponibilité du service externe.",
        accent="#b45309",
    )

    st.warning(
        "Les résumés sont heuristiques et l’application dépend de la disponibilité "
        "de l’API Judilibre. Elle constitue un outil d’aide à la recherche documentaire, "
        "pas une consultation juridique."
    )

with publication_tab:
    st.success(
        "Le package publiable a été contrôlé : aucun fichier secrets.toml, aucune clé API, "
        "aucun environnement virtuel et aucun cache Python n’y sont intégrés."
    )

    st.markdown(
        """
        **Contenu du package public**
        - `app.py` ;
        - `requirements.txt` ;
        - `README.md` ;
        - `.gitignore` ;
        - `secrets.example.toml` avec une valeur fictive ;
        - captures anonymisées et PDF de démonstration.

        **Principe de déploiement**
        - la clé PISTE est configurée uniquement dans les secrets Streamlit Cloud ;
        - elle n’est ni écrite dans le code ni ajoutée au dépôt GitHub ;
        - toute clé réellement exposée doit être révoquée et remplacée.
        """
    )

render_section_heading("Preuves visuelles")
st.caption(
    "Six captures documentent le parcours complet, de la formulation d’une requête "
    "à la génération des documents."
)

visuals = [
    (
        "01_interface_recherche_filtres.png",
        "Interface de recherche — opérateurs, juridiction, chambre, période et volume.",
    ),
    (
        "02_resultats_exports.png",
        "Résultats paginés — métadonnées, résumés et exports CSV, Excel et ZIP.",
    ),
    (
        "03_texte_integral_exports.png",
        "Texte intégral — consultation d’une décision et exports Word et PDF.",
    ),
    (
        "04_archive_zip_decisions.png",
        "Archive ZIP — un PDF généré pour chaque décision de la page affichée.",
    ),
    (
        "05_pdf_decision_exportee.png",
        "Décision exportée — métadonnées, texte complet et pagination.",
    ),
    (
        "06_aide_memo_utilisation.png",
        "Aide-mémo — accompagnement intégré dans la barre latérale.",
    ),
]

image_columns = st.columns(2)
for index, (filename, caption) in enumerate(visuals):
    image_path = JUD_ASSET_DIR / filename
    with image_columns[index % 2]:
        if image_path.exists():
            st.image(str(image_path), caption=caption, width="stretch")
        else:
            st.warning(f"Visuel manquant : {filename}")

render_section_heading("Livrables consultables")
st.caption(
    "La consultation de cette page est statique : aucun appel à l’API Judilibre "
    "n’est effectué depuis le portfolio."
)

source_zip_path = JUD_ASSET_DIR / "Judilibre_Explorer_source_publiable.zip"
visuals_pdf_path = JUD_ASSET_DIR / "Judilibre_Explorer_visuels_selectionnes.pdf"

download_columns = st.columns(2)
with download_columns[0]:
    if source_zip_path.exists():
        st.download_button(
            "💻 Télécharger le code source publiable",
            data=lambda file_path=source_zip_path: file_path.read_bytes(),
            file_name="Judilibre_Explorer_source_publiable.zip",
            mime="application/zip",
            key="download_jud_source",
            width="stretch",
        )

with download_columns[1]:
    if visuals_pdf_path.exists():
        st.download_button(
            "🖼️ Télécharger le PDF de démonstration",
            data=lambda file_path=visuals_pdf_path: file_path.read_bytes(),
            file_name="Judilibre_Explorer_visuels_selectionnes.pdf",
            mime="application/pdf",
            key="download_jud_visuals",
            width="stretch",
        )

render_callout(
    "Le package public sépare strictement le code, les preuves visuelles et les secrets "
    "d’exécution. La clé PISTE reste gérée hors du dépôt.",
    accent="#0f766e",
)
