import React, { useState, useEffect } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useToast } from '../context/ToastContext';
import Input from '../components/Input';
import Button from '../components/Button';
import Card from '../components/Card';
import '../../src/styles/layout.css'; // For auth-card-layout
import '../../src/styles/global.css'; // For base styles

function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});
  const { login, isAuthenticated, loading } = useAuth();
  const { addToast } = useToast();
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  useEffect(() => {
    if (isAuthenticated) {
      navigate('/dashboard');
    }
    if (searchParams.get('session_expired')) {
        addToast('Your session has expired. Please log in again.', 'info');
    }
  }, [isAuthenticated, navigate, searchParams, addToast]);

  const validate = () => {
    const newErrors = {};
    if (!email) newErrors.email = 'Email is required';
    if (!password) newErrors.password = 'Password is required';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validate()) return;

    const success = await login(email, password);
    if (!success) {
      // Errors handled by useAuth and toast context
    }
  };

  return (
    <div className="auth-card-layout">
      <Card>
        <h2>Log in</h2>
        <form onSubmit={handleSubmit}>
          <Input
            label="Email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            error={errors.email}
          />
          <Input
            label="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            error={errors.password}
          />
          <Button type="submit" variant="primary" disabled={loading} loading={loading}>
            Log In
          </Button>
        </form>
        <p className="auth-link-text">
          Don't have an account? <Link to="/signup">Sign up</Link>
        </p>
      </Card>
    </div>
  );
}

export default LoginPage;
