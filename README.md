<div align="center">

<img src="assets/header.svg" alt="Chaymae El Bahloul, étudiante en Sciences des Données" width="100%">

<img src="assets/roles.svg" alt="Étudiante en Sciences des Données, Data Engineering et IA : des applications complètes, de la base à l'interface" width="100%">

<a href="#boot"><img alt="Boot" src="https://img.shields.io/badge/%3E_Boot-0B1020?style=for-the-badge"></a>
<a href="#projet-phare"><img alt="Projets" src="https://img.shields.io/badge/Projets-FF6B35?style=for-the-badge"></a>
<a href="#mes-outils"><img alt="Outils" src="https://img.shields.io/badge/Outils-14B8A6?style=for-the-badge"></a>
<a href="#git-log"><img alt="Parcours" src="https://img.shields.io/badge/Parcours-8B5CF6?style=for-the-badge"></a>
<a href="#contact"><img alt="Contact" src="https://img.shields.io/badge/Contact-0B1020?style=for-the-badge"></a>

<br><br>

**Je transforme des idées en applications complètes : de la base de données à l'interface, avec une touche d'intelligence artificielle.**

<img alt="Localisation : El Kelâa des Sraghna, Maroc" src="https://img.shields.io/badge/Lieu-El%20Kel%C3%A2a%20des%20Sraghna%2C%20Maroc-FF6B35?style=flat-square">
<img alt="Langues : arabe, français, anglais" src="https://img.shields.io/badge/Langues-AR%20%C2%B7%20FR%20%C2%B7%20EN-14B8A6?style=flat-square">
<img alt="Formation : Bachelor Sciences des Données" src="https://img.shields.io/badge/Bachelor-Sciences%20des%20Donn%C3%A9es-8B5CF6?style=flat-square">
<img alt="Visites" src="https://hits.sh/github.com/Chaymae-El-Bahloul.svg?style=flat-square&label=Visites&color=0B1020&labelColor=FF6B35">

</div>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## Boot

```text
$ ./chaymae --boot

[  OK  ] Profil chargé .............. Chaymae El Bahloul
[  OK  ] Formation .................. Bachelor Sciences des Données (en cours)
[  OK  ] Base solide ................ DUT Ingénierie des Données
[  OK  ] Stack ...................... Python · SQL · Flask · Streamlit · C
[  OK  ] Projets compilés ........... 7
[  OK  ] Stages validés ............. 2
[  OK  ] Langues .................... arabe · français · anglais
[ INFO ] Curiosité .................. illimitée
[ WAIT ] En attente de ton message .. c.elbahloul2898@uca.ac.ma
```

<p align="center"><img src="assets/stats.svg" alt="Chiffres clés : 7 projets, 2 stages, 3 langues, 2 certifications" width="100%"></p>

## Choisis ta mission

<table>
<tr>
<td width="33%" valign="top">

**Mission : recruter**

Mon projet phare, mon parcours et mes deux stages.

