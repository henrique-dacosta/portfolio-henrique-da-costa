from pathlib import Path

import streamlit as st

from utils import (
    inject_css,
    load_projects,
    render_badges,
    render_metric_card,
    render_page_header,
    render_section_heading,
    safe_text,
    split_badges,
)


ROOT = Path(__file__).resolve().parents[1]
P1_ASSET_DIR = ROOT / "assets" / "projets" / "P01"
P2_ASSET_DIR = ROOT / "assets" / "projets" / "P02"
P3_ASSET_DIR = ROOT / "assets" / "projets" / "P03"
P4_ASSET_DIR = ROOT / "assets" / "projets" / "P04"
P5_ASSET_DIR = ROOT / "assets" / "projets" / "P05"
P6_ASSET_DIR = ROOT / "assets" / "projets" / "P06"
P7_ASSET_DIR = ROOT / "assets" / "projets" / "P07"
P8_ASSET_DIR = ROOT / "assets" / "projets" / "P08"
P9_ASSET_DIR = ROOT / "assets" / "projets" / "P09"
P10_ASSET_DIR = ROOT / "assets" / "projets" / "P10"



def render_p1_evidence() -> None:
    """Affiche les preuves et livrables du projet P1."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "Deux preuves suffisent pour ce projet de cadrage : l’objectif professionnel "
        "et la cartographie initiale des compétences."
    )

    visuals = [
        (
            "01_objectif_professionnel.png",
            "Objectif professionnel - reconversion vers le conseil et la formation Data / BI, "
            "en capitalisant sur l’expertise métier et pédagogique.",
        ),
        (
            "02_cartographie_competences_initiales.png",
            "Auto-évaluation initiale - 35 compétences cartographiées pour distinguer "
            "les acquis, les compétences à consolider et les priorités d’apprentissage.",
        ),
    ]

    image_cols = st.columns(2)
    for index, (filename, caption) in enumerate(visuals):
        image_path = P1_ASSET_DIR / filename
        with image_cols[index % 2]:
            if image_path.exists():
                st.image(str(image_path), caption=caption, width="stretch")
            else:
                st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Repères du projet")
    metrics = st.columns(4)
    with metrics[0]:
        render_metric_card("Expérience métier", "30 ans", "expertise, audit, formation")
    with metrics[1]:
        render_metric_card("Compétences évaluées", "35", "référentiel BI Analyst")
    with metrics[2]:
        render_metric_card("Soft skills prioritaires", "5", "communication, autonomie, analyse…")
    with metrics[3]:
        render_metric_card("Rythme cible", "30 h/sem.", "organisation du parcours")

    st.markdown("#### Positionnement retenu")
    st.info(
        "Consultant-formateur Data & BI orienté métiers du chiffre, cabinets d’expertise comptable, "
        "TPE et organisations souhaitant fiabiliser leurs données et développer leurs outils décisionnels."
    )

    st.markdown("#### Livrables consultables")
    formation_path = P1_ASSET_DIR / "P1_fiche_debut_formation.pdf"
    metiers_path = P1_ASSET_DIR / "P1_decouverte_metier_soft_skills.pdf"
    autoeval_path = P1_ASSET_DIR / "P1_grille_auto_evaluation.pdf"
    visuals_path = P1_ASSET_DIR / "P1_visuels_selectionnes.pdf"

    first_row = st.columns(2)
    with first_row[0]:
        if formation_path.exists():
            st.download_button(
                "📄 Télécharger la fiche de début de formation",
                data=lambda file_path=formation_path: file_path.read_bytes(),
                file_name="P1_fiche_debut_formation.pdf",
                mime="application/pdf",
                key="download_p1_formation",
                width="stretch",
            )
    with first_row[1]:
        if metiers_path.exists():
            st.download_button(
                "🧭 Télécharger la fiche métier et soft skills",
                data=lambda file_path=metiers_path: file_path.read_bytes(),
                file_name="P1_decouverte_metier_soft_skills.pdf",
                mime="application/pdf",
                key="download_p1_metiers",
                width="stretch",
            )

    second_row = st.columns(2)
    with second_row[0]:
        if autoeval_path.exists():
            st.download_button(
                "📊 Télécharger la grille d’auto-évaluation",
                data=lambda file_path=autoeval_path: file_path.read_bytes(),
                file_name="P1_grille_auto_evaluation.pdf",
                mime="application/pdf",
                key="download_p1_autoeval",
                width="stretch",
            )
    with second_row[1]:
        if visuals_path.exists():
            st.download_button(
                "🖼️ Télécharger la synthèse visuelle P1",
                data=lambda file_path=visuals_path: file_path.read_bytes(),
                file_name="P1_visuels_selectionnes.pdf",
                mime="application/pdf",
                key="download_p1_visuals",
                width="stretch",
            )


def render_p2_evidence() -> None:
    """Affiche les preuves et livrables du projet P2."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "Deux preuves synthétisent le projet : une analyse chiffrée de l’efficacité "
        "et sa traduction en profils directement utilisables par le staff sportif."
    )

    visuals = [
        (
            "01_scoring_efficacite.png",
            "Scoring et efficacité - le volume de points est rapproché des indicateurs "
            "TS% et eFG% pour mesurer la qualité réelle de la production offensive.",
        ),
        (
            "02_profils_types.png",
            "Profils types - shooter extérieur, créateur sûr et protecteur du cercle, "
            "avec des seuils KPI utilisables pour l’entraînement et le recrutement.",
        ),
    ]

    image_cols = st.columns(2)
    for index, (filename, caption) in enumerate(visuals):
        image_path = P2_ASSET_DIR / filename
        with image_cols[index % 2]:
            if image_path.exists():
                st.image(str(image_path), caption=caption, width="stretch")
            else:
                st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Repères du projet")
    metrics = st.columns(4)
    with metrics[0]:
        render_metric_card("Joueurs analysés", "569", "saison NBA 2024-2025")
    with metrics[1]:
        render_metric_card("Équipes", "30", "ensemble de la ligue")
    with metrics[2]:
        render_metric_card("Axes de performance", "3", "attaque, création, défense")
    with metrics[3]:
        render_metric_card("Profils types", "3", "KPI opérationnels")

    st.markdown("#### Enseignements pour Les Pionniers")
    st.info(
        "La performance ne repose pas seulement sur le volume : qualité de sélection des tirs, "
        "discipline dans la création et impact défensif doivent être suivis conjointement. "
        "Le projet propose des indicateurs réplicables sur les joueurs du club."
    )

    st.markdown("#### Livrables consultables")
    source_path = P2_ASSET_DIR / "P2_donnees_NBA_source.xlsx"
    report_path = P2_ASSET_DIR / "P2_rapport_analyse.xlsx"
    pptx_path = P2_ASSET_DIR / "P2_presentation.pptx"
    presentation_pdf_path = P2_ASSET_DIR / "P2_presentation.pdf"
    visuals_path = P2_ASSET_DIR / "P2_visuels_selectionnes.pdf"

    first_row = st.columns(2)
    with first_row[0]:
        if source_path.exists():
            st.download_button(
                "🏀 Télécharger les données NBA",
                data=lambda file_path=source_path: file_path.read_bytes(),
                file_name="P2_donnees_NBA_source.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_p2_data",
                width="stretch",
            )
    with first_row[1]:
        if report_path.exists():
            st.download_button(
                "📊 Télécharger le rapport d’analyse Excel",
                data=lambda file_path=report_path: file_path.read_bytes(),
                file_name="P2_rapport_analyse.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_p2_report",
                width="stretch",
            )

    second_row = st.columns(2)
    with second_row[0]:
        if pptx_path.exists():
            st.download_button(
                "📽️ Télécharger la présentation PowerPoint",
                data=lambda file_path=pptx_path: file_path.read_bytes(),
                file_name="P2_presentation.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                key="download_p2_pptx",
                width="stretch",
            )
    with second_row[1]:
        if presentation_pdf_path.exists():
            st.download_button(
                "📄 Télécharger la présentation en PDF",
                data=lambda file_path=presentation_pdf_path: file_path.read_bytes(),
                file_name="P2_presentation.pdf",
                mime="application/pdf",
                key="download_p2_presentation_pdf",
                width="stretch",
            )

    if visuals_path.exists():
        st.download_button(
            "🖼️ Télécharger les visuels sélectionnés",
            data=lambda file_path=visuals_path: file_path.read_bytes(),
            file_name="P2_visuels_selectionnes.pdf",
            mime="application/pdf",
            key="download_p2_visuals",
            width="stretch",
        )


