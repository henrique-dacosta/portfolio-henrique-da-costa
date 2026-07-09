from pathlib import Path
import re

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
P11_DIR = ROOT / "assets" / "projets" / "P11"

from utils import (
    inject_css,
    render_callout,
    render_feature_card,
    render_metric_card,
    render_page_header,
    render_section_heading,
)

st.set_page_config(page_title="Gestion du projet P11", page_icon="🧭", layout="wide")
inject_css()


def file_key(path: Path, prefix: str = "download") -> str:
    raw = str(path.relative_to(P11_DIR)) if path.is_relative_to(P11_DIR) else str(path)
    return prefix + "_" + re.sub(r"[^A-Za-z0-9_]+", "_", raw)


def mime_for(path: Path) -> str:
    suffix = path.suffix.lower()
    return {
        ".pdf": "application/pdf",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ".png": "image/png",
        ".pbix": "application/octet-stream",
        ".zip": "application/zip",
        ".mp4": "video/mp4",
    }.get(suffix, "application/octet-stream")


def download_button(path: Path, label: str, *, key_suffix: str = "") -> None:
    if path.exists():
        st.download_button(
            label,
            data=lambda fp=path: fp.read_bytes(),
            file_name=path.name,
            mime=mime_for(path),
            key=file_key(path, key_suffix or "download"),
            width="stretch",
        )
    else:
        st.warning(f"Fichier manquant : {path.name}")


def render_downloads(files: list[tuple[Path, str]], cols: int = 2) -> None:
    columns = st.columns(cols)
    for i, (path, label) in enumerate(files):
        with columns[i % cols]:
            download_button(path, label, key_suffix=f"download_{i}")


def render_livrable_card(icon: str, title: str, text: str, proof: str, files: list[tuple[Path, str]]) -> None:
    render_feature_card(icon, title, text)
    st.caption(proof)
    render_downloads(files, cols=2)


render_page_header(
    "Gestion du projet P11",
    "Suivre et valoriser la démarche complète de conception du portfolio : cadrage, planification, maquettage, dashboards, documentation, formation utilisateur et préparation de la soutenance.",
    eyebrow="Cadrage · Mock-ups · Power BI · Documentation · Formation · Soutenance",
    icon="🧭",
    palette="teal",
)

render_callout(
    "Cette page regroupe les livrables produits pour répondre au besoin d’Aéroworld. Elle montre la démarche projet complète, depuis l’analyse du besoin jusqu’aux preuves de conception, aux tableaux de bord Power BI, aux documentations et à la vidéo de formation guidant l’utilisateur dans la prise en main du portfolio.",
    accent="#0f766e",
)

metrics = st.columns(4)
with metrics[0]:
    render_metric_card("Cadrage & pilotage", "4", "Analyse, cahier des charges, Gantt, carte mentale")
with metrics[1]:
    render_metric_card("Mock-ups validés", "3", "Portfolio, dashboard veille, dashboard profil")
with metrics[2]:
    render_metric_card("Dashboards Power BI", "2", "Veille Data / BI et présentation du profil")
with metrics[3]:
    render_metric_card("Documentation & formation", "3", "2 documentations + 1 vidéo guidée")

bundle_path = P11_DIR / "P11_Livrables_complets_Henrique_Da_Costa.zip"
if bundle_path.exists():
    st.download_button(
        "📦 Télécharger le lot complet des livrables P11",
        data=lambda file_path=bundle_path: file_path.read_bytes(),
        file_name=bundle_path.name,
        mime="application/zip",
        key="download_p11_bundle_complet",
        width="stretch",
    )

# -----------------------------------------------------------------------------
# 1. Cadrage et pilotage
# -----------------------------------------------------------------------------
render_section_heading(
    "1. Cadrage et pilotage du projet",
    "Ces livrables démontrent la capacité à comprendre le besoin, formaliser la solution, planifier la mission et structurer la vision globale du portfolio.",
)

