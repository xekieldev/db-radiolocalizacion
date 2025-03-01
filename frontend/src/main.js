import { createApp } from 'vue'
import { createPinia } from 'pinia'
import {
    plugin as formkitPlugin,
    defaultConfig as formkitDefaultConfig,
} from '@formkit/vue'
import App from './App.vue'
import router from './router'
import { Quasar, QTable } from 'quasar'

import 'quasar/dist/quasar.css' // Importar estilos

import './assets/main.css'
// @import 'quasar/src/css/variables.sass'; // Variables de Quasar

const pinia = createPinia()
const app = createApp(App)
app.use(Quasar, {
    plugins: {}, // import Quasar plugins and add here
})

app.use(pinia)
app.use(formkitPlugin, formkitDefaultConfig({ theme: 'genesis' }))
app.use(router)

app.mount('#app')
