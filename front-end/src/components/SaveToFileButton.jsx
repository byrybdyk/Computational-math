import React, { useState } from 'react';

const SaveToFileButton = ({ response }) => {
  const handleSaveToFile = () => {
    // Создаем новый объект Blob из содержимого response
    const blob = new Blob([response], { type: 'text/plain' });
    // Создаем ссылку на объект Blob
    const url = window.URL.createObjectURL(blob);
    // Создаем временный элемент ссылки
    const a = document.createElement('a');
    // Устанавливаем атрибуты ссылки
    a.href = url;
    a.download = 'file.txt'; // Имя файла для сохранения
    // Добавляем ссылку в документ
    document.body.appendChild(a);
    // Кликаем по ссылке
    a.click();
    // Удаляем ссылку из документа
    document.body.removeChild(a);
    // Очищаем URL объекта Blob
    window.URL.revokeObjectURL(url);
  };

  return (
    <button onClick={handleSaveToFile}>Сохранить в файл</button>
  );
};

export default SaveToFileButton;