cadrage_items = [
    (
        "🔎",
        "Analyse du besoin métier client",
        "Identifier les attentes d’Aéroworld, les parties prenantes, les contraintes, les besoins fonctionnels et non fonctionnels.",
        "Compétence démontrée : analyse du besoin et reformulation d’une problématique métier.",
        [
            (P11_DIR / "01_analyse_besoin" / "P11_Analyse_du_besoin_Henrique_Da_Costa.pdf", "📄 PDF"),
            (P11_DIR / "01_analyse_besoin" / "P11_Analyse_du_besoin_Henrique_Da_Costa.docx", "📝 Word"),
        ],
    ),
    (
        "📘",
        "Cahier des charges fonctionnel",
        "Traduire le besoin en périmètre, exigences, livrables, user stories, critères d’acceptation et règles de recette.",
        "Compétence démontrée : cadrage fonctionnel et formalisation d’une solution exploitable.",
        [
            (P11_DIR / "02_cahier_charges" / "P11_Cahier_des_charges_fonctionnel_Henrique_Da_Costa.pdf", "📄 PDF"),
            (P11_DIR / "02_cahier_charges" / "P11_Cahier_des_charges_fonctionnel_Henrique_Da_Costa.docx", "📝 Word"),
        ],
    ),
    (
        "📅",
        "Diagramme de Gantt",
        "Planifier la mission du 20 juin au 20 juillet 2026, avec validations mentor et soutenance avant le 31 juillet.",
        "Compétence démontrée : organisation du projet, jalons, dépendances et sécurisation du calendrier.",
        [
            (P11_DIR / "03_gantt" / "P11_Diagramme_de_Gantt_20juin_20juillet_2026.pdf", "📄 PDF"),
            (P11_DIR / "03_gantt" / "P11_Diagramme_de_Gantt_20juin_20juillet_2026.pptx", "🧩 PowerPoint"),
            (P11_DIR / "03_gantt" / "P11_Diagramme_de_Gantt_20juin_20juillet_2026_Henrique_Da_Costa.xlsx", "📊 Excel"),
            (P11_DIR / "03_gantt" / "P11_Diagramme_de_Gantt_20juin_20juillet_2026-1.png", "🖼️ PNG"),
        ],
    ),
    (
        "🧠",
        "Carte mentale du portfolio",
        "Structurer la vision globale : contexte, profil, projets, preuves, gestion de projet, mock-ups, dashboards, documentation et soutenance.",
        "Compétence démontrée : vision d’ensemble, structuration des contenus et articulation des preuves.",
        [
            (P11_DIR / "04_carte_mentale" / "P11_Carte_mentale_Henrique_Da_Costa.pdf", "📄 PDF"),
            (P11_DIR / "04_carte_mentale" / "P11_Carte_mentale_Henrique_Da_Costa.pptx", "🧩 PowerPoint"),
            (P11_DIR / "04_carte_mentale" / "P11_Carte_mentale_Henrique_Da_Costa.png", "🖼️ PNG"),
        ],
    ),
]

for start in range(0, len(cadrage_items), 2):
    cols = st.columns(2)
    for col, item in zip(cols, cadrage_items[start:start + 2]):
        with col:
            render_livrable_card(*item)

# -----------------------------------------------------------------------------
# 2. Conception : mock-ups
# -----------------------------------------------------------------------------
render_section_heading(
    "2. Conception fonctionnelle : mock-ups",
    "Les trois mock-ups matérialisent les choix UX et la structure cible avant réalisation et intégration finale.",
)

mockups = [
    (
        "🖥️",
        "Mock-up du portfolio Streamlit",
        "Valider l’architecture générale, la navigation, la hiérarchie de lecture et l’accès aux preuves.",
        "Preuve : conception de l’interface cible du portfolio.",
        "P11_Mockup_1_Portfolio_Streamlit_Henrique_Da_Costa",
    ),
    (
        "📡",
        "Mock-up du dashboard de veille",
        "Préparer un tableau de bord de veille métier et technologique orienté sources, thématiques, impact, maturité et recommandations.",
        "Preuve : conception d’un outil de veille utile à la décision.",
        "P11_Mockup_2_Dashboard_Veille_Henrique_Da_Costa",
    ),
    (
        "👤",
        "Mock-up du dashboard profil",
        "Synthétiser le parcours, les compétences, les projets phares et le positionnement Data / BI.",
        "Preuve : conception d’un tableau de bord de présentation du profil.",
        "P11_Mockup_3_Dashboard_Profil_Henrique_Da_Costa",
    ),
]

