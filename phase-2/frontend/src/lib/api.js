const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function fetchApi(endpoint, { body, ...customConfig } = {}) {
  const token = localStorage.getItem("todo_token");
  const headers = { "Content-Type": "application/json" };

  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }

  const config = {
    method: body ? "POST" : "GET",
    ...customConfig,
    headers: {
      ...headers,
      ...customConfig.headers,
    },
  };

  if (body) {
    config.body = JSON.stringify(body);
  }

  let data;
  try {
    const response = await window.fetch(`${API_BASE_URL}${endpoint}`, config);
    data = await response.json();
    if (response.ok) {
      return data;
    }
    // Handle specific error codes
    if (response.status === 401) {
        // unauthorized -> logout & redirect to /login, toast "Session expired"
        localStorage.removeItem("todo_token");
        window.location.href = "/login?session_expired=true";
    }
    throw { ...data, status: response.status }; // Throw structured error object
  } catch (err) {
    if (err instanceof TypeError) { // Network error or response.json() parsing error
      return Promise.reject({ message: "Network error or invalid server response.", code: "network_error", status: 500 });
    }
    // If 'data' was defined (meaning response.json() succeeded but response.ok was false)
    // then 'err' would be the structured error object we threw.
    // If 'data' was not defined, and it's not a TypeError, then 'err' is likely from 'fetch' itself.
    return Promise.reject(err.message ? err : { message: err.message || "An unexpected error occurred.", code: "unexpected_error", status: 500 });
  }
}

export default fetchApi;
