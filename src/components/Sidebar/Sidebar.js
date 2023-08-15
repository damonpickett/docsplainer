import React, { useState } from 'react';

const Sidebar = () => {
  const [pdfFile, setPdfFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setPdfFile(file);
  };

  const handleUpload = () => {
    // Handle PDF file upload logic here
    if (pdfFile) {
      // You can use APIs to upload the PDF file to a server
      console.log('Uploading PDF:', pdfFile.name);
    }
  };

  return (
    <div className="sidebar">
      <h2>Upload PDF</h2>
      <input type="file" accept=".pdf" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default Sidebar;