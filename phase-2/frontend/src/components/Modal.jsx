import React, { useEffect, useRef } from 'react';
import ReactDOM from 'react-dom';
import styles from './Modal.module.css';

function Modal({ open, onClose, title, children }) {
  const modalRef = useRef();

  useEffect(() => {
    if (open) {
      document.body.style.overflow = 'hidden';
      // Trap focus inside modal
      const focusableElements = modalRef.current.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      const firstElement = focusableElements[0];
      const lastElement = focusableElements[focusableElements.length - 1];

      const handleTabKeyPress = (e) => {
        if (e.key === 'Tab') {
          if (e.shiftKey) { // if shift key pressed for shift + tab
            if (document.activeElement === firstElement) {
              lastElement.focus(); // add focus to the last focusable element
              e.preventDefault();
            }
          } else { // if tab key is pressed
            if (document.activeElement === lastElement) {
              firstElement.focus(); // add focus to the first focusable element
              e.preventDefault();
            }
          }
        }
      };

      modalRef.current.addEventListener('keydown', handleTabKeyPress);
      firstElement?.focus(); // Focus first element on open
      return () => {
        modalRef.current.removeEventListener('keydown', handleTabKeyPress);
      };

    } else {
      document.body.style.overflow = '';
    }

    const handleEscape = (e) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    document.addEventListener('keydown', handleEscape);
    return () => {
      document.removeEventListener('keydown', handleEscape);
      document.body.style.overflow = '';
    };
  }, [open, onClose]);

  if (!open) return null;

  return ReactDOM.createPortal(
    <div className={styles.modalOverlay} onClick={onClose}>
      <div className={styles.modalContent} onClick={(e) => e.stopPropagation()} ref={modalRef}>
        <div className={styles.modalHeader}>
          {title && <h3 className={styles.modalTitle}>{title}</h3>}
          <button className={styles.closeButton} onClick={onClose} aria-label="Close modal">
            &times;
          </button>
        </div>
        <div className={styles.modalBody}>
          {children}
        </div>
      </div>
    </div>,
    document.body
  );
}

export default Modal;
