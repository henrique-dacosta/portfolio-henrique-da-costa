from __future__ import annotations

import base64
import html
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "projets_portfolio.csv"
CV_PATH = ROOT / "assets" / "cv" / "CV_EC.pdf"
PROFILE_PHOTO_PATH = ROOT / "assets" / "profile" / "henrique_da_costa.jpg"

PALETTES = {
    "blue": ("#0f172a", "#1e3a8a", "#075985"),
    "indigo": ("#111827", "#4338ca", "#6d28d9"),
    "teal": ("#0f172a", "#0f766e", "#0891b2"),
    "amber": ("#1f2937", "#92400e", "#d97706"),
    "slate": ("#0f172a", "#334155", "#475569"),
}

PROJECT_ACCENTS = {
    "P1": ("#64748b", "#94a3b8"),
    "P2": ("#0369a1", "#38bdf8"),
    "P3": ("#0f766e", "#2dd4bf"),
    "P4": ("#7c3aed", "#c084fc"),
    "P5": ("#be123c", "#fb7185"),
    "P6": ("#047857", "#22c55e"),
    "P7": ("#4f46e5", "#60a5fa"),
    "P8": ("#b45309", "#f59e0b"),
    "P9": ("#1d4ed8", "#9333ea"),
    "P10": ("#2563eb", "#0891b2"),
    "JUD": ("#0f172a", "#2563eb"),
}


@st.cache_data
def load_projects() -> pd.DataFrame:
    """Charge la matrice projets en sécurisant les valeurs manquantes."""
    df = pd.read_csv(DATA_PATH, sep=";", encoding="utf-8-sig")
    return df.fillna("")


def safe_text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def split_badges(value: object) -> list[str]:
    text = safe_text(value)
    if not text:
        return []
    for separator in ("·", ";", ","):
        if separator in text:
            return [item.strip() for item in text.split(separator) if item.strip()]
    return [text]


def badges_html(labels: Iterable[object], limit: int | None = None) -> str:
    cleaned = [safe_text(label) for label in labels if safe_text(label)]
    if limit is not None:
        cleaned = cleaned[:limit]
    return " ".join(
        f'<span class="badge">{html.escape(label)}</span>' for label in cleaned
    )


def render_badges(labels: Iterable[object], limit: int | None = None) -> None:
    st.markdown(badges_html(labels, limit), unsafe_allow_html=True)


