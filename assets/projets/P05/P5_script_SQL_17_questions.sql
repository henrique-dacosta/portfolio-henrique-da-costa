============================================
-- CONTROLES STRUCTURELS DE LA BASE
-- Volumétrie des tables
-- Présence des clés primaires
-- Présence des clés étrangères
-- =================================================
-- 1. Nombres d'enregistrements dans chaque table
-- -------------------------------------------------
-- Nombre de lignes par table
SELECT 'retour_client' AS table_name, COUNT(*) AS nb_lignes
FROM retour_client

UNION ALL
SELECT 'produit' AS table_name, COUNT(*) AS nb_lignes
FROM produit

UNION ALL
SELECT 'ref_magasin' AS table_name, COUNT(*) AS nb_lignes
FROM ref_magasin;

-- 2. Présence d'une clé primaire par table
-- ---------------------------------------------
-- Contrôle structurel => Interrogation de sqlite_master pour vérifier 
-- que chaque table a bien une clause PRIMARY KEY dans sa définition.
SELECT
    name AS table_name,
    CASE 
        WHEN instr(upper(sql), 'PRIMARY KEY') > 0 
            THEN 'OK - clé primaire déclarée'
        ELSE 'ATTENTION - aucune clé primaire trouvée'
    END AS statut_pk
FROM sqlite_master
WHERE type = 'table'
  AND name NOT LIKE 'sqlite_%'      -- on ignore les tables système SQLite
ORDER BY table_name;

-- 3. Présence de clés étrangères (contrôle structurel)
-- -----------------------------------------------------
SELECT
    name AS table_name,
    CASE 
        WHEN instr(upper(sql), 'REFERENCES ') > 0 
            THEN 'OK - au moins une clé étrangère déclarée'
        ELSE 'AUCUNE FK déclarée (table potentiellement "maîtresse")'
    END AS statut_fk
FROM sqlite_master
WHERE type = 'table'
  AND name NOT LIKE 'sqlite_%'
ORDER BY table_name;

-- Détail des clés étrangères sur retour_client
PRAGMA foreign_key_list('retour_client');


-- -----------------------------------
-- CONTRÖLES DE COHERENCE
-- -------------------------------

-- 1.Doublons sur la table retour_client ?
-- ---------------------------------------
--   => Doublons sur clé primaire
SELECT
    'retour_client' AS table_name,
    COUNT(*) AS nb_lignes,
    COUNT(DISTINCT cle_retour_client) AS nb_cles_distinctes,    
    CASE
        WHEN COUNT(*) = COUNT(DISTINCT cle_retour_client)
            THEN 'OK - aucune clé en doublon'
        ELSE 'ATTENTION - doublons présents'
    END AS controle_pk
FROM retour_client;

--  => Doublons sur tous les champs hors clé primaire
SELECT   COUNT(*) AS nbr_doublon, note, cle_produit, ref_magasin, date_achat, libelle_source, libelle_categorie, recommandation
FROM     retour_client
GROUP BY note, cle_produit, ref_magasin, date_achat, libelle_source, libelle_categorie, recommandation
HAVING   COUNT(*) > 1

-- 2.Doublons sur la table produit ?
-- ---------------------------------------
--   => Doublons sur clé primaire
SELECT
    'produit' AS table_name,
    COUNT(*) AS nb_lignes,
    COUNT(DISTINCT cle_produit) AS nb_cles_distinctes,
    CASE
        WHEN COUNT(*) = COUNT(DISTINCT cle_produit)
            THEN 'OK - aucune clé en doublon'
        ELSE 'ATTENTION - doublons présents'
    END AS controle_pk
FROM produit;

--   => Doublons sur tous les chams hors clés primaire
SELECT   COUNT(*) AS nbr_doublon, typologie_produit, titre_produit
FROM     produit
GROUP BY typologie_produit, titre_produit
HAVING   COUNT(*) > 1