[Voir le projet phare](#projet-phare)<br>
[Voir mon git log](#git-log)

</td>
<td width="33%" valign="top">

**Mission : lire du code**

Mes projets, mes technologies, mes dépôts.

[Voir les projets](#tous-mes-projets)<br>
[Voir mes outils](#mes-outils)

</td>
<td width="33%" valign="top">

**Mission : explorer**

Interroge mon terminal, ou essaie mon portfolio interactif.

[Ouvrir le terminal](#terminal-interactif)<br>
[Aller au portfolio](https://chaymae-el-bahloul.github.io)

</td>
</tr>
</table>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## Ce que je sais faire

| Je peux... | Preuve |
| --- | --- |
| **Concevoir** une base de données et une logique métier solides | RC Gestion, Gestion de congés, stadium_db |
| **Construire** une application complète, de l'interface au déploiement | RC Gestion, GraphGen (tests, CI, Docker) |
| **Analyser et visualiser** des données pour décider | Dashboard supermarché, GraphGen |
| **Ajouter de l'IA** là où elle apporte une vraie valeur | RC Gestion (3 modèles ML), AI ChatBot |

<p align="center"><img src="assets/method.svg" alt="Ma méthode : une idée, une base de données, la logique métier, l'interface, une touche d'IA, puis une application prête" width="100%"></p>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## Projet phare

> ### RC Gestion
> **Et si l'application pouvait prévenir les retards fiscaux au lieu de les constater ?**
> Une application web qui digitalise la gestion d'un cabinet comptable : dossiers clients (personnes physiques et morales), déclarations fiscales, comptabilité simplifiée, paie et suivi de création d'entreprises.
> Elle génère automatiquement bulletins de paie, fiches clients et rapports PDF, envoie des alertes et intègre un module d'IA. Trois rôles : **Admin**, **Comptable**, **Client**.
>
> ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white) ![PDF](https://img.shields.io/badge/Rapports%20PDF-0B1020)
>
> **[Voir le code](https://github.com/Chaymae-El-Bahloul/RC-GESTION)**

<details>
<summary><b>Sous le capot de RC Gestion</b></summary>
<br>

```text
RC_Gestion_/
├── app.py            interface et navigation
├── db.py             logique métier et données
├── pdf_reports.py    bulletins et rapports
└── ai.py             modèles d'IA
```

| Modèle | Mission |
| --- | --- |
| Random Forest | Prédire le risque de retard fiscal d'un client |
| Régression linéaire | Prévoir le chiffre d'affaires du mois suivant |
| Isolation Forest | Détecter les montants déclarés suspects |

</details>

## Tous mes projets

<table>
<tr>
<td width="33%" valign="top">

**GraphGen** *(en binôme)*

Importe un CSV ou Excel et obtiens l'analyse exploratoire et des graphiques interactifs, sans écrire une ligne de code. 12 tests, CI GitHub Actions, Docker.

`Flask` `pandas` `Plotly` `Docker`

[Voir le code](https://github.com/Chaymae-El-Bahloul/GraphGen)

</td>
<td width="33%" valign="top">

**Smart Data Pipeline** *(en trinôme, PFE)*

Pipeline de données auto-adaptatif, réalisé pour le projet de fin d'études du DUT.

`Python` `Pipeline de données`

[Voir le code](https://github.com/Samah-boudallaa/smart-data-pipeline-pfe)

</td>
<td width="33%" valign="top">

**Dashboard supermarché**

Tableau de bord interactif : 6 filtres, 4 indicateurs clés et 9 types de visualisations (boxplot, heatmap, sunburst, gauge...), mis à jour en temps réel.

`Streamlit` `Plotly` `Pandas`

[Voir le code](https://github.com/Chaymae-El-Bahloul/dashboard-supermarche)

</td>
</tr>
<tr>
<td width="33%" valign="top">

**Gestion de congés** *(stage 2025)*

Suivi des employés, demandes et validation hiérarchique pour la Commune de Kelâa des Sraghna. Interface bilingue français / arabe.

`Flask` `SQLAlchemy` `SQLite`

</td>
<td width="33%" valign="top">

**AI ChatBot**

Chatbot multilingue basé sur l'API Gemini, avec gestion des requêtes des utilisateurs.

`Python` `Gemini API`

</td>
<td width="33%" valign="top">

**stadium_db** *(en équipe de 5)*

Application de bureau de gestion d'étudiants (ajout, modification, suppression, recherche, affichage).

`C` `GTK+ 3` `MySQL`

[Voir le code](https://github.com/Chaymae-El-Bahloul/stadium_db)

</td>
</tr>
</table>

<p align="center"><a href="https://github.com/Chaymae-El-Bahloul?tab=repositories">Voir tous mes dépôts</a></p>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## Mes outils

<p align="center"><img src="assets/orbit.svg" alt="Mes outils en orbite autour de Data et IA : Python, SQL, R, Flask, Streamlit, Docker, Git, MySQL, SQLite, Spark, Kafka, Hadoop, Power BI" width="100%"></p>

<p align="center"><img src="assets/skills.svg" alt="Technologies classées par nombre de projets : Python 6, bases de données 3, Streamlit 2, Flask 2, Plotly 2, IA 2, Docker 1, C 1" width="100%"></p>

*Déplie un domaine pour voir tout l'arsenal.*

<details><summary><b>Langages</b></summary>

Python, R, SQL, JavaScript, PHP, C

</details>

<details><summary><b>Web et applications</b></summary>

Flask, Streamlit, SQLAlchemy, HTML / CSS

</details>

<details><summary><b>Bases de données</b></summary>

MySQL, Oracle SQL Developer, SQLite, Data Warehouse

</details>

<details><summary><b>Big Data et analyse</b></summary>

Hadoop, Kafka, Apache Spark, Power BI, Data Mining, apprentissage automatique

</details>

<details><summary><b>Intelligence artificielle</b></summary>

IA générative, API Gemini, Microsoft 365 Copilot, scikit-learn

</details>

<details><summary><b>Outils de travail</b></summary>

Git / GitHub, Docker, Ubuntu, WSL, VirtualBox, VS Code

</details>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## En chiffres

<table>
<tr>
<td width="50%" align="center"><img src="assets/donut.svg" alt="Répartition de mes 7 projets par type : 3 applications web, 1 visualisation, 1 data engineering, 1 IA conversationnelle, 1 application de bureau" width="100%"></td>
<td width="50%" align="center"><img src="assets/radar.svg" alt="Radar de ma boîte à outils : langages 6, web 4, bases de données 4, big data 6, IA 4, outils 6" width="100%"></td>
</tr>
</table>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## Terminal interactif

*Clique sur une commande pour voir la réponse.*

<details>
<summary><code>$ about</code></summary>

```text
Chaymae El Bahloul, étudiante en Bachelor Sciences des Données (EST Kelâa des Sraghna)
après un DUT en Ingénierie des Données. Je transforme des idées en applications
complètes : base de données, interface et IA.
```

</details>

<details>
<summary><code>$ ls projets/</code></summary>

```text
RC_Gestion/    GraphGen/    smart-data-pipeline/    dashboard-supermarche/
gestion-conges/    ai-chatbot/    stadium_db/
```

</details>

<details>
<summary><code>$ langues</code></summary>

```text
arabe (langue maternelle) · français (professionnel) · anglais (professionnel)
```

</details>

<details>
<summary><code>$ fortune</code></summary>

```text
Un bug, c'est juste une fonctionnalité
qui n'a pas encore trouvé son utilisateur.
```

</details>

<details>
<summary><code>$ sudo recruter chaymae</code></summary>

```text
[sudo] mot de passe : ********
Permission accordée.
Étape suivante : écrire à c.elbahloul2898@uca.ac.ma
```

</details>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## Qui suis-je ?

<img align="right" src="assets/photo.png" alt="Chaymae El Bahloul" width="170">

J'aime construire des applications complètes autour des données : interface, logique métier, base de données et intelligence artificielle. Chaque projet est l'occasion d'apprendre une nouvelle brique, de la paie au chatbot en passant par la visualisation.

```python
chaymae = {
    "etudes":  "Bachelor Sciences des Données (EST Kelâa des Sraghna)",
    "base":    "DUT Ingénierie des Données, Université Cadi Ayyad",
    "stack":   ["Python", "SQL", "Flask", "Streamlit"],
    "passion": "IA & Data",
    "lieu":    "El Kelâa des Sraghna, Maroc",
    "langues": ["arabe", "français", "anglais"],
}
```

<br clear="all">

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## Git log

<p align="center"><img src="assets/gantt.svg" alt="Frise chronologique : baccalauréat 2023-2024, DUT 2024-2026, stage gestion de congés 2025, stage RC Gestion 2026, Bachelor 2026-2027 en cours" width="100%"></p>

*Mon parcours, raconté comme un historique de commits.*

```text
$ git log --oneline

a7f3c21 (HEAD -> main) 2026-2027      Bachelor Sciences des Données, EST Kelâa des Sraghna (en cours)
5be90d4                avr-juin 2026  Stage : RC Gestion (architecture en couches, paie, bulletins, rôles)
3c1d8e7                juin-juil 2025 Stage : gestion de congés, Commune de Kelâa des Sraghna
9a02f6b                2024-2026      DUT Ingénierie des Données, EST Kelâa des Sraghna, UCA
1e4d7a0                2023-2024      Baccalauréat Sciences Physiques, Lycée Al Maghrib Al Arabi
0000000 (initial)      depuis toujours  la curiosité
```

<details>
<summary><b>Langues et certifications</b></summary>
<br>

**Langues :** arabe (langue maternelle) · français (professionnel) · anglais (professionnel)

**Certifications :** Career Essentials in Generative AI · Learning Microsoft 365 Copilot

</details>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## Mon activité

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Chaymae-El-Bahloul/Chaymae-El-Bahloul/output/github-contribution-grid-snake-dark.svg">
  <img alt="Serpent qui mange mes contributions GitHub" src="https://raw.githubusercontent.com/Chaymae-El-Bahloul/Chaymae-El-Bahloul/output/github-contribution-grid-snake.svg" width="100%">
</picture>
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## Contact

<div align="center">

### Une question, une opportunité, une idée de projet ?

<a href="mailto:c.elbahloul2898@uca.ac.ma"><img alt="E-mail" src="https://img.shields.io/badge/E--mail-FF6B35?style=for-the-badge&logo=gmail&logoColor=white"></a>
<a href="https://www.linkedin.com/in/chaymae-el-bahloul"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://chaymae-el-bahloul.github.io"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio%20interactif-0B1020?style=for-the-badge&logo=googlechrome&logoColor=white"></a>

<sub>Mon portfolio a un vrai terminal et un menu rapide : essaie Ctrl / ⌘ + K.</sub>

</div>

<p align="center"><img src="assets/footer.svg" alt="Construisons quelque chose avec des données" width="100%"></p>
