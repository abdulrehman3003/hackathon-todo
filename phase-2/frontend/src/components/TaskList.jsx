import React from 'react';
import styles from './TaskList.module.css';
import TaskItem from './TaskItem';

function TaskList({ tasks, onEdit, onDelete, onToggle }) {
  if (tasks.length === 0) {
    return (
      <div className={styles.emptyState}>
        <p>No tasks yet! Add a new task to get started.</p>
        {/* Potentially add a button here to add task */}
      </div>
    );
  }

  return (
    <div className={styles.taskList}>
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          onEdit={onEdit}
          onDelete={onDelete}
          onToggle={onToggle}
        />
      ))}
    </div>
  );
}

export default TaskList;
