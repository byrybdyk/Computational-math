import React, { useState } from 'react';

const SaveToFileButton = ({ response }) => {
  const handleSaveToFile = () => {
    const blob = new Blob([response], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'file.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  };

  return (
    <button onClick={handleSaveToFile}>Сохранить в файл</button>
  );
};

export default SaveToFileButton;
