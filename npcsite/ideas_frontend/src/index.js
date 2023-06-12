import React from 'react';
import { createRoot } from 'react-dom/client';
import { IdeasApp } from './components/IdeasApp';


const container = document.getElementById('react-app');
const root = createRoot(container); // createRoot(container!) if you use TypeScript
root.render(<IdeasApp />);