-- 3.Doublons sur la table ref_magasin ?
-- ---------------------------------------
--    => Doublons sur clé primaire
SELECT
    'ref_magasin' AS table_name,
    COUNT(*) AS nb_lignes,
    COUNT(DISTINCT ref_magasin) AS nb_cles_distinctes,
    CASE
        WHEN COUNT(*) = COUNT(DISTINCT ref_magasin)
            THEN 'OK - aucune clé en doublon'
        ELSE 'ATTENTION - doublons présents'
    END AS controle_pk
FROM ref_magasin;

--   => Doublons sur tous les champs hors clé primaire
SELECT   COUNT(*) AS nbr_doublon, departement, departement_commune, libelle_de_commune, population, geo_point_2d
FROM     ref_magasin
GROUP BY departement, departement_commune, libelle_de_commune, population, geo_point_2d
HAVING   COUNT(*) > 1

-- 4.Valeurs nulles sur les champs critiques de la table retour_client ?
-- ------------------------------------------------------------------------
SELECT
    COUNT(*) AS nb_lignes,
    SUM(CASE WHEN note IS NULL THEN 1 ELSE 0 END) AS nb_note_null,
    SUM(CASE WHEN cle_produit IS NULL THEN 1 ELSE 0 END) AS nb_cle_produit_null,
    SUM(CASE WHEN ref_magasin IS NULL THEN 1 ELSE 0 END) AS nb_ref_magasin_null,
    SUM(CASE WHEN date_achat IS NULL THEN 1 ELSE 0 END) AS nb_date_achat_null,
    SUM(CASE WHEN libelle_categorie IS NULL THEN 1 ELSE 0 END) AS nb_categorie_null,
    SUM(CASE WHEN libelle_source IS NULL THEN 1 ELSE 0 END) AS nb_source_null,
    SUM(CASE WHEN recommandation IS NULL THEN 1 ELSE 0 END) AS nb_reco_null
FROM retour_client;

-- 5.Valeurs nulles sur les champs critiques de la table produit ?
-- ------------------------------------------------------------------------
SELECT
    COUNT(*) AS nb_lignes,
    SUM(CASE WHEN cle_produit IS NULL THEN 1 ELSE 0 END) AS nb_cle_produit_null,
    SUM(CASE WHEN typologie_produit IS NULL THEN 1 ELSE 0 END) AS nb_typologie_produit_null,
    SUM(CASE WHEN titre_produit IS NULL THEN 1 ELSE 0 END) AS nb_titre_produit_null
FROM produit;

-- 6.Valeurs nulles sur les champs critiques de la table ref_magasin ?
-- ------------------------------------------------------------------------
SELECT
    COUNT(*) AS nb_lignes,
    SUM(CASE WHEN ref_magasin IS NULL THEN 1 ELSE 0 END) AS nb_ref_magasin_null,
    SUM(CASE WHEN departement IS NULL THEN 1 ELSE 0 END) AS nb_departement_null,
    SUM(CASE WHEN departement_commune IS NULL THEN 1 ELSE 0 END) AS nb_departement_commune_null,
    SUM(CASE WHEN libelle_de_commune IS NULL THEN 1 ELSE 0 END) AS nb_libelle_de_commune_null,
    SUM(CASE WHEN population IS NULL THEN 1 ELSE 0 END) AS nb_population_null,
    SUM(CASE WHEN geo_point_2d IS NULL THEN 1 ELSE 0 END) AS nb_geo_point_2d_null
FROM ref_magasin;

-- 7.Contrôle d'intégrité sur les clés étrangères de la table retour_client
-- -------------------------------------------------------------------------
-- 7.1. Lignes de retour_client qui n'ont pas de produit correspondant
-- Si le résultat = 0 → toutes les cle_produit de retour_client existent dans produit → FK cohérente.
-- Si > 0 → on a le nombre de lignes « orphelines ».
SELECT COUNT(*) AS nb_retours_sans_produit
FROM retour_client rc
LEFT JOIN produit p
       ON rc.cle_produit = p.cle_produit
WHERE p.cle_produit IS NULL;

