import React from 'react';
import { Link } from 'react-router-dom';
import Button from './Button';
import styles from './Navbar.module.css';

function Navbar({ userEmail, onLogout, onAddTask }) {
  return (
    <nav className={styles.navbar}>
      <Link to="/" className={styles.appTitle}>Todo App</Link>
      <div className={styles.rightSection}>
        {userEmail && <span className={styles.userEmail}>{userEmail}</span>}
        <Button onClick={onAddTask} variant="primary" className={styles.addTaskButton}>Add Task</Button>
        <Button onClick={onLogout} variant="ghost">Logout</Button>
      </div>
    </nav>
  );
}

export default Navbar;
