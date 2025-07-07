import React,{ useState } from "react";
import axios from "axios"
function UploadForm({onResults}){
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const handleUpload = async () => {
    if (!file) return alert("Upload a resume");

    const formData = new FormData();
    formData.append("resume", file);
     setLoading(true);
    try {
      const res = await axios.post("http://localhost:5000/upload-resume", formData);
      const extractedSkills = res.data.extracted_skills;

      // Now recommend jobs
      const jobRes = await axios.post("http://localhost:5000/recommend-jobs", {
        skills: extractedSkills
      });
       onResults(jobRes.data.matched_jobs);
    }catch(err){
        alert("Error: " + err.message);
    }
    setLoading(false);
};
return (
    <div className="mb-4">
      <div className="input-group">
        <input
          type="file"
          className="form-control"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button
          className="btn btn-primary"
          onClick={handleUpload}
          disabled={loading}
        >
          {loading ? "Processing..." : "Upload & Match"}
        </button>
      </div>
    </div>
  );
}

export default UploadForm;