-- 7.2. -- Lignes de retour_client qui n'ont pas de magasin correspondant
-- Si le résultat = 0 → toutes les ref_magasin de retour_client existent dans ref_magasin → FK cohérente.
-- Si > 0 → on a le nombre de lignes « orphelines ».
SELECT COUNT(*) AS nb_retours_sans_magasin
FROM retour_client rc
LEFT JOIN ref_magasin rm
       ON rc.ref_magasin = rm.ref_magasin
WHERE rm.ref_magasin IS NULL;

-- 8. Conrôles métier
-- -----------------------
-- 8.1. Intervalles de notes entre 0 et 1
-- ---------------------------------------
SELECT
    COUNT(*) AS nb_retours_total,
    COUNT(CASE WHEN note BETWEEN 0 AND 10 THEN 1 END) AS nb_notes_0_10,
    COUNT(*) - COUNT(CASE WHEN note BETWEEN 0 AND 10 THEN 1 END) AS nb_notes_hors_0_10
FROM retour_client;

-- 8.2. Période couverte sur 2021
-- -------------------------------
SELECT
    MIN(date_achat) AS date_min,
    MAX(date_achat) AS date_max
FROM retour_client;

--8.3. Cohérence des recommandations clients(Oui, Non, Absente)
-- -------------------------------------------------------------
SELECT
    CASE
        WHEN recommandation = '1' THEN 'Oui'
        WHEN recommandation = '0' THEN 'Non'
        WHEN recommandation IS NULL OR TRIM(recommandation) = '' THEN 'Non renseigné'
        ELSE 'Valeur inattendue (' || recommandation || ')'
    END AS statut_recommandation,
    COUNT(*) AS nb,
    ROUND(
        100.0 * COUNT(*) / (SELECT COUNT(*) FROM retour_client),
        1
    ) AS pct
FROM retour_client
GROUP BY statut_recommandation
ORDER BY nb DESC;

-- 8.4. Cohérence des catégories de retours
-- ------------------------------------------
SELECT *
FROM (
    SELECT libelle_categorie, COUNT(*) AS nb
    FROM retour_client
    GROUP BY libelle_categorie

    UNION ALL

    SELECT 'TOTAL' AS libelle_categorie, COUNT(*) AS nb
    FROM retour_client
)
ORDER BY
    CASE WHEN libelle_categorie = 'TOTAL' THEN 1 ELSE 0 END,
    nb DESC;

-- 8.5. Cohérence de la source des retours (canaux)
-- ---------------------------------------------------
SELECT *
FROM (
    SELECT libelle_source, COUNT(*) AS nb
    FROM retour_client
    GROUP BY libelle_source

    UNION ALL

    SELECT 'TOTAL' AS libelle_source, COUNT(*) AS nb
    FROM retour_client
)
ORDER BY
    (libelle_source = 'TOTAL') ASC,  -- TOTAL en bas
    nb DESC;                         -- puis tri décroissant


-- --------------------------------------------------------
-- SCRIPT - REPONSES AUX QUESTIONS METIER D'OLIVIER
-- ----------------------------------------------------------

    --Q1 – Nombre de retours sur la livraison
-- ----------------------------------------------
SELECT COUNT(*) AS nb_retours_livraison
FROM retour_client
WHERE LOWER(libelle_categorie) = 'livraison';

--Q2 - Distribution des notes TV / réseaux sociaux
-- -----------------------------------------------------------------
SELECT rc.note,
       COUNT(*) AS nb_retours
FROM retour_client rc
JOIN produit p
  ON rc.cle_produit = p.cle_produit
WHERE rc.libelle_source = 'réseaux sociaux'
  AND p.titre_produit = 'TV'
GROUP BY rc.note
ORDER BY rc.note DESC;

--Q3 - Note moyenne par typologie de produit
-- -------------------------------------------
SELECT p.typologie_produit,
       ROUND(AVG(rc.note), 1) AS note_moyenne,
       COUNT(*)              AS nb_retours
FROM retour_client rc
JOIN produit p
  ON rc.cle_produit = p.cle_produit
GROUP BY p.typologie_produit
ORDER BY note_moyenne DESC;