def render_p3_evidence() -> None:
    """Affiche les preuves et livrables du projet P3."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "Deux preuves résument la progression : la construction du modèle relationnel "
        "puis une requête avancée combinant normalisation, filtrage et agrégation."
    )

    visuals = [
        (
            "01_schema_relationnel.png",
            "Schéma relationnel - tables contrat et region reliées par "
            "Code_dep_code_commune, avec clés, index et volumétrie.",
        ),
        (
            "02_requete_avancee_paris.png",
            "Cas avancé - normalisation des libellés de Paris dans une CTE, "
            "puis calcul de la surface moyenne sur les vingt arrondissements.",
        ),
    ]

    image_cols = st.columns(2)
    for index, (filename, caption) in enumerate(visuals):
        image_path = P3_ASSET_DIR / filename
        with image_cols[index % 2]:
            if image_path.exists():
                st.image(str(image_path), caption=caption, width="stretch")
            else:
                st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Repères du projet")
    metrics = st.columns(4)
    with metrics[0]:
        render_metric_card("Tables relationnelles", "2", "contrat et region")
    with metrics[1]:
        render_metric_card("Contrats", "30 335", "assurance logement")
    with metrics[2]:
        render_metric_card("Références géographiques", "38 916", "communes et territoires")
    with metrics[3]:
        render_metric_card("Requêtes documentées", "12", "du SELECT à la CTE")

    st.markdown("#### Résultats métier")
    st.info(
        "La base permet de lister, compter, moyenner et classer les contrats par territoire. "
        "Exemples : cotisation mensuelle moyenne de 19,33 €, surface moyenne parisienne de 51,77 m² "
        "et 14 177 contrats recensés en Île-de-France."
    )

    st.markdown("#### Livrables consultables")
    livrables_p3 = [
        {
            "label": "🗃️ Télécharger les sources CSV",
            "path": P3_ASSET_DIR / "P3_sources_CSV.zip",
            "file_name": "P3_sources_CSV.zip",
            "mime": "application/zip",
            "key": "download_p3_sources",
        },
        {
            "label": "🧩 Télécharger le document technique",
            "path": P3_ASSET_DIR / "P3_document_technique.pdf",
            "file_name": "P3_document_technique.pdf",
            "mime": "application/pdf",
            "key": "download_p3_technical",
        },
        {
            "label": "🧾 Télécharger les requêtes et résultats",
            "path": P3_ASSET_DIR / "P3_liste_requetes_et_resultats.pdf",
            "file_name": "P3_liste_requetes_et_resultats.pdf",
            "mime": "application/pdf",
            "key": "download_p3_queries",
        },
        {
            "label": "📽️ Télécharger la présentation PowerPoint",
            "path": P3_ASSET_DIR / "P3_presentation.pptx",
            "file_name": "P3_presentation.pptx",
            "mime": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "key": "download_p3_pptx",
        },
        {
            "label": "📄 Télécharger la présentation en PDF",
            "path": P3_ASSET_DIR / "P3_presentation.pdf",
            "file_name": "P3_presentation.pdf",
            "mime": "application/pdf",
            "key": "download_p3_presentation_pdf",
        },
        {
            "label": "✅ Télécharger la grille d’autoévaluation",
            "path": P3_ASSET_DIR / "P3_grille_autoevaluation.pdf",
            "file_name": "P3_grille_autoevaluation.pdf",
            "mime": "application/pdf",
            "key": "download_p3_evaluation",
        },
        {
            "label": "🖼️ Télécharger les visuels sélectionnés",
            "path": P3_ASSET_DIR / "P3_visuels_selectionnes.pdf",
            "file_name": "P3_visuels_selectionnes.pdf",
            "mime": "application/pdf",
            "key": "download_p3_visuals",
        },
    ]

    livrables_p3_disponibles = [
        livrable for livrable in livrables_p3 if livrable["path"].exists()
    ]

    if livrables_p3_disponibles:
        cols = st.columns(2)
        for index, livrable in enumerate(livrables_p3_disponibles):
            with cols[index % 2]:
                st.download_button(
                    livrable["label"],
                    data=lambda file_path=livrable["path"]: file_path.read_bytes(),
                    file_name=livrable["file_name"],
                    mime=livrable["mime"],
                    key=livrable["key"],
                    width="stretch",
                )

    archive_path = P3_ASSET_DIR / "P3_documents_et_preuves.zip"
    if archive_path.exists():
        st.download_button(
            "📦 Télécharger l’archive complète P3",
            data=lambda file_path=archive_path: file_path.read_bytes(),
            file_name="P3_documents_et_preuves.zip",
            mime="application/zip",
            key="download_p3_archive",
            width="stretch",
        )


def render_p4_evidence() -> None:
    """Affiche les preuves et livrables publics du projet P4."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "Deux preuves présentent la chaîne de conformité : les étapes Power Query "
        "et le jeu de données anonymisé remis au service marketing."
    )

    visuals = [
        (
            "01_pipeline_power_query.png",
            "Pipeline Power Query - pseudonymisation, familles de métiers, tranches "
            "et suppression progressive des variables fines.",
        ),
        (
            "02_base_anonymisee_finale.png",
            "Base anonymisée finale - aucune donnée directement identifiante et "
            "variables sensibles remplacées par des catégories exploitables.",
        ),
    ]

    image_cols = st.columns(2)
    for index, (filename, caption) in enumerate(visuals):
        image_path = P4_ASSET_DIR / filename
        with image_cols[index % 2]:
            if image_path.exists():
                st.image(str(image_path), caption=caption, width="stretch")
            else:
                st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Repères du projet")
    metrics = st.columns(4)
    with metrics[0]:
        render_metric_card("Base CRM source", "10 302", "enregistrements contrôlés")
    with metrics[1]:
        render_metric_card("Périmètre retenu", "1 158", "dossiers complets de 2022")
    with metrics[2]:
        render_metric_card("Jeu public", "19 colonnes", "sans identifiant direct")
    with metrics[3]:
        render_metric_card("Recommandations RGPD", "5", "gouvernance et sécurité")

    st.markdown("#### Démarche de conformité")
    st.info(
        "L’identifiant client est pseudonymisé et neuf variables fines sont généralisées : "
        "métier, âge, date de demande, tarif, revenus, valeur de résidence, nombre d’enfants, "
        "points perdus et âge du véhicule."
    )

    st.warning(
        "La base CRM source, l’export SQL intermédiaire et la table de correspondance "
        "Mapping_ID sont volontairement exclus des téléchargements publics."
    )

    st.markdown("#### Livrables consultables")
    data_path = P4_ASSET_DIR / "P4_donnees_anonymisees.zip"
    recommendations_path = P4_ASSET_DIR / "P4_recommandations_RGPD.pdf"
    report_path = P4_ASSET_DIR / "P4_rapport_public.pdf"
    evaluation_path = P4_ASSET_DIR / "P4_grille_autoevaluation.pdf"
    dictionary_path = P4_ASSET_DIR / "P4_dictionnaire_donnees.pdf"
    mission_path = P4_ASSET_DIR / "P4_etapes_mission.pdf"
    visuals_path = P4_ASSET_DIR / "P4_visuels_selectionnes.pdf"
    archive_path = P4_ASSET_DIR / "P4_livrables_publics.zip"

    first_row = st.columns(2)
    with first_row[0]:
        if data_path.exists():
            st.download_button(
                "🛡️ Télécharger les données anonymisées",
                data=lambda file_path=data_path: file_path.read_bytes(),
                file_name="P4_donnees_anonymisees.zip",
                mime="application/zip",
                key="download_p4_data",
                width="stretch",
            )
    with first_row[1]:
        if recommendations_path.exists():
            st.download_button(
                "📋 Télécharger les recommandations RGPD",
                data=lambda file_path=recommendations_path: file_path.read_bytes(),
                file_name="P4_recommandations_RGPD.pdf",
                mime="application/pdf",
                key="download_p4_recommendations",
                width="stretch",
            )

    second_row = st.columns(2)
    with second_row[0]:
        if report_path.exists():
            st.download_button(
                "📄 Télécharger le rapport public",
                data=lambda file_path=report_path: file_path.read_bytes(),
                file_name="P4_rapport_public.pdf",
                mime="application/pdf",
                key="download_p4_report",
                width="stretch",
            )
    with second_row[1]:
        if visuals_path.exists():
            st.download_button(
                "🖼️ Télécharger les visuels sélectionnés",
                data=lambda file_path=visuals_path: file_path.read_bytes(),
                file_name="P4_visuels_selectionnes.pdf",
                mime="application/pdf",
                key="download_p4_visuals",
                width="stretch",
            )

    third_row = st.columns(2)
    with third_row[0]:
        if dictionary_path.exists():
            st.download_button(
                "📚 Télécharger le dictionnaire de données",
                data=lambda file_path=dictionary_path: file_path.read_bytes(),
                file_name="P4_dictionnaire_donnees.pdf",
                mime="application/pdf",
                key="download_p4_dictionary",
                width="stretch",
            )
    with third_row[1]:
        if mission_path.exists():
            st.download_button(
                "🧭 Télécharger les étapes de la mission",
                data=lambda file_path=mission_path: file_path.read_bytes(),
                file_name="P4_etapes_mission.pdf",
                mime="application/pdf",
                key="download_p4_mission",
                width="stretch",
            )

    fourth_row = st.columns(2)
    with fourth_row[0]:
        if evaluation_path.exists():
            st.download_button(
                "✅ Télécharger la grille d’autoévaluation",
                data=lambda file_path=evaluation_path: file_path.read_bytes(),
                file_name="P4_grille_autoevaluation.pdf",
                mime="application/pdf",
                key="download_p4_evaluation",
                width="stretch",
            )
    with fourth_row[1]:
        if archive_path.exists():
            st.download_button(
                "📦 Télécharger l’archive publique complète",
                data=lambda file_path=archive_path: file_path.read_bytes(),
                file_name="P4_livrables_publics.zip",
                mime="application/zip",
                key="download_p4_archive",
                width="stretch",
            )


