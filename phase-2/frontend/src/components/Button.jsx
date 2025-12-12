import React from 'react';
import styles from './Button.module.css';
import Loader from './Loader'; // Assuming Loader component exists

function Button({ children, variant = 'primary', disabled, loading, onClick, type = 'button', className = '' }) {
  const buttonClass = `${styles.button} ${styles[variant]} ${className}`;

  return (
    <button
      type={type}
      className={buttonClass}
      onClick={onClick}
      disabled={disabled || loading}
    >
      {loading ? <Loader size="small" /> : children}
    </button>
  );
}

export default Button;