--Q4 - Top 5 des magasins par note moyenne
-- -------------------------------------------
SELECT rm.ref_magasin,
       rm.departement,
       rm.libelle_de_commune,
       ROUND(AVG(rc.note), 1) AS note_moyenne,
       COUNT(*)              AS nb_retours
FROM retour_client rc
JOIN ref_magasin rm
  ON rc.ref_magasin = rm.ref_magasin
GROUP BY rm.ref_magasin
ORDER BY note_moyenne DESC
LIMIT 5;

--Q5 - Magasins => + de 12 feedbacks / drive
-- ----------------------------------------------------
SELECT rm.ref_magasin,
       rm.departement,
       rm.libelle_de_commune,
       COUNT(*) AS nb_feedbacks_drive
FROM retour_client rc
JOIN ref_magasin rm
  ON rc.ref_magasin = rm.ref_magasin
WHERE LOWER(rc.libelle_categorie) = 'drive'
GROUP BY rm.ref_magasin
HAVING COUNT(*) > 12
ORDER BY nb_feedbacks_drive DESC;

--Q6 - Classement des départements par note moyenne
-- ------------------------------------------------
SELECT rm.departement,
       ROUND(AVG(rc.note), 1) AS note_moyenne,
       COUNT(*)              AS nb_retours
FROM retour_client rc
JOIN ref_magasin rm
  ON rc.ref_magasin = rm.ref_magasin
GROUP BY rm.departement
ORDER BY note_moyenne DESC;

--Q7 - Typologie de produit avec le meilleur SAV
-- ----------------------------------------------
SELECT p.typologie_produit,
       ROUND(AVG(rc.note), 1) AS note_moyenne,
       COUNT(*)              AS nb_retours
FROM retour_client rc
JOIN produit p
  ON rc.cle_produit = p.cle_produit
WHERE LOWER(rc.libelle_categorie) = 'service après-vente'
GROUP BY p.typologie_produit
ORDER BY note_moyenne DESC;

--Q8 - Note moyenne sur l’ensemble des boissons
-- --------------------------------------------
SELECT ROUND(AVG(rc.note), 1) AS note_moyenne_boissons,
       COUNT(*)              AS nb_retours_boissons
FROM retour_client rc
JOIN produit p
  ON rc.cle_produit = p.cle_produit
WHERE p.titre_produit IN (
  'Boissons', 'Boissons alcoolisées',
  'Boissons avec sucre ajouté',
  'Boissons gazeuses',
  'Boissons instantanées','Cafés',
  'Cafés solubles','Sodas',
  'Aliments et boissons à base de végétaux'
);

--Q9 - Classement des jours de semaine en magasin
-- -----------------------------------------------
SELECT
  CASE strftime('%w', rc.date_achat)
    WHEN '0' THEN 'Dimanche'
    WHEN '1' THEN 'Lundi'
    WHEN '2' THEN 'Mardi'
    WHEN '3' THEN 'Mercredi'
    WHEN '4' THEN 'Jeudi'
    WHEN '5' THEN 'Vendredi'
    WHEN '6' THEN 'Samedi'
  END AS jour_semaine,
  ROUND(AVG(rc.note), 1) AS note_moyenne,
  COUNT(*)              AS nb_retours
FROM retour_client rc
WHERE LOWER(rc.libelle_categorie) = 'expérience en magasin'
GROUP BY jour_semaine
ORDER BY note_moyenne DESC;

--Q10 - Mois avec le plus de retours SAV
-- ------------------------------------------
SELECT strftime('%m', rc.date_achat) AS mois,
       COUNT(*)                     AS nb_retours_sav
FROM retour_client rc
WHERE LOWER(rc.libelle_categorie) = 'service après-vente'
GROUP BY mois
ORDER BY nb_retours_sav DESC
LIMIT 5;

-- Q11 - Pourcentage de recommandations client (parmi les répondants uniquement)
-- ---------------------------------------------------------------------------------
SELECT
    SUM(CASE WHEN recommandation IN ('0','1') THEN 1 ELSE 0 END) AS nb_repondants,
    SUM(CASE WHEN recommandation = '1' THEN 1 ELSE 0 END)         AS nb_oui,
    SUM(CASE WHEN recommandation = '0' THEN 1 ELSE 0 END)         AS nb_non,
    ROUND(
        100.0 * SUM(CASE WHEN recommandation = '1' THEN 1 ELSE 0 END)
        / SUM(CASE WHEN recommandation IN ('0','1') THEN 1 ELSE 0 END),
        1
    ) AS pct_oui_repondants
