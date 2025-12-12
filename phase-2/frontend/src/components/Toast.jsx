import React, { useEffect, useState } from 'react';
import styles from './Toast.module.css';

function Toast({ message, type, onClose }) {
  const [exiting, setExiting] = useState(false);

  useEffect(() => {
    // Start exit animation before closing
    const timer = setTimeout(() => {
      setExiting(true);
      const closeTimer = setTimeout(onClose, 300); // Match animation duration
      return () => clearTimeout(closeTimer);
    }, 2700); // 3s total duration (300ms for exit animation)

    return () => clearTimeout(timer);
  }, [onClose]);

  const toastClass = `${styles.toast} ${styles[type]} ${exiting ? styles.exiting : ''}`;

  return (
    <div className={toastClass} role="alert">
      <span>{message}</span>
      <button onClick={() => { setExiting(true); setTimeout(onClose, 300); }} className={styles.closeButton}>
        &times;
      </button>
    </div>
  );
}

export default Toast;
