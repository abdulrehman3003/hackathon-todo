import React from 'react';
import styles from './TaskItem.module.css';
import Button from './Button';
import { formatDistanceToNow } from 'date-fns'; // Requires date-fns, will assume it's installed

function TaskItem({ task, onEdit, onDelete, onToggle }) {
  const timeAgo = task.created_at ? formatDistanceToNow(new Date(task.created_at), { addSuffix: true }) : '';

  return (
    <div className={styles.taskItem}>
      <div className={styles.taskContent}>
        <button
          className={`${styles.statusToggle} ${task.completed ? styles.completed : ''}`}
          onClick={() => onToggle(task.id)}
          aria-label={task.completed ? "Mark as pending" : "Mark as completed"}
        >
          {task.completed && '✔'}
        </button>
        <div className={styles.details}>
          <h4 className={task.completed ? styles.completedText : ''}>{task.title}</h4>
          {task.description && <p className={styles.description}>{task.description}</p>}
          <span className={styles.timeAgo}>Created {timeAgo}</span>
        </div>
      </div>
      <div className={styles.taskActions}>
        <Button variant="ghost" onClick={() => onEdit(task)} aria-label="Edit task">✏️</Button>
        <Button variant="ghost" onClick={() => onDelete(task.id)} aria-label="Delete task">🗑️</Button>
      </div>
    </div>
  );
}

export default TaskItem;
