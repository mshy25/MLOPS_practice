# Iris ML Pipeline with DVC

A machine learning project demonstrating **Data Version Control (DVC)** with the classic Iris dataset. This project shows how to build reproducible ML pipelines that track code, data, models, and experiments.

## 🎯 Project Overview

This project trains a Random Forest classifier on the Iris dataset using:
- **Git** for code versioning
- **DVC** for data and model versioning
- **Scikit-learn** for machine learning
- **YAML** for parameter configuration

## 📁 Project Structure

```
iris-dvc/
├── .dvc/                  # DVC configuration
├── data/
│   └── iris.csv          # Dataset (tracked by DVC)
├── model/
│   └── model.pkl         # Trained model (tracked by DVC)
├── metrics/
│   └── eval.json         # Model accuracy metrics
├── prepare.py            # Data preparation script
├── train.py              # Model training script
├── params.yaml           # Hyperparameters configuration
├── dvc.yaml              # DVC pipeline definition
└── dvc.lock              # Pipeline lockfile
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- DVC

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/mshy25/MLOPS_practice.git
cd MLOPS_practice
```

2. **Create and activate virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install dvc pandas scikit-learn joblib pyyaml
```

4. **Pull data and models from DVC remote:**
```bash
dvc pull
```

5. **Run the pipeline:**
```bash
dvc repro
```

## 📊 Pipeline Stages

### Stage 1: Prepare
- **Command:** `python prepare.py`
- **Output:** `data/iris.csv`
- **Description:** Loads the Iris dataset and saves it as CSV

### Stage 2: Train
- **Command:** `python train.py`
- **Dependencies:** `data/iris.csv`, `train.py`
- **Parameters:** `test_size`, `n_estimators`, `random_state`
- **Outputs:** `model/model.pkl`, `metrics/eval.json`
- **Description:** Trains a Random Forest model and evaluates accuracy

## ⚙️ Configuration

Edit `params.yaml` to experiment with different parameters:

```yaml
split:
  test_size: 0.3        # Test set size (0.0 to 1.0)

train:
  n_estimators: 180     # Number of trees in random forest
  random_state: 42      # Random seed for reproducibility
```

## 🔬 Running Experiments

### Change parameters and re-run:
```bash
# Edit params.yaml with your preferred editor
nano params.yaml

# Run the pipeline (only affected stages will re-run)
dvc repro

# Compare with previous run
dvc params diff
dvc metrics diff
```

### Commit your experiment:
```bash
git add params.yaml dvc.lock
git commit -m "Experiment: test_size=0.3, n_estimators=180"
git push
dvc push
```

## 📈 View Results

### Check current accuracy:
```bash
cat metrics/eval.json
```

### Compare experiments:
```bash
# Compare parameters between commits
dvc params diff HEAD~1

# Compare metrics between commits
dvc metrics diff HEAD~1
```

## 🔄 Collaboration Workflow

### For collaborators:

1. **Clone the repository**
2. **Install dependencies**
3. **Pull data/models:** `dvc pull`
4. **Run experiments:** `dvc repro`
5. **Push changes:** `git push` + `dvc push`

## 🛠️ Technologies Used

- **Python 3.12** - Programming language
- **DVC** - Data version control
- **Git** - Code version control
- **Scikit-learn** - Machine learning library
- **Pandas** - Data manipulation
- **Joblib** - Model serialization

## 📝 Key Learnings

This project demonstrates:
- ✅ Reproducible ML pipelines
- ✅ Version control for data and models
- ✅ Parameter tracking and experiment comparison
- ✅ Efficient collaboration on ML projects
- ✅ Separation of code (Git) and data (DVC)

## 🤝 Contributing

Feel free to fork this project and experiment with:
- Different ML algorithms
- Additional pipeline stages
- More complex datasets
- Advanced DVC features

## 📚 Resources

- [DVC Documentation](https://dvc.org/doc)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Iris Dataset Information](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)

## 👤 Author

**mshy25**
- GitHub: [@mshy25](https://github.com/mshy25)

## 📄 License

This project is open source and available for educational purposes.

---

**Happy experimenting! 🚀**