def render_p5_evidence() -> None:
    """Affiche les preuves et livrables du projet P5."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "Le projet est présenté en deux temps : fiabilisation du modèle relationnel, "
        "puis restitution synthétique des indicateurs de satisfaction."
    )

    visuals = [
        (
            "01_schema_relationnel_normalise.png",
            "Schéma relationnel - trois tables reliées autour de retour_client, "
            "avec clés primaires et étrangères identifiées.",
        ),
        (
            "02_vue_synthetique_satisfaction.png",
            "Vue décisionnelle - NPS, recommandation, produits, magasins, canaux "
            "et expérience client réunis dans une synthèse opérationnelle.",
        ),
    ]

    for filename, caption in visuals:
        image_path = P5_ASSET_DIR / filename
        if image_path.exists():
            st.image(str(image_path), caption=caption, width="stretch")
        else:
            st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Repères du projet")
    metrics = st.columns(4)
    with metrics[0]:
        render_metric_card("Retours clients", "3 000", "voix du client analysée")
    with metrics[1]:
        render_metric_card("Produits / magasins", "145 / 84", "référentiels reliés")
    with metrics[2]:
        render_metric_card("Questions métier", "17", "requêtes SQL documentées")
    with metrics[3]:
        render_metric_card("NPS global", "31,0", "promoteurs - détracteurs")

    st.markdown("#### Enseignements métier")
    st.info(
        "La note moyenne atteint 8,05/10 et 90,9 % des répondants déclarent recommander l’enseigne. "
        "Le téléphone affiche le meilleur NPS par canal, tandis que la lecture magasin permet "
        "de cibler les points de vente à fort volume mais sous la moyenne."
    )

    st.markdown("#### Livrables consultables")
    sources_path = P5_ASSET_DIR / "P5_sources_et_base.zip"
    technical_path = P5_ASSET_DIR / "P5_dossier_technique.zip"
    expression_path = P5_ASSET_DIR / "P5_expression_des_besoins.pdf"
    sql_path = P5_ASSET_DIR / "P5_script_SQL_17_questions.sql"
    pptx_path = P5_ASSET_DIR / "P5_presentation.pptx"
    presentation_pdf_path = P5_ASSET_DIR / "P5_presentation.pdf"
    visuals_path = P5_ASSET_DIR / "P5_visuels_selectionnes.pdf"
    archive_path = P5_ASSET_DIR / "P5_documents_et_preuves.zip"

    first_row = st.columns(2)
    with first_row[0]:
        if sources_path.exists():
            st.download_button(
                "🗃️ Télécharger les sources et la base SQLite",
                data=lambda file_path=sources_path: file_path.read_bytes(),
                file_name="P5_sources_et_base.zip",
                mime="application/zip",
                key="download_p5_sources",
                width="stretch",
            )
    with first_row[1]:
        if technical_path.exists():
            st.download_button(
                "🧩 Télécharger le dossier technique",
                data=lambda file_path=technical_path: file_path.read_bytes(),
                file_name="P5_dossier_technique.zip",
                mime="application/zip",
                key="download_p5_technical",
                width="stretch",
            )

    second_row = st.columns(2)
    with second_row[0]:
        if expression_path.exists():
            st.download_button(
                "📝 Télécharger l’expression des besoins",
                data=lambda file_path=expression_path: file_path.read_bytes(),
                file_name="P5_expression_des_besoins.pdf",
                mime="application/pdf",
                key="download_p5_expression",
                width="stretch",
            )
    with second_row[1]:
        if sql_path.exists():
            st.download_button(
                "💾 Télécharger le script SQL des 17 questions",
                data=lambda file_path=sql_path: file_path.read_bytes(),
                file_name="P5_script_SQL_17_questions.sql",
                mime="text/plain",
                key="download_p5_sql",
                width="stretch",
            )

    third_row = st.columns(2)
    with third_row[0]:
        if pptx_path.exists():
            st.download_button(
                "📽️ Télécharger la présentation PowerPoint",
                data=lambda file_path=pptx_path: file_path.read_bytes(),
                file_name="P5_presentation.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                key="download_p5_pptx",
                width="stretch",
            )
    with third_row[1]:
        if presentation_pdf_path.exists():
            st.download_button(
                "📄 Télécharger la présentation en PDF",
                data=lambda file_path=presentation_pdf_path: file_path.read_bytes(),
                file_name="P5_presentation.pdf",
                mime="application/pdf",
                key="download_p5_presentation_pdf",
                width="stretch",
            )

    fourth_row = st.columns(2)
    with fourth_row[0]:
        if visuals_path.exists():
            st.download_button(
                "🖼️ Télécharger les visuels sélectionnés",
                data=lambda file_path=visuals_path: file_path.read_bytes(),
                file_name="P5_visuels_selectionnes.pdf",
                mime="application/pdf",
                key="download_p5_visuals",
                width="stretch",
            )
    with fourth_row[1]:
        if archive_path.exists():
            st.download_button(
                "📦 Télécharger l’archive complète P5",
                data=lambda file_path=archive_path: file_path.read_bytes(),
                file_name="P5_documents_et_preuves.zip",
                mime="application/zip",
                key="download_p5_archive",
                width="stretch",
            )

def render_p6_evidence() -> None:
    """Affiche la première galerie de preuves intégrée au portfolio : projet P6."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "Quatre visuels synthétiques montrent la chaîne complète : consolidation des sources, "
        "nettoyage, analyse du chiffre d’affaires et lecture des corrélations."
    )

    visuals = [
        (
            "01_pipeline_sources_dataset.png",
            "Pipeline de traitement - des sources ERP, liaison et Web au dataset final exploitable.",
        ),
        (
            "02_nettoyage_web_1513_714.png",
            "Nettoyage Web - réduction de 1 513 lignes brutes à 714 produits exploitables.",
        ),
        (
            "03_pareto_chiffre_affaires.png",
            "Analyse Pareto - 61 % du catalogue concentre 80 % du chiffre d’affaires, sans profil 80/20 classique.",
        ),
        (
            "04_correlations_prix_ventes_stock.png",
            "Corrélations - lecture croisée des relations entre prix, ventes et stock avec Pearson et Spearman.",
        ),
    ]

    image_cols = st.columns(2)
    for index, (filename, caption) in enumerate(visuals):
        image_path = P6_ASSET_DIR / filename
        with image_cols[index % 2]:
            if image_path.exists():
                st.image(str(image_path), caption=caption, width="stretch")
            else:
                st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Résultats clés")
    result_cols = st.columns(3)
    with result_cols[0]:
        render_metric_card("Sources consolidées", "3", "ERP, liaison et Web")
    with result_cols[1]:
        render_metric_card("Produits consolidés", "713", "Périmètre final exploitable")
    with result_cols[2]:
        render_metric_card("Lecture Pareto", "61 %", "du catalogue pour 80 % du CA")

    st.markdown("#### Livrables consultables")
    st.caption(
        "Quatre niveaux de preuve sont proposés : restitution, traitement reproductible, "
        "lecture rapide des graphiques et jeux de données pédagogiques d’entrée."
    )

    presentation_path = P6_ASSET_DIR / "P6_presentation_Bottleneck.pdf"
    notebook_path = P6_ASSET_DIR / "P6_notebook_Bottleneck.ipynb"
    visuals_pdf_path = P6_ASSET_DIR / "P6_visuels_notebook_complets.pdf"
    source_data_path = P6_ASSET_DIR / "P6_donnees_entree.zip"

    first_row = st.columns(2)
    with first_row[0]:
        if presentation_path.exists():
            st.download_button(
                "📄 Télécharger la présentation en PDF",
                data=lambda file_path=presentation_path: file_path.read_bytes(),
                file_name="P6_Bottleneck_presentation.pdf",
                mime="application/pdf",
                key="download_p6_presentation",
                width="stretch",
            )
    with first_row[1]:
        if notebook_path.exists():
            st.download_button(
                "📓 Télécharger le notebook P6",
                data=lambda file_path=notebook_path: file_path.read_bytes(),
                file_name="P6_Bottleneck_notebook.ipynb",
                mime="application/x-ipynb+json",
                key="download_p6_notebook",
                width="stretch",
            )

    second_row = st.columns(2)
    with second_row[0]:
        if visuals_pdf_path.exists():
            st.download_button(
                "📊 Télécharger tous les visuels du notebook",
                data=lambda file_path=visuals_pdf_path: file_path.read_bytes(),
                file_name="P6_Bottleneck_visuels_notebook.pdf",
                mime="application/pdf",
                key="download_p6_visuals_pdf",
                width="stretch",
            )
    with second_row[1]:
        if source_data_path.exists():
            st.download_button(
                "🗂️ Télécharger les données d’entrée",
                data=lambda file_path=source_data_path: file_path.read_bytes(),
                file_name="P6_Bottleneck_donnees_entree.zip",
                mime="application/zip",
                key="download_p6_source_data",
                width="stretch",
            )



