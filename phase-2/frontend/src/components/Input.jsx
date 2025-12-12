import React, { useState } from 'react';
import styles from './Input.module.css';

function Input({ label, value, placeholder, type = 'text', error, onChange, className = '' }) {
  const [showPassword, setShowPassword] = useState(false);

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const inputType = type === 'password' && showPassword ? 'text' : type;
  const isTextArea = type === 'textarea';

  return (
    <div className={`${styles.inputGroup} ${className}`}>
      {label && <label htmlFor={label.toLowerCase()}>{label}</label>}
      <div className={styles.inputWrapper}>
        {isTextArea ? (
          <textarea
            id={label?.toLowerCase()}
            className={`${styles.input} ${styles.textarea} ${error ? styles.errorBorder : ''}`}
            value={value}
            placeholder={placeholder}
            onChange={onChange}
            aria-invalid={error ? 'true' : 'false'}
            aria-describedby={error ? `${label?.toLowerCase()}-error` : undefined}
          />
        ) : (
          <input
            id={label?.toLowerCase()}
            type={inputType}
            className={`${styles.input} ${error ? styles.errorBorder : ''}`}
            value={value}
            placeholder={placeholder}
            onChange={onChange}
            aria-invalid={error ? 'true' : 'false'}
            aria-describedby={error ? `${label?.toLowerCase()}-error` : undefined}
          />
        )}
        {type === 'password' && (
          <button
            type="button"
            className={styles.passwordToggle}
            onClick={togglePasswordVisibility}
            aria-label={showPassword ? 'Hide password' : 'Show password'}
          >
            {showPassword ? '🙈' : '👁️'}
          </button>
        )}
      </div>
      {error && <p id={`${label?.toLowerCase()}-error`} className={styles.errorMessage}>{error}</p>}
    </div>
  );
}

export default Input;
