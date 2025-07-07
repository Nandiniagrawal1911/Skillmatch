from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import spacy
import json
from docx import Document
from pdfminer.high_level import extract_text 
nlp = spacy.load("en_core_web_sm")
known_skills=["pyhton","sql","pandas","numpy","java","C++","C","excel","matplotlib","React","CSS","Javascript",
              "Node.js","C#","Docker","html","Flask"]
course_links = {
    "Python": "https://www.coursera.org/learn/python",
    "SQL": "https://www.codecademy.com/learn/learn-sql",
    "Pandas": "https://www.kaggle.com/learn/pandas",
    "React": "https://reactjs.org/docs/getting-started.html",
    "Flask": "https://www.freecodecamp.org/news/tag/flask/",
    "Docker": "https://docker-curriculum.com/",
    "Machine Learning": "https://www.coursera.org/learn/machine-learning",
    "Node.js": "https://nodejs.dev/en/learn",
    "JavaScript": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
    "HTML": "https://www.freecodecamp.org/learn/responsive-web-design/",
    "CSS": "https://www.freecodecamp.org/learn/responsive-web-design/"
}

def extract_skills(text):
    doc=nlp(text)
    found_skills=set() #no use of list beacuse set do not allow duplicate so better
    for skill in doc:
        if skill.text in known_skills:
            found_skills.add(skill.text)
    return list(found_skills) #because api returns json which do not understand set 


def extract_text_from_resume(file):
    filename=file.filename
    #save file temporary
    filepath=os.path.join("temp",filename)
    os.makedirs("temp", exist_ok=True)
    file.save(filepath)
    
    text = ""
    #extract text
    if filename.endswith(".pdf"):
        text=extract_text(filepath)
    elif filename.endswith(".docx"):
        doc = Document(filepath)
        text = "\n".join([para.text for para in doc.paragraphs])
    
    os.remove(filepath)
    return text
app = Flask(__name__)
CORS(app)  # To allow frontend requests

@app.route('/')
def home():
    return "SkillMatch Backend Running!"
    

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400

    resume = request.files['resume']
    # For now, just return filename
    text=extract_text_from_resume(resume)
    skills=extract_skills(text)
    return jsonify({"message": "Resume received", "filename": resume.filename,"extracted_skills": skills})

@app.route('/recommend-jobs', methods=['POST'])
def recommend_jobs():
    user_skills = request.json.get("skills", [])
    
    with open('jobs.json') as f:
        all_jobs = json.load(f)

    # Filter jobs based on overlap
    matched_jobs = []
    for job in all_jobs:
        required = set(job["required_skills"])
        user = set(user_skills)
        matched = user & required
        #matched =(set(user_skills) & set(job["required_skills"]))
        score = int((len(matched) / len(required)) * 100)
        if score > 0:
            missing=required-user
            recommend_courses=[]
            for skill in missing:
                link= course_links.get(skill, f"https://www.google.com/search?q={skill}+course")
                recommend_courses.append({skill: link})
            matched_jobs.append({"title": job["title"],
            "required_skills": job["required_skills"],
            "fit_percent": score,
            "recommended_courses": recommend_courses})

    return jsonify({"matched_jobs": matched_jobs})


if __name__ == '__main__':
    app.run(debug=True)