def render_p7_evidence() -> None:
    """Affiche les preuves visuelles et les livrables du projet P7 Sanitoral."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "La sélection relie le cadrage utilisateur, l’architecture du modèle et les trois axes "
        "de pilotage du portefeuille : coûts, délais et livrables."
    )

    visuals = [
        (
            "01_product_strategy_canvas.png",
            "Product Strategy Canvas - objectifs, profils utilisateurs et neuf user stories.",
        ),
        (
            "02_modele_relationnel_power_bi.png",
            "Modèle relationnel Power BI - faits planifiés/réels, dimensions projet, phase, pays et dates.",
        ),
        (
            "03_vue_globale_portefeuille.png",
            "Vue globale - variance pondérée, carte mondiale, projets, pays et régions prioritaires.",
        ),
        (
            "04_kpi_couts.png",
            "Pilotage des coûts - réalisé versus planifié, alertes et projets à investiguer.",
        ),
        (
            "05_kpi_delais.png",
            "Pilotage des délais - variance de durée, projets en retard et répartition par phase.",
        ),
        (
            "06_kpi_livrables.png",
            "Pilotage des livrables - écarts au planning et pays nécessitant une action corrective.",
        ),
    ]

    image_cols = st.columns(2)
    for index, (filename, caption) in enumerate(visuals):
        image_path = P7_ASSET_DIR / filename
        with image_cols[index % 2]:
            if image_path.exists():
                st.image(str(image_path), caption=caption, width="stretch")
            else:
                st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Résultats clés")
    result_cols = st.columns(4)
    with result_cols[0]:
        render_metric_card("Portefeuille", "104", "projets IT et Marketing")
    with result_cols[1]:
        render_metric_card("Axes pilotés", "3", "coûts, délais, livrables")
    with result_cols[2]:
        render_metric_card("Niveaux de lecture", "3", "DG, région et pays")
    with result_cols[3]:
        render_metric_card("Seuil d’alerte", "15 %", "écart réel / prévisionnel")

    st.markdown("#### Livrables consultables")
    st.caption(
        "Le PBIX permet d’examiner le modèle et les mesures dans Power BI Desktop. "
        "Les PDF offrent une consultation immédiate, tandis que l’archive rassemble les sources pédagogiques et la documentation."
    )

    pbix_path = P7_ASSET_DIR / "P7_Sanitoral_tableau_de_bord.pbix"
    dashboard_pdf_path = P7_ASSET_DIR / "P7_Sanitoral_tableau_de_bord.pdf"
    selected_visuals_path = P7_ASSET_DIR / "P7_Sanitoral_visuels_selectionnes.pdf"
    sources_path = P7_ASSET_DIR / "P7_Sanitoral_sources_et_methodologie.zip"

    first_row = st.columns(2)
    with first_row[0]:
        if pbix_path.exists():
            st.download_button(
                "📊 Télécharger le fichier Power BI",
                data=lambda file_path=pbix_path: file_path.read_bytes(),
                file_name="P7_Sanitoral_tableau_de_bord.pbix",
                mime="application/octet-stream",
                key="download_p7_pbix",
                width="stretch",
            )
    with first_row[1]:
        if dashboard_pdf_path.exists():
            st.download_button(
                "📄 Télécharger le tableau de bord en PDF",
                data=lambda file_path=dashboard_pdf_path: file_path.read_bytes(),
                file_name="P7_Sanitoral_tableau_de_bord.pdf",
                mime="application/pdf",
                key="download_p7_dashboard_pdf",
                width="stretch",
            )

    second_row = st.columns(2)
    with second_row[0]:
        if selected_visuals_path.exists():
            st.download_button(
                "🖼️ Télécharger les visuels sélectionnés",
                data=lambda file_path=selected_visuals_path: file_path.read_bytes(),
                file_name="P7_Sanitoral_visuels_selectionnes.pdf",
                mime="application/pdf",
                key="download_p7_selected_visuals",
                width="stretch",
            )
    with second_row[1]:
        if sources_path.exists():
            st.download_button(
                "🗂️ Télécharger les sources et la méthodologie",
                data=lambda file_path=sources_path: file_path.read_bytes(),
                file_name="P7_Sanitoral_sources_et_methodologie.zip",
                mime="application/zip",
                key="download_p7_sources",
                width="stretch",
            )


def render_p8_evidence() -> None:
    """Affiche les preuves visuelles et les livrables du projet P8 Immobilier Paris."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "La sélection raconte le projet de bout en bout : compréhension du marché, "
        "segmentation géographique, comparaison des modèles, valorisation, contrôle métier "
        "et classification automatique des opportunités."
    )

    visuals = [
        (
            "01_evolution_marche_parisien.png",
            "Marché parisien - hausse d’environ 10 % du prix moyen des appartements entre 2017 et 2021.",
        ),
        (
            "02_segmentation_geographique.png",
            "Segmentation géographique - des niveaux de prix durablement différenciés entre arrondissements.",
        ),
        (
            "03_benchmark_pycaret.png",
            "Benchmark PyCaret - LightGBM retenu comme modèle champion avec une MAPE de 3,06 %.",
        ),
        (
            "04_comparaison_valorisations.png",
            "Valorisation - comparaison des scénarios sklearn et PyCaret par segment de portefeuille.",
        ),
        (
            "05_controle_coherence_iqr.png",
            "Contrôle métier - baisse des prédictions hors bornes IQR historiques avec PyCaret.",
        ),
        (
            "06_resultat_clustering.png",
            "Classification K-Means - deux groupes de 20 opportunités clairement séparés par le prix au m².",
        ),
    ]

    image_cols = st.columns(2)
    for index, (filename, caption) in enumerate(visuals):
        image_path = P8_ASSET_DIR / filename
        with image_cols[index % 2]:
            if image_path.exists():
                st.image(str(image_path), caption=caption, width="stretch")
            else:
                st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Résultats clés")
    result_cols = st.columns(4)
    with result_cols[0]:
        render_metric_card("Historique analysé", "26 180", "transactions après dédoublonnage")
    with result_cols[1]:
        render_metric_card("Modèle champion", "3,06 %", "MAPE LightGBM")
    with result_cols[2]:
        render_metric_card("Valorisation retenue", "153,31 M€", "scénario PyCaret")
    with result_cols[3]:
        render_metric_card("Opportunités classées", "40", "deux clusters de 20 biens")

    st.markdown("#### Livrables consultables")
    st.caption(
        "Les supports combinent restitution business, code reproductible, lecture synthétique "
        "des visuels et données pédagogiques d’entrée."
    )

    presentation_pdf_path = P8_ASSET_DIR / "P8_presentation_immobilier.pdf"
    presentation_pptx_path = P8_ASSET_DIR / "P8_presentation_immobilier.pptx"
    notebook_path = P8_ASSET_DIR / "P8_notebook_immobilier.ipynb"
    notebook_visuals_path = P8_ASSET_DIR / "P8_visuels_notebook_complets.pdf"
    selected_visuals_path = P8_ASSET_DIR / "P8_visuels_selectionnes.pdf"
    source_data_path = P8_ASSET_DIR / "P8_donnees_entree.zip"

    first_row = st.columns(2)
    with first_row[0]:
        if presentation_pdf_path.exists():
            st.download_button(
                "📄 Télécharger la présentation en PDF",
                data=lambda file_path=presentation_pdf_path: file_path.read_bytes(),
                file_name="P8_Immobilier_presentation.pdf",
                mime="application/pdf",
                key="download_p8_presentation_pdf",
                width="stretch",
            )
    with first_row[1]:
        if presentation_pptx_path.exists():
            st.download_button(
                "📽️ Télécharger la présentation en PowerPoint",
                data=lambda file_path=presentation_pptx_path: file_path.read_bytes(),
                file_name="P8_Immobilier_presentation.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                key="download_p8_presentation_pptx",
                width="stretch",
            )

    second_row = st.columns(2)
    with second_row[0]:
        if notebook_path.exists():
            st.download_button(
                "📓 Télécharger le notebook P8",
                data=lambda file_path=notebook_path: file_path.read_bytes(),
                file_name="P8_Immobilier_notebook.ipynb",
                mime="application/x-ipynb+json",
                key="download_p8_notebook",
                width="stretch",
            )
    with second_row[1]:
        if notebook_visuals_path.exists():
            st.download_button(
                "📊 Télécharger tous les visuels du notebook",
                data=lambda file_path=notebook_visuals_path: file_path.read_bytes(),
                file_name="P8_Immobilier_visuels_notebook.pdf",
                mime="application/pdf",
                key="download_p8_notebook_visuals",
                width="stretch",
            )

    third_row = st.columns(2)
    with third_row[0]:
        if selected_visuals_path.exists():
            st.download_button(
                "🖼️ Télécharger les visuels sélectionnés",
                data=lambda file_path=selected_visuals_path: file_path.read_bytes(),
                file_name="P8_Immobilier_visuels_selectionnes.pdf",
                mime="application/pdf",
                key="download_p8_selected_visuals",
                width="stretch",
            )
    with third_row[1]:
        if source_data_path.exists():
            st.download_button(
                "🗂️ Télécharger les données d’entrée",
                data=lambda file_path=source_data_path: file_path.read_bytes(),
                file_name="P8_Immobilier_donnees_entree.zip",
                mime="application/zip",
                key="download_p8_source_data",
                width="stretch",
            )


