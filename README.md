# Phishing Detection AI 🔒

A simple project to detect phishing URLs using Python.  
Starts with **basic rule-based checks** and extends to **machine learning**.

## Project Overview

This project helps identify suspicious URLs that may be used for phishing attacks.  
It demonstrates both simple rule-based detection and a basic ML model.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/FaizAjmal/Phishing-Detection-using-AI.git
cd Phishing-Detection-using-AI
```
2 . Install required packages:
```bash
pip install -r requirements.txt
```

### 📂 Project Structure

phishing-detection-ai/
├── data/ # Datasets (CSV files)
│ └── phishing_urls.csv
├── scripts/ # Python scripts
│ ├── simple_phishing_checker.py
│ ├── smart_phishing_checker.py
│ └── generate_dataset.py
└── notebooks/ # ML experiments
└── ml_experiment.py



## How to Run

### 1) Simple Checker
```bash
python scripts/simple_phishing_checker.py
```
### 2) Smart Checker
```bash
python scripts/smart_phishing_checker.py
```
### 3) Generate Dataset
```bash
python scripts/generate_dataset.py
```
### 4) ML Experiment
```bash
python notebooks/ml_experiment.py

```
Requirements

⦁	Python 3.x
⦁	pandas
⦁	scikit-learn