mockup_cols = st.columns(3)
for col, (icon, title, text, proof, stem) in zip(mockup_cols, mockups):
    with col:
        render_feature_card(icon, title, text)
        st.caption(proof)
        preview = P11_DIR / "05_mockups" / f"{stem}.png"
        if preview.exists():
            st.image(str(preview), caption=title, width="stretch")
        render_downloads(
            [
                (P11_DIR / "05_mockups" / f"{stem}.pdf", "📄 PDF"),
                (P11_DIR / "05_mockups" / f"{stem}.pptx", "🧩 PowerPoint"),
                (P11_DIR / "05_mockups" / f"{stem}.png", "🖼️ PNG"),
            ],
            cols=1,
        )

# -----------------------------------------------------------------------------
# 3. Réalisation : dashboards Power BI
# -----------------------------------------------------------------------------
render_section_heading(
    "3. Tableaux de bord Power BI",
    "Les dashboards transforment les mock-ups en preuves concrètes : un tableau de bord de veille et un tableau de bord de présentation du profil.",
)

dashboard_items = [
    (
        "📡",
        "Dashboard de veille Data / BI",
        "Structurer la veille autour des sources, thématiques, signaux, impact, maturité et recommandations actionnables.",
        "Compétence démontrée : veille métier et technologique, priorisation et restitution.",
        P11_DIR / "06_dashboard_veille",
        "P11_Dashboard_Veille_DataBI_Henrique_Da_Costa",
        "P11_Source_Dashboard_Veille_DataBI_Henrique_Da_Costa.xlsx",
    ),
    (
        "👤",
        "Dashboard de présentation du profil",
        "Présenter l’expérience, les compétences clés, la chronologie, les projets P6 à P9 et le positionnement Data / BI.",
        "Compétence démontrée : synthèse visuelle, storytelling professionnel et preuve par les réalisations.",
        P11_DIR / "07_dashboard_profil",
        "P11_Dashboard_Profil_Henrique_Da_Costa",
        "P11_Source_Dashboard_Profil_Henrique_Da_Costa.xlsx",
    ),
]

cols = st.columns(2)
for col, (icon, title, text, proof, folder, stem, source_name) in zip(cols, dashboard_items):
    with col:
        render_feature_card(icon, title, text)
        st.caption(proof)
        preview = folder / f"{stem}.png"
        if preview.exists():
            st.image(str(preview), caption=title, width="stretch")
        render_downloads(
            [
                (folder / f"{stem}.pdf", "📄 PDF"),
                (folder / f"{stem}.pbix", "📊 Power BI PBIX"),
                (folder / f"{stem}.png", "🖼️ PNG"),
                (folder / source_name, "📁 Source Excel"),
            ],
            cols=2,
        )

# -----------------------------------------------------------------------------
# 4. Documentation
# -----------------------------------------------------------------------------
render_section_heading(
    "4. Documentation utilisateur et technique",
    "Les documentations sécurisent la prise en main, la maintenance et la reproductibilité de l’application Streamlit.",
)

doc_cols = st.columns(2)
with doc_cols[0]:
    render_livrable_card(
        "📖",
        "Documentation utilisateur",
        "Expliquer la finalité du portfolio, le parcours de consultation, les pages, les téléchargements et les bonnes pratiques d’utilisation.",
        "Compétence démontrée : accompagnement utilisateur et clarté de restitution.",
        [
            (P11_DIR / "08_documentation" / "P11_Documentation_utilisateur_Portfolio_Henrique_Da_Costa.pdf", "📄 PDF"),
            (P11_DIR / "08_documentation" / "P11_Documentation_utilisateur_Portfolio_Henrique_Da_Costa.docx", "📝 Word"),
        ],
    )
with doc_cols[1]:
    render_livrable_card(
        "🛠️",
        "Documentation technique",
        "Documenter l’architecture, l’installation, les dépendances, le contrôle qualité, la sécurité et le déploiement Streamlit Cloud.",
        "Compétence démontrée : documentation technique, maintenabilité et reproductibilité.",
        [
            (P11_DIR / "08_documentation" / "P11_Documentation_technique_Portfolio_Henrique_Da_Costa.pdf", "📄 PDF"),
            (P11_DIR / "08_documentation" / "P11_Documentation_technique_Portfolio_Henrique_Da_Costa.docx", "📝 Word"),
        ],
    )

