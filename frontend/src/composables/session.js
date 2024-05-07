import axios from 'axios'
import { ref } from 'vue'


export function useSession() {
    const loading = ref(false);
    const loggedIn = ref(document.cookie.indexOf('Auth') !== -1);

    const loginAxiosInstance = axios.create({
        baseURL: import.meta.env.VITE_APP_API_URL
    })

    function updateLoggedIn() {
        loggedIn.value = document.cookie.indexOf('Auth') !== -1
    }

    async function login(data) {
        loading.value = true
        const response = await loginAxiosInstance.post('/login',data)
        loading.value = false
        const fechaActual = new Date()
        const expirationDate = new Date(fechaActual.getTime() + (30 * 60 * 1000))
        const expirationDateGMT = expirationDate.toGMTString()
        document.cookie = `appAuth=${response.data}; expires=${expirationDateGMT};samesite=lax`
        return response && response.data
    }

    async function logout() {
        document.cookie = 'appAuth=; expires=Thu, 01 Jan 1970 00:00:00 UTC;samesite=lax' 
      }

      return {
        login,
        logout,
        loggedIn,
        updateLoggedIn,
        
    }
}