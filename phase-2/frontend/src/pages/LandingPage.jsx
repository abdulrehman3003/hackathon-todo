import React from 'react';
import { Link } from 'react-router-dom';
import '../../src/styles/layout.css'; // For .container
import '../../src/styles/global.css'; // For base styles

// Placeholder for feature icons
const FeatureIcon = ({ children }) => (
  <div style={{ fontSize: '3rem', color: 'var(--primary)' }}>{children}</div>
);

const FeatureCard = ({ icon, title, description }) => (
  <div className="card feature-card">
    <FeatureIcon>{icon}</FeatureIcon>
    <h3>{title}</h3>
    <p>{description}</p>
  </div>
);

const Step = ({ icon, title, description }) => (
  <div className="step-item">
    <FeatureIcon>{icon}</FeatureIcon>
    <h4>{title}</h4>
    <p>{description}</p>
  </div>
);

function LandingPage() {
  return (
    <div className="landing-page">
      <header className="hero">
        <div className="container">
          <h1>Your tasks, perfectly simple.</h1>
          <p>Organize your life, boost productivity, and achieve your goals with ease. The ultimate task management solution.</p>
          <div className="hero-actions">
            <Link to="/signup" className="button primary">Get Started</Link>
            <Link to="/login" className="button ghost">Login</Link>
          </div>
        </div>
      </header>

      <section className="features-section">
        <div className="container">
          <h2>Features designed for you</h2>
          <div className="feature-cards-grid">
            <FeatureCard icon="🚀" title="Boost Productivity" description="Streamline your workflow and get more done efficiently." />
            <FeatureCard icon="📝" title="Stay Organized" description="Keep track of all your tasks in one intuitive place." />
            <FeatureCard icon="🎯" title="Achieve Goals" description="Break down big goals into manageable steps and track progress." />
          </div>
        </div>
      </section>

      <section className="how-it-works-section">
        <div className="container">
          <h2>How it works</h2>
          <div className="steps-grid">
            <Step icon="💡" title="Create Account" description="Sign up in seconds and start managing your tasks." />
            <Step icon="✅" title="Add Tasks" description="Quickly add, categorize, and prioritize your to-dos." />
            <Step icon="📈" title="Track Progress" description="Monitor your achievements and stay motivated." />
          </div>
        </div>
      </section>

      <footer className="footer">
        <div className="container">
          <p>
            &copy; {new Date().getFullYear()} Hackathon II Todo App.
            <a href="https://github.com/your-github" target="_blank" rel="noopener noreferrer" style={{ marginLeft: '10px' }}>GitHub</a>
            <a href="mailto:contact@example.com" style={{ marginLeft: '10px' }}>Contact</a>
          </p>
        </div>
      </footer>
    </div>
  );
}

export default LandingPage;
