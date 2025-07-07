import React from 'react';

function JobResults({ jobs }) {
  return (
    <div>
      <h2 className="text-left mb-4" style={{ color: '#ffffff', textShadow: '1px 1px 4px #000' }}>Matched Jobs</h2>
      <div className="row">
        {jobs.map((job, index) => (
          <div className="col-md-6" key={index}>
            <div className="card mb-4 shadow-sm">
              <div className="card-body">
                <h5 className="card-title">{job.title}</h5>
                <p><strong>Required Skills:</strong> {job.required_skills.join(', ')}</p>
                <p><strong>Fit:</strong> {job.fit_percent}%</p>
                {job.recommended_courses?.length > 0 && (
                  <div>
                    <strong>Courses:</strong>
                    <ul className="list-unstyled">
                      {job.recommended_courses.map((course, i) => {
                        const skill = Object.keys(course)[0];
                        const link = course[skill];
                        return (
                          <li key={i}>
                            <a href={link} target="_blank" rel="noreferrer">{skill}</a>
                          </li>
                        );
                      })}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default JobResults;
