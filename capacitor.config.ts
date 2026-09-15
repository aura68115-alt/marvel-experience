import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.marvelexperience.app',
  appName: 'Marvel Experience',
  webDir: '.',
  bundledWebRuntime: false,
  server: {
    androidScheme: 'https'
  }
};

export default config;
