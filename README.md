🔐 Cyber Threat Detection System using Machine Learning

📌 Overview

This project is a Cybersecurity AI System that detects potential cyber threats using a Machine Learning model.
It uses a trained Random Forest Classifier and exposes predictions through a Flask API.

---

🚀 Features

- Detects cyber threats based on input features
- Machine Learning model trained on real-world-like data
- REST API using Flask
- Easily deployable on cloud platforms (AWS / GCP)

---

🧠 Tech Stack

- Python
- Flask
- Scikit-learn
- NumPy / Pandas
- Jupyter Notebook

---

📂 Project Structure

Cybersecurity_Project/
│── app.py
│── model.pkl
│── test_api.py
│── train_model.ipynb
│── requirements.txt
│── sample_input.json
│── README.md

---

⚙️ How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run Flask API

python app.py

3. Test API

python test_api.py

---

📡 API Endpoint

POST /predict

Input (JSON)

{
  "0": 12,
  "1": 5,
  ...
  "41": 3
}

Output

{
  "Prediction": 1
}

---

📊 Model Details

- Algorithm: Random Forest Classifier
- Input Features: 42
- Output: Cyber Threat (0 = Safe, 1 = Threat)

---

🔄 Future Improvements

- Train with real-world cybersecurity datasets
- Deploy on AWS Lambda / Google Cloud
- Real-time threat detection system
- Continuous model updates

---

👩‍💻 Author

Dhananjay Bhaskar

---

⭐ If you like this project, consider giving it a star!
