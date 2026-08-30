import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        manifesto: resolve(__dirname, 'manifesto.html'),
        apply: resolve(__dirname, 'apply.html'),
        success: resolve(__dirname, 'success.html'),
        privacy: resolve(__dirname, 'privacy.html'),
        honor: resolve(__dirname, 'honor.html')
      }
    }
  }
});