def render_p9_evidence() -> None:
    """Affiche les preuves visuelles et les livrables du projet P9 Bottleneck BI."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "La sélection montre le passage d’une base SQLite auditée à un modèle Power BI "
        "orienté pilotage : vue exécutive, marge, stocks, segments et promotions."
    )

    visuals = [
        (
            "01_modele_relationnel_power_bi.png",
            "Modèle relationnel Power BI - table de faits produit × mois, dimension produit et calendrier.",
        ),
        (
            "02_vue_ensemble_dashboard.png",
            "Vue d’ensemble - chiffre d’affaires, marge, volumes, tendances et alertes de pilotage.",
        ),
        (
            "03_marge_inflation_fournisseurs.png",
            "Marge et inflation - prix d’achat, taux de marge et produits les plus exposés.",
        ),
        (
            "04_ventes_stocks.png",
            "Ventes et stocks - commandes, rotation, couverture et risques de rupture ou de surstockage.",
        ),
        (
            "05_produits_segments_sans_alcool.png",
            "Produits et segments - contribution au CA, marge, produits leaders et suivi du sans alcool.",
        ),
        (
            "06_promotions.png",
            "Promotions - contribution au chiffre d’affaires, marge et performance des références remisées.",
        ),
    ]

    image_cols = st.columns(2)
    for index, (filename, caption) in enumerate(visuals):
        image_path = P9_ASSET_DIR / filename
        with image_cols[index % 2]:
            if image_path.exists():
                st.image(str(image_path), caption=caption, width="stretch")
            else:
                st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Résultats clés")
    result_cols = st.columns(4)
    with result_cols[0]:
        render_metric_card("Tables auditées", "4", "Web, Finance, Sales, Promo")
    with result_cols[1]:
        render_metric_card("Catalogue actif", "761 SKU", "référentiel produit exploitable")
    with result_cols[2]:
        render_metric_card("Chiffre d’affaires", "2,37 M€", "période 10/2022 - 09/2023")
    with result_cols[3]:
        render_metric_card("Taux de marge", "46,86 %", "lecture consolidée")

    st.markdown("#### Livrables consultables")
    st.caption(
        "Les livrables permettent d’examiner le modèle Power BI, le dashboard, "
        "l’analyse d’architecture et l’ensemble des sources pédagogiques utilisées."
    )

    pbix_path = P9_ASSET_DIR / "P9_Bottleneck_tableau_de_bord.pbix"
    dashboard_pdf_path = P9_ASSET_DIR / "P9_Bottleneck_tableau_de_bord.pdf"
    report_path = P9_ASSET_DIR / "P9_Bottleneck_rapport_analyse.pdf"
    selected_visuals_path = P9_ASSET_DIR / "P9_Bottleneck_visuels_selectionnes.pdf"
    sources_path = P9_ASSET_DIR / "P9_Bottleneck_sources_et_methodologie.zip"

    first_row = st.columns(2)
    with first_row[0]:
        if pbix_path.exists():
            st.download_button(
                "📊 Télécharger le fichier Power BI",
                data=lambda file_path=pbix_path: file_path.read_bytes(),
                file_name="P9_Bottleneck_tableau_de_bord.pbix",
                mime="application/octet-stream",
                key="download_p9_pbix",
                width="stretch",
            )
    with first_row[1]:
        if dashboard_pdf_path.exists():
            st.download_button(
                "📄 Télécharger le tableau de bord en PDF",
                data=lambda file_path=dashboard_pdf_path: file_path.read_bytes(),
                file_name="P9_Bottleneck_tableau_de_bord.pdf",
                mime="application/pdf",
                key="download_p9_dashboard_pdf",
                width="stretch",
            )

    second_row = st.columns(2)
    with second_row[0]:
        if report_path.exists():
            st.download_button(
                "📝 Télécharger le rapport d’analyse",
                data=lambda file_path=report_path: file_path.read_bytes(),
                file_name="P9_Bottleneck_rapport_analyse.pdf",
                mime="application/pdf",
                key="download_p9_report",
                width="stretch",
            )
    with second_row[1]:
        if selected_visuals_path.exists():
            st.download_button(
                "🖼️ Télécharger les visuels sélectionnés",
                data=lambda file_path=selected_visuals_path: file_path.read_bytes(),
                file_name="P9_Bottleneck_visuels_selectionnes.pdf",
                mime="application/pdf",
                key="download_p9_selected_visuals",
                width="stretch",
            )

    if sources_path.exists():
        st.download_button(
            "🗂️ Télécharger la base, le schéma, le dictionnaire et les requêtes SQL",
            data=lambda file_path=sources_path: file_path.read_bytes(),
            file_name="P9_Bottleneck_sources_et_methodologie.zip",
            mime="application/zip",
            key="download_p9_sources",
            width="stretch",
        )



def render_p10_evidence() -> None:
    """Affiche les preuves visuelles et les livrables du projet P10 UOI Games."""
    st.divider()
    st.markdown("#### Preuves visuelles sélectionnées")
    st.caption(
        "La sélection montre le cheminement décisionnel : dimension du marché, "
        "signal consommateur, diagnostic stratégique, scoring des segments, "
        "arbitrage du risque et recommandation finale."
    )

    visuals = [
        (
            "01_marche_mondial_2025.png",
            "Marché - 188,8 Md$ en 2025 et une projection à 206,5 Md$ en 2028.",
        ),
        (
            "02_questionnaire_consommateurs.png",
            "Questionnaire - signal exploratoire favorable à l’action-aventure et au PC.",
        ),
        (
            "03_swot_uoi_games.png",
            "SWOT - opportunité commerciale réelle, mais forte exigence de différenciation et d’exécution.",
        ),
        (
            "04_classement_segments.png",
            "Scoring - l’action-aventure AAA ressort en tête avec 4,54 sur 5.",
        ),
        (
            "05_matrice_attractivite_faisabilite.png",
            "Attractivité / faisabilité - arbitrage entre potentiel international et risque de production.",
        ),
        (
            "06_recommandation_finale.png",
            "Recommandation - nouvelle licence action-aventure premium, PC et consoles, modèle digital.",
        ),
    ]

    image_cols = st.columns(2)
    for index, (filename, caption) in enumerate(visuals):
        image_path = P10_ASSET_DIR / filename
        with image_cols[index % 2]:
            if image_path.exists():
                st.image(str(image_path), caption=caption, width="stretch")
            else:
                st.warning(f"Visuel manquant : {filename}")

    st.markdown("#### Résultats clés")
    result_cols = st.columns(4)
    with result_cols[0]:
        render_metric_card("Marché mondial 2025", "188,8 Md$", "projection 2028 : 206,5 Md$")
    with result_cols[1]:
        render_metric_card("Signal questionnaire", "71,4 %", "citent action / aventure")
    with result_cols[2]:
        render_metric_card("Score décisionnel", "4,54 / 5", "action-aventure AAA")
    with result_cols[3]:
        render_metric_card("Scénario central", "3,0 M", "unités - 210 M€ de revenu consommateur")

    st.markdown("#### Recommandation opérationnelle")
    st.info(
        "Lancer une phase de prototype court puis un vertical slice avant tout engagement lourd ; "
        "viser une aventure narrative semi-ouverte, destinée en priorité au PC, à PlayStation et à Xbox, "
        "avec un modèle premium digital et un périmètre de production strictement maîtrisé."
    )

    st.markdown("#### Livrables consultables")
    st.caption(
        "La présentation restitue la décision business ; le notebook et son PDF de graphiques "
        "documentent les analyses ; le PBIX permet de prolonger l’exploration ; l’archive rassemble "
        "les données pédagogiques, le questionnaire, les tables analytiques et les sources du PBIX."
    )

    presentation_pdf_path = P10_ASSET_DIR / "P10_UOI_Games_presentation.pdf"
    presentation_pptx_path = P10_ASSET_DIR / "P10_UOI_Games_presentation.pptx"
    notebook_path = P10_ASSET_DIR / "P10_UOI_Games_notebook.ipynb"
    all_visuals_path = P10_ASSET_DIR / "P10_UOI_Games_tous_les_visuels_notebook.pdf"
    selected_visuals_path = P10_ASSET_DIR / "P10_UOI_Games_visuels_selectionnes.pdf"
    pbix_path = P10_ASSET_DIR / "P10_UOI_Games_dashboard.pbix"
    dashboard_pdf_path = P10_ASSET_DIR / "P10_UOI_Games_dashboard_Power_BI.pdf"
    power_bi_sources_path = P10_ASSET_DIR / "P10_UOI_Games_sources_Power_BI.zip"
    sources_path = P10_ASSET_DIR / "P10_UOI_Games_sources_et_donnees.zip"

    first_row = st.columns(2)
    with first_row[0]:
        if presentation_pdf_path.exists():
            st.download_button(
                "📄 Télécharger la présentation en PDF",
                data=lambda file_path=presentation_pdf_path: file_path.read_bytes(),
                file_name="P10_UOI_Games_presentation.pdf",
                mime="application/pdf",
                key="download_p10_pdf",
                width="stretch",
            )
    with first_row[1]:
        if presentation_pptx_path.exists():
            st.download_button(
                "📽️ Télécharger la présentation en PowerPoint",
                data=lambda file_path=presentation_pptx_path: file_path.read_bytes(),
                file_name="P10_UOI_Games_presentation.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                key="download_p10_pptx",
                width="stretch",
            )

    second_row = st.columns(2)
    with second_row[0]:
        if notebook_path.exists():
            st.download_button(
                "📓 Télécharger le notebook P10",
                data=lambda file_path=notebook_path: file_path.read_bytes(),
                file_name="P10_UOI_Games_notebook.ipynb",
                mime="application/x-ipynb+json",
                key="download_p10_notebook",
                width="stretch",
            )
    with second_row[1]:
        if all_visuals_path.exists():
            st.download_button(
                "📊 Télécharger tous les visuels du notebook",
                data=lambda file_path=all_visuals_path: file_path.read_bytes(),
                file_name="P10_UOI_Games_tous_les_visuels_notebook.pdf",
                mime="application/pdf",
                key="download_p10_all_visuals",
                width="stretch",
            )

    third_row = st.columns(2)
    with third_row[0]:
        if selected_visuals_path.exists():
            st.download_button(
                "🖼️ Télécharger les visuels sélectionnés",
                data=lambda file_path=selected_visuals_path: file_path.read_bytes(),
                file_name="P10_UOI_Games_visuels_selectionnes.pdf",
                mime="application/pdf",
                key="download_p10_selected_visuals",
                width="stretch",
            )
    with third_row[1]:
        if pbix_path.exists():
            st.download_button(
                "📊 Télécharger le fichier Power BI",
                data=lambda file_path=pbix_path: file_path.read_bytes(),
                file_name="P10_UOI_Games_dashboard.pbix",
                mime="application/octet-stream",
                key="download_p10_pbix",
                width="stretch",
            )

    fourth_row = st.columns(2)
    with fourth_row[0]:
        if dashboard_pdf_path.exists():
            st.download_button(
                "📄 Télécharger le tableau de bord Power BI en PDF",
                data=lambda file_path=dashboard_pdf_path: file_path.read_bytes(),
                file_name="P10_UOI_Games_dashboard_Power_BI.pdf",
                mime="application/pdf",
                key="download_p10_dashboard_pdf",
                width="stretch",
            )
    with fourth_row[1]:
        if power_bi_sources_path.exists():
            st.download_button(
                "🧩 Télécharger les fichiers d'entrée du PBIX",
                data=lambda file_path=power_bi_sources_path: file_path.read_bytes(),
                file_name="P10_UOI_Games_sources_Power_BI.zip",
                mime="application/zip",
                key="download_p10_power_bi_sources",
                width="stretch",
            )

    if sources_path.exists():
        st.download_button(
            "🗂️ Télécharger l'ensemble des données, questionnaires et tables analytiques",
            data=lambda file_path=sources_path: file_path.read_bytes(),
            file_name="P10_UOI_Games_sources_et_donnees.zip",
            mime="application/zip",
            key="download_p10_sources",
            width="stretch",
        )


st.set_page_config(page_title="Projets OpenClassrooms", page_icon="📚", layout="wide")
inject_css()
df = load_projects()
oc = df[df["projet_id"] != "JUD"].copy()

render_page_header(
    "Projets OpenClassrooms",
    "Dix missions couvrant la chaîne complète : cadrage, SQL, Python, qualité des données, Power BI, machine learning et stratégie.",
    eyebrow="Parcours Business Intelligence Analyst",
    icon="📚",
    palette="blue",
)

st.caption(
    "Version web allégée : les preuves visuelles et principaux documents restent accessibles. "
    "Les bases, PBIX, PowerPoint et archives techniques lourdes sont conservés dans la version complète."
)

metrics = st.columns(3)
with metrics[0]:
    render_metric_card("Projets", str(len(oc)), "De P1 à P10")
with metrics[1]:
    render_metric_card("Projets phares", str((oc["mise_en_avant"] == "Phare").sum()), "Python, Power BI, ML, stratégie")
with metrics[2]:
    render_metric_card("Logique", "De bout en bout", "Besoin → données → décision")

render_section_heading(
    "Explorer les projets",
    "Filtrez la liste, puis sélectionnez une seule fiche détaillée. "
    "Cette présentation limite le chargement aux livrables du projet effectivement consulté.",
)

filter_col1, filter_col2 = st.columns([1, 2])
with filter_col1:
    categories = ["Toutes"] + sorted(oc["categorie"].dropna().unique().tolist())
    category = st.selectbox("Catégorie", categories)
with filter_col2:
    keyword = st.text_input(
        "Recherche",
        placeholder="Ex. Python, SQL, Power BI, RGPD…",
    )

filtered = oc.copy()
if category != "Toutes":
    filtered = filtered[filtered["categorie"] == category]

if keyword.strip():
    searched = keyword.lower().strip()
    mask = filtered.apply(
        lambda row: searched in " ".join(map(str, row.values)).lower(),
        axis=1,
    )
    filtered = filtered[mask]

st.caption(f"{len(filtered)} projet(s) correspondant aux critères")

if filtered.empty:
    st.warning(
        "Aucun projet ne correspond aux filtres. Modifiez la catégorie "
        "ou le terme de recherche."
    )
else:
    summary = filtered[
        [
            "projet_id",
            "titre_court",
            "categorie",
            "mise_en_avant",
        ]
    ].copy()
    summary.columns = [
        "Projet",
        "Titre",
        "Domaine",
        "Mise en avant",
    ]

    st.dataframe(
        summary,
        width="stretch",
        hide_index=True,
    )

    project_ids = filtered["projet_id"].tolist()
    project_labels = {
        row["projet_id"]: f'{row["projet_id"]} — {row["titre_portfolio"]}'
        for _, row in filtered.iterrows()
    }

    selected_project_id = st.selectbox(
        "Projet à consulter",
        options=project_ids,
        format_func=lambda project_id: project_labels[project_id],
    )

    row = filtered.loc[
        filtered["projet_id"] == selected_project_id
    ].iloc[0]

    st.divider()
    st.subheader(project_labels[selected_project_id])

    meta_col1, meta_col2 = st.columns([2, 1])
    with meta_col1:
        render_badges(split_badges(row["competences"]), limit=8)
    with meta_col2:
        st.caption(
            f"Catégorie : {row['categorie']} · "
            f"Mise en avant : {row['mise_en_avant']}"
        )

    st.markdown("#### Contexte & problématique")
    st.write(safe_text(row["contexte"]))
    st.info(safe_text(row["problematique"]))

    detail_col1, detail_col2 = st.columns(2)
    with detail_col1:
        st.markdown("#### Données utilisées")
        st.write(safe_text(row["donnees"]))
        st.markdown("#### Outils")
        st.write(safe_text(row["outils"]))
    with detail_col2:
        st.markdown("#### Méthode")
        st.write(safe_text(row["methode"]))
        st.markdown("#### Résultats")
        st.success(safe_text(row["resultats"]))

    st.markdown("#### Livrables & preuves")
    st.write(safe_text(row["livrables"]))
    st.caption(safe_text(row["visuels"]))

    if row["projet_id"] == "P1":
        render_p1_evidence()
    elif row["projet_id"] == "P2":
        render_p2_evidence()
    elif row["projet_id"] == "P3":
        render_p3_evidence()
    elif row["projet_id"] == "P4":
        render_p4_evidence()
    elif row["projet_id"] == "P5":
        render_p5_evidence()
    elif row["projet_id"] == "P6":
        render_p6_evidence()
    elif row["projet_id"] == "P7":
        render_p7_evidence()
    elif row["projet_id"] == "P8":
        render_p8_evidence()
    elif row["projet_id"] == "P9":
        render_p9_evidence()
    elif row["projet_id"] == "P10":
        render_p10_evidence()
