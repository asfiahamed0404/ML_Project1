# 🎓 Student Performance Predictor — End-to-End ML Project

> A production-style machine learning project that predicts a student's **Math Score** based on demographic & academic features. Built with a clean modular pipeline, a colorful animated Flask UI, and best practices for reproducibility.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  <img alt="CatBoost" src="https://img.shields.io/badge/CatBoost-1.2%2B-FFCC00?style=for-the-badge&logoColor=black">
  <img alt="XGBoost" src="https://img.shields.io/badge/XGBoost-2.0%2B-0060AA?style=for-the-badge&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge">
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-6366f1?style=for-the-badge">
</p>

<p align="center">
  <a href="#-demo"><img alt="Demo" src="https://img.shields.io/badge/▶-Live%20Demo-ec4899?style=for-the-badge"></a>
  <a href="#-quick-start"><img alt="Quick Start" src="https://img.shields.io/badge/⚡-Quick%20Start-06b6d4?style=for-the-badge"></a>
  <a href="#-api"><img alt="API" src="https://img.shields.io/badge/🔌-API%20Routes-f59e0b?style=for-the-badge"></a>
  <a href="#-architecture"><img alt="Architecture" src="https://img.shields.io/badge/🧩-Architecture-10b981?style=for-the-badge"></a>
</p>

---

## ✨ Highlights

<table>
<tr>
<td width="50%" valign="top">

### 🧠 **ML Pipeline**
- 📥 **Data Ingestion** — Loads `stud.csv`, persists train/test splits to `artifacts/`
- 🛠️ **Data Transformation** — Numerical scaling + categorical one-hot encoding (`ColumnTransformer`)
- 🧪 **Model Training** — `GridSearchCV` across **8 regressors**, best model saved as `model.pkl`

</td>
<td width="50%" valign="top">

### 🎨 **Web UI**
- 🌈 Animated gradient background with floating color blobs
- 🪟 Glassmorphism cards, smooth fade-up & pop animations
- 🎯 Animated score-meter ring + 🪅 confetti on prediction
- 📱 Fully responsive (mobile → desktop)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ⚙️ **Engineering**
- 🪵 Custom timestamped logger (file + console handlers)
- 🚨 Custom exception class with file & line number
- 💾 Pickled artifacts via `dill`
- 🧱 `setup.py` based packaging (`-e .` install)

</td>
<td width="50%" valign="top">

### 🔌 **API Endpoints**
- `GET /` — Landing page
- `GET|POST /predictdata` — Predict math score
- `GET /train` — Retrain pipeline end-to-end
- `GET /health` — JSON health & artifact check

</td>
</tr>
</table>

---

## 📸 Demo

<p align="center">
  <img src="assets/landing.png" alt="Landing Page" width="48%">
  <img src="assets/predict.png" alt="Predict Page" width="48%">
</p>

<p align="center">
  <img src="assets/demo.gif" width="800">
</p>

---

## 🧩 Architecture

```
┌──────────────────┐    ┌────────────────────┐    ┌────────────────────┐
│   Data Source    │──▶ │   Data Ingestion   │──▶ │  Data Transformation│
│  stud.csv        │    │   (src/components) │    │  (ColumnTransformer)│
└──────────────────┘    └────────────────────┘    └─────────┬──────────┘
                                                           │
                                                           ▼
                        ┌────────────────────┐    ┌────────────────────┐
                        │   Flask Web App    │◀── │  Model Trainer     │
                        │   (templates + UI) │    │  (GridSearchCV x8) │
                        └────────────────────┘    └────────────────────┘
```

---

## 🚀 Quick Start

Pick the workflow that fits your machine. All three end up with the same running app.

---

### 🪟 Option A — Conda (Windows-friendly, prefix env)

```cmd
:: 1) Open the project in VS Code
code .

:: 2) Create a local Conda env (prefix style, no global registration)
conda create -p venv python==3.8 -y

:: 3) (One-time) enable 'conda activate' in cmd
conda init
::     **Close & reopen your terminal** so the changes take effect.

:: 4) Activate the env
conda activate venv\

:: 5) Install dependencies + editable package
pip install -r requirements.txt
pip install -e .
```

