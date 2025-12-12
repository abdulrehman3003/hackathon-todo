import React from 'react';
import styles from './Loader.module.css';

function Loader({ size = 'medium', className = '' }) {
  const loaderClass = `${styles.loader} ${styles[size]} ${className}`;
  return <div className={loaderClass}></div>;
}

export default Loader;
