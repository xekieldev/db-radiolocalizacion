import axios from 'axios'
import { ref } from 'vue'
import { loggedIn, userData } from '../composables/loginstatus'

export function useSession() {
    const loading = ref(false)

    const loginAxiosInstance = axios.create({
        baseURL: import.meta.env.VITE_APP_API_URL,
        withCredentials: true,
        xsrfCookieName:'csrf_access_token'
    })

    async function login(data) {
        loading.value = true
        const response = await loginAxiosInstance.post('/login',data)
        if (response.status === 201) {
            loggedIn.value = true
            const response_user = await loginAxiosInstance.get('/check_user')
            userData.value = response_user.data            
        }
        return response && response.data
    }

    async function changePassword(data) {
        loading.value = true
        const response = await loginAxiosInstance.patch('/change_password', data)
        loading.value = false
        return response && response.data
    }

    async function logout() {
        loading.value = true        
        const response = await loginAxiosInstance.post('/logout')
        if (response.status === 200) {
            loggedIn.value = false
        }
        loading.value = false
        return response
      }

      return {
        login,
        logout,
        loggedIn,
        changePassword,
        userData,
        
    }
}