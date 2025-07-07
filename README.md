
# 🧠 SkillMatch – Intelligent Job & Skill Recommender

SkillMatch is a smart resume-based job recommender system that analyzes your resume, extracts your skills using NLP, and recommends matching job profiles and learning resources to upskill.  

> 🔍 Powered by Flask, React, and SpaCy NLP.

---

## 🌐 Live Demo (optional if deployed)
> _[Coming Soon / Add your deployed link here]_

---

## 📌 Features

- 📄 Upload resume (.pdf or .docx)
- 🧠 Extract skills using NLP (SpaCy)
- 💼 Get matched jobs based on skill overlap
- 📊 See skill-job fit percentage
- 📚 Get course suggestions for missing skills
- ✅ Responsive UI using React + Bootstrap
- 🔁 (Optional) Save resume history for future reference

---

## 🛠 Tech Stack

| Frontend | Backend | NLP | Database |
|----------|---------|-----|----------|
| React (Vite) | Flask | SpaCy (en_core_web_sm) | (Optional: MongoDB or PostgreSQL) |

---

## 🚀 How It Works

1. **Upload your resume**
2. Backend extracts text & skills from the file
3. Compares your skills with job listings
4. Returns matching job roles + fit % + learning links

---

## 🖼 UI Preview

![SkillMatch UI](https://user-images.githubusercontent.com/your_screenshot.png)  
_👉 Add your screenshot or demo GIF here_

---

## 📁 Folder Structure

```
skillmatch/
│
├── skillmatch-backend/
│   ├── app.py
│   ├── jobs.json
│   └── ...
│
├── skillmatch-frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── UploadForm.jsx
│   │   │   └── JobResults.jsx
│   │   └── App.jsx
│   └── ...
```

---

## 🔧 Setup Instructions

### 📦 Backend

```bash
cd skillmatch-backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
```

### ⚛️ Frontend

```bash
cd skillmatch-frontend
npm install
npm run dev
```

---

## ✨ Bonus Ideas

- Save and view history of resume uploads
- Add authentication (login/signup)
- Integrate real job APIs like LinkedIn or Indeed
- Deploy full app (Render / Vercel / Netlify + FlaskAnywhere)

---

## 🙋‍♀️ Made By

**Nandini Agrawal**  
_Beginner Web & ML Enthusiast | ECE Undergrad_  
📫 [Your LinkedIn or Email if you want to share]
