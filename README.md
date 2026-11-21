<div align="center">

<img src="assets/header.svg" alt="Chaymae El Bahloul, Data Science and Data Engineering student, AI enthusiast" width="100%">

<a href="#in-2-the-flagship"><img alt="Flagship" src="https://img.shields.io/badge/Flagship-E8553D?style=for-the-badge"></a>
<a href="#in-3-the-method"><img alt="Method" src="https://img.shields.io/badge/Method-0E9F8E?style=for-the-badge"></a>
<a href="#in-4-all-projects"><img alt="Projects" src="https://img.shields.io/badge/Projects-6D4AFF?style=for-the-badge"></a>
<a href="#in-5-tools"><img alt="Tools" src="https://img.shields.io/badge/Tools-F4A300?style=for-the-badge"></a>
<a href="#in-6-journey"><img alt="Journey" src="https://img.shields.io/badge/Journey-1E1B2E?style=for-the-badge"></a>
<a href="#in-7-contact"><img alt="Contact" src="https://img.shields.io/badge/Contact-E8553D?style=for-the-badge"></a>

<br><br>

<img alt="Status: open to internship" src="https://img.shields.io/badge/Status-Open%20to%20internship-16A34A?style=flat-square">
<img alt="Location: El Kelâa des Sraghna, Morocco" src="https://img.shields.io/badge/Location-El%20Kel%C3%A2a%20des%20Sraghna%2C%20Morocco-E8553D?style=flat-square">
<img alt="Languages: Arabic, French, English" src="https://img.shields.io/badge/Languages-AR%20%C2%B7%20FR%20%C2%B7%20EN-0E9F8E?style=flat-square">
<img alt="Visits" src="https://hits.sh/github.com/Chaymae-El-Bahloul.svg?style=flat-square&label=Visits&color=1E1B2E&labelColor=F4A300">

</div>

&nbsp;

## In [2]: the flagship

