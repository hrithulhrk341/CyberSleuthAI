# 🛡 CyberSleuthAI - Autonomous Threat Detection Dashboard

CyberSleuthAI is a modern, lightweight, real-time threat monitoring system built using Flask, Python, and frontend visualizations. It detects SSH brute-force attacks, displays attack metrics on a beautiful dashboard, and includes unique features like **incident replay** and **live brute-force attempt graphs**.

---

## 🚀 Features

* 📊 **Real-Time Brute-Force Detection** from `/var/log/auth.log`
* 📈 **Live Updating Graphs** for login attempts
* 🎞 **Incident Replay (Timeline Mode)** to visualize brute-force attack patterns
* 📬 Optional **Email Alert Integration** on detection
* 📁 Modular Codebase (core, app, utils, data)
* 🌐 Web Dashboard built with **Chart.js + Flask**

---

## 📸 Screenshots

> Add screenshots to `assets/` folder and reference here.

---

## 🧰 Tech Stack

* **Backend**: Python 3.13, Flask
* **Frontend**: Chart.js, HTML, CSS
* **Deployment**: Linux / Kali
* **Monitoring**: Live log tailing, custom parser

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/hrithulhrk341/CyberSleuthAI.git
cd CyberSleuthAI
```

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Monitoring Log

```bash
python CyberSleuthAI/app/log_watcher.py
```

### 5. Launch the Web Dashboard

```bash
export PYTHONPATH=$(pwd)
export FLASK_APP=CyberSleuthAI.app:create_app
export FLASK_ENV=development
flask run
```

---

## 📫 Optional: Enable Email Alerts

Edit `utils/emailer.py` with your credentials (for testing purposes only!)

```python
EMAIL_ADDRESS = "your-email"
EMAIL_PASSWORD = "your-app-password"
```

---

## 📁 Folder Structure

```
CyberSleuthAI/
├── app/
├── core/
├── data/
├── utils/
├── templates/
├── static/
├── alerts/
├── run.py
├── requirements.txt
└── README.md
```

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](./LICENSE) file for details.

---

## 🙌 Author

**Hrithul Krishna**
GitHub: [@hrithulhrk341](https://github.com/hrithulhrk341)

---

## ⭐ Star This Repo

If you found this project useful, give it a ⭐ on GitHub — it motivates future development!

```bash
https://github.com/hrithulhrk341/CyberSleuthAI
```
