import React, { useState, useEffect, useCallback } from 'react';
import { useAuth } from '../context/AuthContext';
import { useToast } from '../context/ToastContext';
import fetchApi from '../lib/api';
import Navbar from '../components/Navbar';
import Sidebar from '../components/Sidebar';
import Card from '../components/Card';
import TaskList from '../components/TaskList';
import Modal from '../components/Modal';
import Input from '../components/Input';
import Button from '../components/Button';
import Loader from '../components/Loader';
import '../../src/styles/layout.css';
import '../../src/styles/global.css';

function DashboardPage() {
  const { user, setUser, logout, isAuthenticated } = useAuth();
  const { addToast } = useToast();
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentTask, setCurrentTask] = useState(null); // For edit mode
  const [taskForm, setTaskForm] = useState({ title: '', description: '' });
  const [formErrors, setFormErrors] = useState({});
  const [filter, setFilter] = useState('all'); // all, pending, completed
  const [searchTerm, setSearchTerm] = useState('');

  const fetchTasks = useCallback(async () => {
    setLoading(true);
    try {
      const queryParams = new URLSearchParams();
      if (filter !== 'all') queryParams.append('status', filter);
      if (searchTerm) queryParams.append('q', searchTerm);

      const data = await fetchApi(`/tasks?${queryParams.toString()}`);
      setTasks(data.data);
      // Assuming the user email might be in the token, or fetched from a /me endpoint
      if (isAuthenticated && !user?.email) {
        // Placeholder, ideally fetch /me for full user profile
        setUser(prev => ({ ...prev, email: 'user@example.com' })); // Replace with actual email from token or /me
      }
    } catch (error) {
      addToast(error.detail || 'Failed to fetch tasks', 'error');
      console.error('Fetch tasks error:', error);
    } finally {
      setLoading(false);
    }
  }, [filter, searchTerm, addToast, isAuthenticated, user?.email, setUser]);

  useEffect(() => {
    fetchTasks();
  }, [fetchTasks]);

  const handleAddTask = () => {
    setCurrentTask(null);
    setTaskForm({ title: '', description: '' });
    setFormErrors({});
    setIsModalOpen(true);
  };

  const handleEditTask = (task) => {
    setCurrentTask(task);
    setTaskForm({ title: task.title, description: task.description });
    setFormErrors({});
    setIsModalOpen(true);
  };

  const validateForm = () => {
    const newErrors = {};
    if (!taskForm.title) newErrors.title = 'Title is required';
    else if (taskForm.title.length > 200) newErrors.title = 'Title cannot exceed 200 characters';
    if (taskForm.description && taskForm.description.length > 2000) newErrors.description = 'Description cannot exceed 2000 characters';
    setFormErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmitTask = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    try {
      if (currentTask) {
        // Update task
        await fetchApi(`/tasks/${currentTask.id}`, {
          method: 'PUT',
          body: { ...taskForm, completed: currentTask.completed }, // Retain original completion status
        });
        addToast('Task updated successfully!', 'success');
      } else {
        // Create task
        await fetchApi('/tasks', { method: 'POST', body: taskForm });
        addToast('Task created successfully!', 'success');
      }
      setIsModalOpen(false);
      fetchTasks(); // Refresh tasks
    } catch (error) {
      addToast(error.detail || 'Failed to save task', 'error');
      console.error('Save task error:', error);
    }
  };

  const handleDeleteTask = async (id) => {
    if (!window.confirm('Are you sure you want to delete this task?')) return;
    try {
      await fetchApi(`/tasks/${id}`, { method: 'DELETE' });
      addToast('Task deleted successfully!', 'success');
      fetchTasks(); // Refresh tasks
    } catch (error) {
      addToast(error.detail || 'Failed to delete task', 'error');
      console.error('Delete task error:', error);
    }
  };

  const handleToggleCompletion = async (id) => {
    try {
      await fetchApi(`/tasks/${id}/toggle`, { method: 'PATCH' });
      addToast('Task status updated!', 'success');
      fetchTasks(); // Refresh tasks
    } catch (error) {
      addToast(error.detail || 'Failed to update task status', 'error');
      console.error('Toggle task error:', error);
    }
  };

  return (
    <div className="dashboard-layout">
      <Sidebar onFilterChange={setFilter} currentFilter={filter} />
      <div className="main-content">
        <Navbar userEmail={user?.email || 'Loading...'} onLogout={logout} onAddTask={handleAddTask} />
        <div className="dashboard-header">
          <h1>Dashboard</h1>
          <Input
            placeholder="Search tasks..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            type="search"
            style={{ width: '300px' }}
          />
        </div>

        <div className="stats-row">
            <Card><h3>Total Tasks</h3><p>{tasks.length}</p></Card>
            <Card><h3>Completed</h3><p>{tasks.filter(t => t.completed).length}</p></Card>
            <Card><h3>Pending</h3><p>{tasks.filter(t => !t.completed).length}</p></Card>
        </div>

        {loading ? (
          <Loader />
        ) : (
          <TaskList
            tasks={tasks}
            onEdit={handleEditTask}
            onDelete={handleDeleteTask}
            onToggle={handleToggleCompletion}
          />
        )}
      </div>

      <Modal
        open={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        title={currentTask ? 'Edit Task' : 'Add New Task'}
      >
        <form onSubmit={handleSubmitTask}>
          <Input
            label="Title"
            value={taskForm.title}
            onChange={(e) => setTaskForm({ ...taskForm, title: e.target.value })}
            error={formErrors.title}
          />
          <Input
            label="Description"
            type="textarea"
            value={taskForm.description}
            onChange={(e) => setTaskForm({ ...taskForm, description: e.target.value })}
            error={formErrors.description}
          />
          <Button type="submit" variant="primary">
            {currentTask ? 'Save Changes' : 'Create Task'}
          </Button>
        </form>
      </Modal>

      {/* Floating Add Task button for mobile */}
      <Button variant="primary" className="add-task-fab" onClick={handleAddTask}>
        +
      </Button>
    </div>
  );
}

export default DashboardPage;
