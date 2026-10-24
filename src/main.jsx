import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';
import FounderProfile from './components/FounderProfile.jsx';
import './index.css';

const page = window.location.pathname.replace(/\/+$/, '') === '/about-amos'
  ? <FounderProfile />
  : <App />;

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {page}
  </React.StrictMode>,
);