FROM retour_client;

--Q12 - Magasins avec note inférieure à la moyenne globale
-- ----------------------------------------------------------
SELECT
  rm.ref_magasin,rm.departement, rm.libelle_de_commune,
  ROUND(AVG(rc.note), 2) AS note_moyenne_magasin
FROM retour_client rc
JOIN ref_magasin rm
  ON rc.ref_magasin = rm.ref_magasin
GROUP BY rm.ref_magasin
HAVING AVG(rc.note) < (SELECT AVG(note) FROM retour_client)
ORDER BY note_moyenne_magasin DESC
LIMIT 5;

--Q13 - Typologies ayant amélioré leur moyenne entre T1 et T2 2021
-- -------------------------------------------------------------------
SELECT
  p.typologie_produit,
  ROUND(AVG(
    CASE WHEN strftime('%m', rc.date_achat) BETWEEN '01' AND '03'
         THEN rc.note END
  ), 1) AS note_T1,
  ROUND(AVG(
    CASE WHEN strftime('%m', rc.date_achat) BETWEEN '04' AND '06'
         THEN rc.note END
  ), 1) AS note_T2
FROM retour_client rc
JOIN produit p
  ON rc.cle_produit = p.cle_produit
WHERE strftime('%Y', rc.date_achat) = '2021'
  AND strftime('%m', rc.date_achat) BETWEEN '01' AND '06'
GROUP BY p.typologie_produit
HAVING note_T2 > note_T1
ORDER BY (note_T2 - note_T1) DESC;

--Q14 - NPS global
-- ----------------
SELECT
  ROUND(100.0 * SUM(CASE WHEN note >= 9 THEN 1 ELSE 0 END) / COUNT(*), 1)
    AS pct_promoteurs,
  ROUND(100.0 * SUM(CASE WHEN note <= 6 THEN 1 ELSE 0 END) / COUNT(*), 1)
    AS pct_detracteurs,
  ROUND(
    100.0 * SUM(CASE WHEN note >= 9 THEN 1 ELSE 0 END) / COUNT(*)
  - 100.0 * SUM(CASE WHEN note <= 6 THEN 1 ELSE 0 END) / COUNT(*),
    1
  ) AS nps_global
FROM retour_client;

--Q15 - NPS par source
-- -------------------
SELECT
  libelle_source,
  ROUND(100.0 * SUM(CASE WHEN note >= 9 THEN 1 ELSE 0 END) / COUNT(*), 1)
    AS pct_promoteurs,
  ROUND(100.0 * SUM(CASE WHEN note <= 6 THEN 1 ELSE 0 END) / COUNT(*), 1)
    AS pct_detracteurs,
  ROUND(
    100.0 * SUM(CASE WHEN note >= 9 THEN 1 ELSE 0 END) / COUNT(*)
  - 100.0 * SUM(CASE WHEN note <= 6 THEN 1 ELSE 0 END) / COUNT(*),
    1
  ) AS nps_source
FROM retour_client
GROUP BY libelle_source
ORDER BY nps_source DESC;

--Q16 - Nombre de retours par source
-- -------------------------------------
SELECT libelle_source,
       COUNT(*) AS nb_retours
FROM retour_client
GROUP BY libelle_source
ORDER BY nb_retours DESC;

--Q17 - Top 5 magasins avec le plus de feedbacks
-- ------------------------------------------------
SELECT
  rm.ref_magasin,
  rm.departement,
  rm.libelle_de_commune,
  COUNT(*) AS nb_retours
FROM retour_client rc
JOIN ref_magasin rm
  ON rc.ref_magasin = rm.ref_magasin
GROUP BY rm.ref_magasin
ORDER BY nb_retours DESC
LIMIT 5;

