import React, { useState } from 'react';
import UploadForm from './components/UploadForm';
import JobResults from './components/JobResults';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  const [matchedJobs, setMatchedJobs] = useState([]);

  return (
    <div style={{ padding: '2rem' }}>
      <h1 className="text-center mb-4" style={{ color: '#ffffff', textShadow: '1px 1px 4px #000' }}>
  🧠 SkillMatch – Job Recommender
      </h1>

      <UploadForm onResults={setMatchedJobs} />
      <JobResults jobs={matchedJobs} />
    </div>
  );
}

export default App;