# -----------------------------------------------------------------------------
# 5. Vidéo de formation
# -----------------------------------------------------------------------------
render_section_heading(
    "5. Vidéo de formation — parcours guidé du portfolio",
    "Une démonstration écran commentée accompagne l’utilisateur dans la découverte des pages, des projets, des preuves, des dashboards et des livrables P11.",
)

video_path = P11_DIR / "09_video_formation" / "P11_Video_formation_Portfolio_Henrique_Da_Costa.mp4"

render_feature_card(
    "🎬",
    "Prendre en main le portfolio en 13 minutes",
    "Cette vidéo suit un parcours utilisateur complet : accueil, profil, compétences, projets OpenClassrooms, Judilibre Explorer, livrables, gestion du projet P11 et objectifs professionnels.",
)
st.caption(
    "Compétence démontrée : accompagnement utilisateur, pédagogie, démonstration d’une solution et accès guidé aux preuves."
)

if video_path.exists():
    st.video(str(video_path), format="video/mp4")
    download_button(video_path, "🎥 Télécharger la vidéo de formation", key_suffix="download_video_formation")
else:
    st.warning("La vidéo de formation n’est pas disponible dans cette distribution.")

# -----------------------------------------------------------------------------
# 6. Aperçus synthétiques
# -----------------------------------------------------------------------------
render_section_heading("Aperçus synthétiques", "Ces visuels permettent de contrôler rapidement les productions sans ouvrir les fichiers sources.")

tabs = st.tabs(["Carte mentale & Gantt", "Mock-ups", "Dashboards"])
with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Carte mentale")
        mental_png = P11_DIR / "04_carte_mentale" / "P11_Carte_mentale_Henrique_Da_Costa.png"
        if mental_png.exists():
            st.image(str(mental_png), caption="Vision globale du projet portfolio P11", width="stretch")
    with c2:
        st.markdown("#### Planning de référence")
        gantt_png = P11_DIR / "03_gantt" / "P11_Diagramme_de_Gantt_20juin_20juillet_2026-1.png"
        if gantt_png.exists():
            st.image(str(gantt_png), caption="Mission planifiée du 20 juin au 20 juillet 2026", width="stretch")
with tabs[1]:
    cols = st.columns(3)
    for col, (_, title, _, _, stem) in zip(cols, mockups):
        with col:
            img = P11_DIR / "05_mockups" / f"{stem}.png"
            st.markdown(f"#### {title}")
            if img.exists():
                st.image(str(img), width="stretch")
with tabs[2]:
    cols = st.columns(2)
    for col, (_, title, _, _, folder, stem, _) in zip(cols, dashboard_items):
        with col:
            img = folder / f"{stem}.png"
            st.markdown(f"#### {title}")
            if img.exists():
                st.image(str(img), width="stretch")

# -----------------------------------------------------------------------------
# 6. Correspondance compétences OC
# -----------------------------------------------------------------------------
render_section_heading(
    "Correspondance avec les compétences OpenClassrooms",
    "Les livrables servent de preuves concrètes pour les compétences de cadrage, de conception, de réalisation, de restitution et de documentation.",
)
competences = pd.DataFrame(
    [
        ["Analyser un besoin métier", "Analyse du besoin", "Parties prenantes, contraintes, besoins explicites et implicites"],
        ["Formaliser une solution", "Cahier des charges", "Périmètre, exigences, user stories et critères de recette"],
        ["Organiser un projet Data", "Diagramme de Gantt", "Tâches, dépendances, jalons et calendrier de soutenance"],
        ["Structurer une vision produit", "Carte mentale et mock-ups", "Architecture des contenus, parcours utilisateur et preuves attendues"],
        ["Réaliser une restitution décisionnelle", "Dashboards Power BI", "Veille exploitable, profil synthétique, KPI et recommandations"],
        ["Documenter et accompagner", "Documentation utilisateur et technique", "Prise en main, maintenance, déploiement et reproductibilité"],
        ["Former et accompagner un utilisateur", "Vidéo de formation", "Parcours guidé, démonstration écran, pédagogie et prise en main de la solution"],
        ["Adopter une posture de consultant", "Ensemble des livrables", "Reformulation, arbitrages, recommandations et clarté de restitution"],
    ],
    columns=["Compétence", "Preuve principale", "Ce qui est démontré"],
)
st.dataframe(competences, width="stretch", hide_index=True)