> ### RC Gestion
> **What if the application could prevent tax delays instead of just recording them?**
>
> A web application that digitizes the management of an accounting firm: client files (individuals and companies), tax filings, simplified bookkeeping, payroll and company-creation tracking. It generates payslips, client sheets and PDF reports, sends alerts, and includes an AI module. Three roles: **Admin**, **Accountant**, **Client**.
>
> ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
>
> **[Read the code](https://github.com/Chaymae-El-Bahloul/RC-GESTION)**

<p align="center"><img src="assets/rc-gestion-live.svg" alt="Simulated live preview of RC Gestion: a Random Forest risk gauge, a revenue forecast and an Isolation Forest anomaly detector that triggers an alert to the accountant" width="100%"></p>
<p align="center"><sub>Animated preview drawn in SVG with demo data: the three models of <code>ai.py</code> at work.</sub></p>

<details>
<summary><b>Under the hood</b></summary>
<br>

```mermaid
flowchart LR
    U([Admin / Accountant / Client]) --> A[app.py<br>interface]
    A --> B[db.py<br>logic and data]
    B --> D[(SQLite)]
    B --> P[pdf_reports.py<br>payslips, reports]
    B --> M[ai.py<br>3 models]
```

| Model | Mission |
| --- | --- |
| Random Forest | Predict a client's risk of tax delay |
| Linear regression | Forecast next month's revenue |
| Isolation Forest | Detect suspicious declared amounts |

</details>

&nbsp;

## In [3]: the method

<p align="center"><img src="assets/pipeline.svg" alt="My method as notebook cells: an idea, a database, business logic, the interface, a touch of AI, a ready application" width="100%"></p>

| I can... | Proof |
| --- | --- |
| **Design** a solid database and business logic | RC Gestion, Leave Management, stadium_db |
| **Build** a complete application, from the interface to deployment | RC Gestion, GraphGen (tests, CI, Docker) |
| **Analyze and visualize** data to support decisions | Supermarket Dashboard, GraphGen |
| **Add AI** where it brings real value | RC Gestion (3 ML models), AI ChatBot |

&nbsp;

## In [4]: all projects

```python
projects.sort_values("year", ascending=False)
```

| Project | What it does | Stack | Code |
| --- | --- | --- | --- |
| **GraphGen** *(pair project)* | Import a CSV or Excel file and get exploratory analysis and interactive charts, with no code. 12 tests, GitHub Actions CI, Docker. | `Flask` `pandas` `Plotly` `Docker` | [repo](https://github.com/Chaymae-El-Bahloul/GraphGen) |
| **Smart Data Pipeline** *(team of three)* | Self-adaptive data pipeline, built for the DUT final-year project. | `Python` | [repo](https://github.com/Samah-boudallaa/smart-data-pipeline) |
| **Supermarket Dashboard** | Interactive dashboard: 6 filters, 4 key indicators, 9 chart types (boxplot, heatmap, sunburst, gauge...), updated in real time. | `Streamlit` `Plotly` `Pandas` | [repo](https://github.com/Chaymae-El-Bahloul/dashboard-supermarche) |
| **Leave Management** *(2025 internship)* | Employee tracking, requests and hierarchical approval for the Municipality of Kelâa des Sraghna. Bilingual French / Arabic. | `Flask` `SQLAlchemy` `SQLite` | [repo](https://github.com/Chaymae-El-Bahloul/Gestion-Conges) |
| **AI ChatBot** | Multilingual chatbot based on the Gemini API, with user request handling. | `Python` `Gemini API` | [repo](https://github.com/Chaymae-El-Bahloul/AI-chatbot) |
| **stadium_db** *(team of 5)* | Desktop application for student management (add, edit, delete, search, display). | `C` `GTK+ 3` `MySQL` | [repo](https://github.com/Chaymae-El-Bahloul/stadium_db) |

<p align="center"><a href="https://github.com/Chaymae-El-Bahloul?tab=repositories">All my repositories</a></p>

&nbsp;

## In [5]: tools

<p align="center"><img src="assets/skills.svg" alt="Technologies ranked by number of projects: Python 6, databases 3, Streamlit 2, Flask 2, Plotly 2, AI 2, Docker 1, C 1" width="100%"></p>

<details><summary><b>Full arsenal</b></summary>
<br>

| Domain | Tools |
| --- | --- |
| Languages | Python, R, SQL, JavaScript, PHP, C |
| Web and applications | Flask, Streamlit, SQLAlchemy, HTML / CSS |
| Databases | MySQL, Oracle SQL Developer, SQLite, Data Warehouse |
| Big Data and analytics | Hadoop, Kafka, Apache Spark, Power BI, Data Mining, machine learning |
| Artificial intelligence | Generative AI, Gemini API, Microsoft 365 Copilot, scikit-learn |
| Work tools | Git / GitHub, Docker, Ubuntu, WSL, VirtualBox, VS Code |

</details>

&nbsp;

## In [6]: journey

<p align="center"><img src="assets/timeline.svg" alt="Gantt timeline from 2023 to 2027: baccalaureate, DUT in Data Engineering, two internships, Bachelor in Data Science in progress" width="100%"></p>

<img align="right" src="assets/photo.png" alt="Chaymae El Bahloul" width="170">

I love building complete applications around data: interface, business logic, database and artificial intelligence. Each project is a chance to learn a new building block, from payroll to chatbots to visualization.

**Right now**

| | |
| --- | --- |
| Studying | Bachelor in Data Science, EST Kelâa des Sraghna |
| Building | A live demo and deeper ML features for RC Gestion |
| Learning | Apache Spark and Kafka |
| Looking for | An internship in Data / AI / Software |

<br clear="all">

### Certifications

| Certification | Issuer | What it covers |
| --- | --- | --- |
| **Career Essentials in Generative AI** | Microsoft and LinkedIn Learning | Generative AI fundamentals, effective prompts, responsible use of AI tools at work |
| **Learning Microsoft 365 Copilot** | LinkedIn Learning | Copilot in Word, Excel, PowerPoint, Outlook and Teams |
| **Master Series 4.0: Smart Factories, Hypermanufacturing & Beyond** | UNIDO and the Digital Development Agency (ADD), Morocco | Webinar series "Industry 4.0 and Digital Transformation", June to September 2025 · [certificate](certificates/attestation-unido-add.pdf) |

&nbsp;

## In [7]: contact

<p align="center"><img src="assets/footer.svg" alt="Let's build something with data" width="100%"></p>

<div align="center">

<a href="mailto:c.elbahloul2898@uca.ac.ma"><img alt="Email" src="https://img.shields.io/badge/Email-E8553D?style=for-the-badge&logo=gmail&logoColor=white"></a>
<a href="https://www.linkedin.com/in/chaymae-el-bahloul"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://chaymae-el-bahloul.github.io"><img alt="Portfolio" src="https://img.shields.io/badge/Interactive%20Portfolio-1E1B2E?style=for-the-badge&logo=googlechrome&logoColor=white"></a>

<sub>My portfolio has a real terminal and a quick menu: try Ctrl / ⌘ + K.</sub>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Chaymae-El-Bahloul/Chaymae-El-Bahloul/output/github-contribution-grid-snake-dark.svg">
  <img alt="Snake eating my GitHub contributions" src="https://raw.githubusercontent.com/Chaymae-El-Bahloul/Chaymae-El-Bahloul/output/github-contribution-grid-snake.svg" width="100%">
</picture>

</div>
