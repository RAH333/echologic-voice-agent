// Dynamically fall back to localhost if the production cloud variable is not present
export const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';
