import { createContext, useContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import fetchApi from '../lib/api';
import { useToast } from '../context/ToastContext';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('todo_token'));
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  const { addToast } = useToast();

  useEffect(() => {
    const loadUser = async () => {
      if (token) {
        // In a real app, you'd verify the token with the backend
        // For this hackathon, we'll just assume a valid token means logged in
        // and fetch user details if needed, or decode the token locally for basic info
        setLoading(false);
        // Placeholder for user data. Actual user data should come from token or /me endpoint
        try {
            // For now, let's assume if token exists, user is logged in.
            // A /me endpoint would be ideal to fetch user details.
            // If we decode JWT, we can get email/sub from it
            // For now, setting a dummy user for display purposes
            setUser({ email: "Loading..." }); // Will be updated on Dashboard fetch
        } catch (error) {
            console.error("Error loading user from token:", error);
            localStorage.removeItem('todo_token');
            setToken(null);
            setUser(null);
            navigate('/login?session_expired=true');
        }
      } else {
        setLoading(false);
      }
    };
    loadUser();
  }, [token, navigate]);

  const login = async (email, password) => {
    setLoading(true);
    try {
      const data = await fetchApi('/auth/login', { body: { email, password }, method: 'POST' });
      localStorage.setItem('todo_token', data.access_token);
      setToken(data.access_token);
      setUser({ email: email }); // Set initial user, dashboard will fetch full details
      navigate('/dashboard');
      addToast('Login successful!', 'success');
      return true;
    } catch (error) {
      addToast(error.detail || 'Login failed', 'error');
      console.error('Login error:', error);
      return false;
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    localStorage.removeItem('todo_token');
    setToken(null);
    setUser(null);
    navigate('/login');
    addToast('Logged out successfully.', 'info');
  };

  const value = {
    user,
    token,
    isAuthenticated: !!token,
    loading,
    login,
    logout,
    setUser, // Allows setting user details from dashboard
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  return useContext(AuthContext);
};
