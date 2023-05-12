import { createApp } from 'vue'
import {
    plugin as formkitPlugin,
    defaultConfig as formkitDefaultConfig,
} from '@formkit/vue'
import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App)

app.use(formkitPlugin, formkitDefaultConfig({ theme: 'genesis' }))
app.use(router)

app.mount('#app')
