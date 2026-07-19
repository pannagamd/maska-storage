/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_BASE_URL: string;
  readonly VITE_API_VERSION: string;
  readonly VITE_API_TIMEOUT_MS: string;
  readonly VITE_APP_NAME: string;
  readonly VITE_APP_VERSION: string;
  readonly VITE_APP_ENV: string;
  readonly VITE_ENABLE_CHAT: string;
  readonly VITE_ENABLE_ARCHIVE: string;
  readonly VITE_ENABLE_UPLOAD: string;
  readonly VITE_MAX_UPLOAD_SIZE_MB: string;
  readonly VITE_ALLOWED_FILE_TYPES: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