> 💡 `conda activate venv\` works because the env was created with a **prefix path** (`-p venv`) — that's why the trailing `\` is required on Windows.

---

### 🐍 Option B — `venv` (built-in, no Conda)

**Windows (cmd / PowerShell):**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

---

### 🧪 Option C — Conda with `environment.yml`

If you prefer a fully reproducible environment from a YAML file:

```cmd
conda env create -f environment.yml
conda activate mlproject
pip install -e .
```

A ready-to-use `environment.yml` is provided — see below.

---

### ⚡ One-click helpers (optional)

- **Windows:** double-click `setup-windows.cmd`
- **macOS / Linux:** `bash setup.sh`

Both scripts create the env, install deps and print the next steps.

---

### 🧠 Train the model

```bash
# Option 1 — trigger via the API
python app.py
# then visit http://127.0.0.1:5000/train

# Option 2 — direct CLI
python -m src.pipeline.train_pipeline
```

This produces:

```
artifacts/
├── data.csv         # raw ingested data
├── train.csv        # 80% split
├── test.csv         # 20% split
├── preprocessor.pkl # ColumnTransformer
└── model.pkl        # best model
```

---

### ▶️ Run the app

```bash
python app.py
```

Then open **<http://127.0.0.1:5000/>** in your browser.

---

## 🔌 API

| Method | Route           | Description                                          |
| :----- | :-------------- | :--------------------------------------------------- |
| `GET`  | `/`             | Colorful landing page                                |
| `GET`  | `/predictdata`  | Render the prediction form                           |
| `POST` | `/predictdata`  | Predict the math score from form fields              |
| `GET`  | `/train`        | Retrain the end-to-end pipeline                      |
| `GET`  | `/health`       | JSON health-check incl. artifact existence          |

### Example: `POST /predictdata`

```bash
curl -X POST http://127.0.0.1:5000/predictdata \
  -d "gender=female" \
  -d "race_ethnicity=group B" \
  -d "parental_level_of_education=bachelor's degree" \
  -d "lunch=standard" \
  -d "test_preparation_course=completed" \
  -d "reading_score=88" \
  -d "writing_score=92"
```

Returns the rendered HTML containing the predicted score.

---

## 🗂️ Project Structure

```
ML_Project/
├── app.py                         # Flask entry-point + routes
├── setup.py                       # Package configuration
├── requirements.txt
├── LICENSE
├── README.md
├── .env.example
├── artifacts/                     # Generated at train-time
│   ├── data.csv
│   ├── train.csv / test.csv
│   ├── preprocessor.pkl
│   └── model.pkl
├── logs/                          # Timestamped log files
├── notebook/
│   ├── data/stud.csv
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   └── 2. MODEL TRAINING.ipynb
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── utils.py
│   ├── logger.py
│   └── exception.py
├── static/
│   ├── css/style.css              # Global styles
│   └── js/main.js                 # UI polish (confetti, meter)
└── templates/
    ├── index.html                 # Landing page
    └── home.html                  # Prediction form
```

---

## 🧪 Models Compared

| Model                   | Tuned? |
| :---------------------- | :----: |
| Linear Regression       |   ✅   |
| Decision Tree           |   ✅   |
| Random Forest           |   ✅   |
| Gradient Boosting       |   ✅   |
| K-Neighbors Regressor   |   ✅   |
| XGBRegressor            |   ✅   |
| CatBoosting Regressor   |   ✅   |
| AdaBoost Regressor      |   ✅   |

The best model (by R² on the test set) is auto-selected and serialized to `artifacts/model.pkl`.

---

## 🛡️ Error Handling & Logging

- All exceptions go through `CustomException`, which enriches messages with **file name** and **line number**.
- Logs go to both `logs/<timestamp>.log` and the console.
- Input validation protects against out-of-range scores and missing artifacts.

---

## 🧰 Tech Stack

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white">
  <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
  <img alt="CatBoost" src="https://img.shields.io/badge/CatBoost-FFCC00?style=flat-square&logoColor=black">
  <img alt="XGBoost" src="https://img.shields.io/badge/XGBoost-0060AA?style=flat-square&logoColor=white">
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white">
  <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white">
  <img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white">
  <img alt="CSS3" src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white">
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black">
</p>

---

## 🗺️ Roadmap

- [x] Colorful animated UI with confetti & score meter
- [x] Robust error handling & input validation
- [x] Configurable artifact paths (BASE_DIR-based)
- [x] `/train` & `/health` API routes
- [ ] Dockerize the app
- [ ] Add CI (GitHub Actions) — lint + import sanity
- [ ] Add SHAP feature importance plot
- [ ] Add unit tests with `pytest`

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to open an issue or PR.

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for the full text.

---

<p align="center">
  Made with ❤️ by <a href="mailto:muasfiahamed276@gmail.com">Asfi</a> • ⭐ this repo if you found it useful!
</p>