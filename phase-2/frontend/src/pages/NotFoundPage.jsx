import React from 'react';
import { Link } from 'react-router-dom';
import '../../src/styles/layout.css'; // For layout styling
import '../../src/styles/global.css'; // For base styles

function NotFoundPage() {
  return (
    <div className="not-found-container">
      <h1>Page not found</h1>
      <p>We couldn't find that page.</p>
      <Link to="/" className="button primary">Go home</Link>
    </div>
  );
}

export default NotFoundPage;
