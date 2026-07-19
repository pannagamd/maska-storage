/**
 * MaskaStorage — Axios API Client
 * =================================
 * Configures a pre-built Axios instance with:
 * - Base URL + version prefix
 * - Request / response interceptors
 * - Standardised error handling
 *
 * All service modules import this client — never create Axios instances inline.
 */

import axios, { AxiosInstance, AxiosError, InternalAxiosRequestConfig } from "axios";
import { API_PREFIX, API_TIMEOUT_MS } from "../constants";
import type { ApiError } from "../types";

// ─── Create Axios Instance ─────────────────────────────────────────────────
const apiClient: AxiosInstance = axios.create({
  baseURL: API_PREFIX,
  timeout: API_TIMEOUT_MS,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

// ─── Request Interceptor ──────────────────────────────────────────────────
apiClient.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // TODO: Attach auth token from store/context when auth is implemented
    // const token = getAuthToken();
    // if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
  },
  (error: AxiosError) => Promise.reject(error),
);

// ─── Response Interceptor ─────────────────────────────────────────────────
apiClient.interceptors.response.use(
  (response) => response,
  (error: AxiosError<ApiError>) => {
    // Normalise server error into a consistent shape
    const serverError = error.response?.data;
    const message =
      serverError?.detail ?? error.message ?? "An unexpected error occurred.";

    // TODO: Dispatch to a global toast/notification system
    console.error(`[API Error] ${error.response?.status ?? "NETWORK"}: ${message}`);

    return Promise.reject(error);
  },
);

export default apiClient;
