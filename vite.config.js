import { defineConfig } from 'vite';
import { resolve } from 'path';
import htmlInject from 'vite-plugin-html-inject';

export default defineConfig({
  plugins: [htmlInject()],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        manifesto: resolve(__dirname, 'manifesto.html'),
        apply: resolve(__dirname, 'apply.html'),
        success: resolve(__dirname, 'success.html'),
        privacy: resolve(__dirname, 'privacy.html'),
        honor: resolve(__dirname, 'honor.html'),
        shop: resolve(__dirname, 'shop.html'),
        'research/index': resolve(__dirname, 'research/index.html'),
        'research/papers/competence': resolve(__dirname, 'research/papers/competence.html'),
        'research/papers/rapport': resolve(__dirname, 'research/papers/rapport.html'),
        'research/insights/voices-not-voicemail': resolve(__dirname, 'research/insights/voices-not-voicemail.html'),
        'research/insights/carer-retention': resolve(__dirname, 'research/insights/carer-retention.html'),
        'research/insights/the-layers-pitch': resolve(__dirname, 'research/insights/the-layers-pitch.html'),
        
        // Flowstate Beta
        'flowstatebeta/index': resolve(__dirname, 'flowstatebeta/index.html'),
        'flowstatebeta/book-a-demo': resolve(__dirname, 'flowstatebeta/book-a-demo.html'),
        'flowstatebeta/sales': resolve(__dirname, 'flowstatebeta/sales.html'),
        'flowstatebeta/gateway/index': resolve(__dirname, 'flowstatebeta/gateway/index.html'),
        'flowstatebeta/pricing/index': resolve(__dirname, 'flowstatebeta/pricing/index.html'),
        'flowstatebeta/compliance/index': resolve(__dirname, 'flowstatebeta/compliance/index.html'),
        'flowstatebeta/agents/index': resolve(__dirname, 'flowstatebeta/agents/index.html'),
        'flowstatebeta/agents/dialogue/index': resolve(__dirname, 'flowstatebeta/agents/dialogue/index.html'),
        'flowstatebeta/agents/runners/index': resolve(__dirname, 'flowstatebeta/agents/runners/index.html')
      }
    }
  }
});