def inject_css() -> None:
    """Injecte la charte graphique commune à toutes les pages."""
    if PROFILE_PHOTO_PATH.exists():
        encoded_photo = base64.b64encode(
            PROFILE_PHOTO_PATH.read_bytes()
        ).decode("ascii")

        st.markdown(
            f"""
            <style>
            [data-testid="stSidebarNav"]::before {{
                content: "";
                display: block !important;
                width: 180px !important;
                min-width: 180px !important;
                max-width: 180px !important;
                height: 180px !important;
                min-height: 180px !important;
                max-height: 180px !important;
                aspect-ratio: 1 / 1;
                flex: 0 0 180px !important;
                margin: 0.35rem auto 1.1rem auto !important;
                border-radius: 50%;
                background-image: url("data:image/jpeg;base64,{encoded_photo}");
                background-size: 128% auto;
                background-position: center 34%;
                background-repeat: no-repeat;
                border: 5px solid rgba(255, 255, 255, 0.98);
                box-shadow:
                    0 8px 22px rgba(15, 23, 42, 0.16),
                    0 0 0 1px rgba(148, 163, 184, 0.32);
                box-sizing: border-box;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <style>
        .block-container {
            max-width: 1700px;
            padding-top: 2rem;
            padding-bottom: 3.5rem;
        }

        :root {
            --hdc-navy: #0f172a;
            --hdc-blue: #2563eb;
            --hdc-indigo: #4f46e5;
            --hdc-cyan: #0891b2;
            --hdc-teal: #0f766e;
            --hdc-gold: #b45309;
            --hdc-muted: #64748b;
            --hdc-border: #e2e8f0;
            --hdc-soft: #f8fafc;
            --hdc-white: #ffffff;
        }

        [data-testid="stSidebar"] {
            border-right: 1px solid #e2e8f0;
            background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
        }

        [data-testid="stSidebarNav"] a {
            border-radius: 9px;
            margin: 2px 8px;
        }

        .page-hero {
            position: relative;
            padding: 30px 36px;
            border-radius: 22px;
            color: white;
            box-shadow: 0 16px 36px rgba(15, 23, 42, 0.16);
            margin-bottom: 26px;
            overflow: hidden;
            background:
                radial-gradient(circle at top right, rgba(255,255,255,0.14), transparent 31%),
                linear-gradient(135deg, var(--hero1), var(--hero2) 52%, var(--hero3));
        }

        .page-hero::after {
            content: "";
            position: absolute;
            right: -55px;
            top: -65px;
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: rgba(255,255,255,0.08);
        }

        .hero-eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 11px;
            border-radius: 999px;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.18);
            color: #eff6ff;
            font-size: 0.86rem;
            margin-bottom: 0.9rem;
        }

        .hero-title {
            font-size: 2.05rem;
            font-weight: 820;
            letter-spacing: -0.035em;
            line-height: 1.15;
            margin: 0 0 0.45rem 0;
        }

        .hero-subtitle {
            max-width: 1120px;
            color: #e0f2fe;
            font-size: 1rem;
            line-height: 1.65;
            margin: 0;
        }

        .section-heading {
            margin: 1.45rem 0 0.3rem 0;
            font-size: 1.52rem;
            font-weight: 810;
            color: var(--hdc-navy);
            letter-spacing: -0.025em;
        }

        .section-caption {
            color: var(--hdc-muted);
            line-height: 1.55;
            margin-bottom: 1rem;
        }

        .metric-card,
        .feature-card,
        .skill-card,
        .contact-card,
        .timeline-card,
        .proof-card,
        .project-card {
            border: 1px solid var(--hdc-border);
            background: #ffffff;
            box-shadow: 0 7px 21px rgba(15, 23, 42, 0.055);
        }

        .metric-card {
            border-radius: 16px;
            padding: 18px 20px;
            min-height: 112px;
            background: linear-gradient(180deg, #ffffff, #f8fafc);
        }

        .metric-label {
            color: var(--hdc-muted);
            font-size: 0.84rem;
            margin-bottom: 6px;
        }

        .metric-value {
            color: var(--hdc-navy);
            font-size: 1.85rem;
            font-weight: 790;
            line-height: 1.1;
        }

        .metric-note {
            color: #475569;
            font-size: 0.84rem;
            margin-top: 6px;
        }

        .feature-card,
        .skill-card,
        .contact-card {
            border-radius: 17px;
            padding: 20px 22px;
            min-height: 154px;
            transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
        }

        .feature-card:hover,
        .skill-card:hover,
        .project-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 31px rgba(15, 23, 42, 0.09);
            border-color: rgba(37, 99, 235, 0.28);
        }

        .card-icon {
            width: 39px;
            height: 39px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
            background: #eff6ff;
            margin-bottom: 10px;
            font-size: 1.1rem;
        }

        .card-title {
            margin: 0 0 0.45rem 0;
            font-size: 1.05rem;
            font-weight: 790;
            color: var(--hdc-navy);
        }

        .card-text {
            margin: 0;
            color: #334155;
            line-height: 1.58;
        }

        .skill-proof {
            color: #475569;
            font-size: 0.86rem;
            margin-top: 0.7rem;
            padding-top: 0.65rem;
            border-top: 1px solid #eef2f7;
        }

        .timeline-card {
            position: relative;
            border-radius: 15px;
            padding: 18px 20px 18px 24px;
            margin-bottom: 14px;
            border-left: 5px solid var(--timeline-accent);
        }

        .timeline-period {
            color: var(--timeline-accent);
            font-weight: 780;
            font-size: 0.9rem;
            margin-bottom: 4px;
        }

        .timeline-title {
            color: var(--hdc-navy);
            font-weight: 780;
            margin-bottom: 5px;
        }

        .timeline-text {
            color: #334155;
            line-height: 1.55;
        }

        .project-card {
            position: relative;
            border-radius: 17px;
            padding: 20px 22px 18px 22px;
            margin-bottom: 20px;
            min-height: 186px;
            overflow: hidden;
            transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
        }

        .project-card::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 5px;
            background: linear-gradient(180deg, var(--accent1), var(--accent2));
        }

        .project-title {
            font-weight: 800;
            font-size: 1.02rem;
            margin-bottom: 0.28rem;
            color: var(--hdc-navy);
            padding-left: 4px;
        }

        .project-category {
            display: inline-block;
            color: #334155;
            font-size: 0.8rem;
            margin: 0 0 0.72rem 4px;
            padding: 4px 9px;
            border-radius: 999px;
            background: #f1f5f9;
            border: 1px solid #e2e8f0;
        }

        .project-description {
            color: #1f2937;
            line-height: 1.55;
            margin: 0 0 0.9rem 4px;
        }

        .badge {
            display: inline-block;
            padding: 4px 9px;
            margin: 3px 5px 3px 0;
            border-radius: 999px;
            background: #f8fafc;
            border: 1px solid #dbe3ec;
            font-size: 0.77rem;
            color: #334155;
            white-space: nowrap;
        }

        .proof-card {
            border-left: 5px solid var(--proof-accent, #2563eb);
            border-radius: 14px;
            padding: 17px 20px;
            color: #1f2937;
            line-height: 1.65;
            margin: 0.7rem 0 1rem 0;
            background: linear-gradient(90deg, #f8fafc, #ffffff);
        }

        .contact-card {
            min-height: 0;
            background: linear-gradient(145deg, #ffffff, #f8fafc);
        }

        .contact-line {
            margin: 0.45rem 0;
            color: #334155;
        }

        .contact-line strong {
            color: var(--hdc-navy);
        }

        div[data-testid="stExpander"] {
            border: 1px solid #e2e8f0;
            border-radius: 15px;
            background: #ffffff;
            box-shadow: 0 5px 16px rgba(15, 23, 42, 0.04);
            margin-bottom: 0.8rem;
            overflow: hidden;
        }

        div[data-testid="stExpander"] summary {
            font-weight: 700;
            color: #0f172a;
        }

        .stDownloadButton button,
        .stButton button {
            border-radius: 999px;
            border: 1px solid rgba(37, 99, 235, 0.35);
            background: #eff6ff;
            color: #1e3a8a;
            font-weight: 670;
        }

        .stDownloadButton button:hover,
        .stButton button:hover {
            border-color: #2563eb;
            color: #1d4ed8;
        }

        div[data-baseweb="select"] > div,
        .stTextInput input {
            border-radius: 12px;
        }

        [data-testid="stDataFrame"] {
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            overflow: hidden;
        }

        @media (max-width: 900px) {
            .block-container { padding-top: 1.2rem; }
            .page-hero { padding: 24px 22px; }
            .hero-title { font-size: 1.65rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_page_header(
    title: str,
    subtitle: str,
    *,
    eyebrow: str = "Portfolio Data / BI",
    icon: str = "📊",
    palette: str = "blue",
) -> None:
    colors = PALETTES.get(palette, PALETTES["blue"])
    st.markdown(
        f"""
        <div class="page-hero" style="--hero1:{colors[0]};--hero2:{colors[1]};--hero3:{colors[2]};">
            <div class="hero-eyebrow">{html.escape(icon)} {html.escape(eyebrow)}</div>
            <div class="hero-title">{html.escape(title)}</div>
            <p class="hero-subtitle">{html.escape(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_heading(title: str, caption: str = "") -> None:
    st.markdown(
        f'<div class="section-heading">{html.escape(title)}</div>',
        unsafe_allow_html=True,
    )
    if caption:
        st.markdown(
            f'<div class="section-caption">{html.escape(caption)}</div>',
            unsafe_allow_html=True,
        )


def render_metric_card(label: str, value: str, note: str = "") -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{html.escape(label)}</div>
            <div class="metric-value">{html.escape(value)}</div>
            <div class="metric-note">{html.escape(note)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_feature_card(icon: str, title: str, text: str) -> None:
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="card-icon">{html.escape(icon)}</div>
            <div class="card-title">{html.escape(title)}</div>
            <p class="card-text">{html.escape(text)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_skill_card(
    icon: str,
    title: str,
    text: str,
    proof: str,
    badges: Sequence[str] | None = None,
) -> None:
    badges_block = badges_html(badges or [], limit=7)
    st.markdown(
        f"""
        <div class="skill-card">
            <div class="card-icon">{html.escape(icon)}</div>
            <div class="card-title">{html.escape(title)}</div>
            <p class="card-text">{html.escape(text)}</p>
            <div style="margin-top:.65rem;">{badges_block}</div>
            <div class="skill-proof"><strong>Projets-preuves :</strong> {html.escape(proof)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_timeline_card(period: str, title: str, text: str, accent: str = "#2563eb") -> None:
    st.markdown(
        f"""
        <div class="timeline-card" style="--timeline-accent:{accent};">
            <div class="timeline-period">{html.escape(period)}</div>
            <div class="timeline-title">{html.escape(title)}</div>
            <div class="timeline-text">{html.escape(text)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_project_card(row: Mapping[str, object], badge_limit: int = 6) -> None:
    project_id = safe_text(row.get("projet_id"))
    title = safe_text(row.get("titre_portfolio"))
    category = safe_text(row.get("categorie"))
    if project_id == "JUD":
        category = "Application métier / API"
    description = safe_text(row.get("problematique"))
    accents = PROJECT_ACCENTS.get(project_id, ("#2563eb", "#0891b2"))
    badges = badges_html(split_badges(row.get("competences")), badge_limit)
    st.markdown(
        f"""
        <div class="project-card" style="--accent1:{accents[0]};--accent2:{accents[1]};">
            <div class="project-title">{html.escape(project_id)} — {html.escape(title)}</div>
            <div class="project-category">{html.escape(category)}</div>
            <div class="project-description">{html.escape(description)}</div>
            <div style="padding-left:4px;">{badges}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_callout(text: str, accent: str = "#2563eb") -> None:
    st.markdown(
        f'<div class="proof-card" style="--proof-accent:{accent};">{html.escape(text)}</div>',
        unsafe_allow_html=True,
    )


def render_contact_card(lines: Sequence[tuple[str, str]]) -> None:
    body = "".join(
        f'<div class="contact-line"><strong>{html.escape(label)} :</strong> {html.escape(value)}</div>'
        for label, value in lines
    )
    st.markdown(f'<div class="contact-card">{body}</div>', unsafe_allow_html=True)


def cv_download_button(label: str = "📄 Télécharger le CV") -> None:
    if CV_PATH.exists():
        st.download_button(
            label,
            data=lambda file_path=CV_PATH: file_path.read_bytes(),
            file_name="CV_Henrique_DaCosta.pdf",
            mime="application/pdf",
        )
    else:
        st.info("CV non disponible dans le dossier assets/cv pour le moment.")
