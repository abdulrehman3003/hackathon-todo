import React, { createContext, useContext, useState, useCallback } from 'react';
import ReactDOM from 'react-dom';
import Toast from '../components/Toast'; // Assuming Toast component path

const ToastContext = createContext(null);

export const ToastProvider = ({ children }) => {
  const [toasts, setToasts] = useState([]);
  const toastId = React.useRef(0);

  const addToast = useCallback((message, type = 'info', duration = 3000) => {
    const id = toastId.current++;
    setToasts((prevToasts) => {
      const newToasts = [...prevToasts, { id, message, type }];
      // Stack up to 4 toasts
      if (newToasts.length > 4) {
        return newToasts.slice(newToasts.length - 4);
      }
      return newToasts;
    });

    setTimeout(() => {
      removeToast(id);
    }, duration);
  }, []);

  const removeToast = useCallback((id) => {
    setToasts((prevToasts) => prevToasts.filter((toast) => toast.id !== id));
  }, []);

  const value = {
    addToast,
  };

  return (
    <ToastContext.Provider value={value}>
      {children}
      {ReactDOM.createPortal(
        <div style={{
          position: 'fixed',
          bottom: 'var(--gap)',
          right: 'var(--gap)',
          zIndex: 1000,
          display: 'flex',
          flexDirection: 'column',
          gap: 'var(--gap, 16px)'
        }}>
          {toasts.map((toast) => (
            <Toast
              key={toast.id}
              message={toast.message}
              type={toast.type}
              onClose={() => removeToast(toast.id)}
            />
          ))}
        </div>,
        document.body
      )}
    </ToastContext.Provider>
  );
};

export const useToast = () => {
  const context = useContext(ToastContext);
  if (!context) {
    throw new Error('useToast must be used within a ToastProvider');
  }
  return context;
};
