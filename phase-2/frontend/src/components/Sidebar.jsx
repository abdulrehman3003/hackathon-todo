import React from 'react';
import { NavLink } from 'react-router-dom';
import styles from './Sidebar.module.css';
import Button from './Button';
import { useAuth } from '../context/AuthContext';

function Sidebar({ onFilterChange, currentFilter }) {
  const { logout } = useAuth();

  return (
    <aside className={styles.sidebar}>
      <h2 className={styles.logo}>Todo App</h2>
      <nav>
        <ul>
          <li>
            <NavLink
              to="/dashboard"
              className={({ isActive }) =>
                isActive && currentFilter === 'all' ? `${styles.active} ${styles.navItem}` : styles.navItem
              }
              onClick={() => onFilterChange('all')}
            >
              Dashboard
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/dashboard?status=pending"
              className={({ isActive }) =>
                isActive || currentFilter === 'pending' ? `${styles.active} ${styles.navItem}` : styles.navItem
              }
              onClick={() => onFilterChange('pending')}
            >
              Pending
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/dashboard?status=completed"
              className={({ isActive }) =>
                isActive || currentFilter === 'completed' ? `${styles.active} ${styles.navItem}` : styles.navItem
              }
              onClick={() => onFilterChange('completed')}
            >
              Completed
            </NavLink>
          </li>
          <li>
            <Button variant="ghost" onClick={logout} className={styles.logoutButton}>
              Logout
            </Button>
          </li>
        </ul>
      </nav>
    </aside>
  );
}

export default Sidebar;
