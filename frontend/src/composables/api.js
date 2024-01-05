import axios from 'axios'
import { ref } from 'vue'

export function useApi() {
    var loading = ref(false);
    const axiosInstance = axios.create({
        baseURL: 'http://127.0.0.1:5000',
    })

    async function list() {
        loading.value = true
        const response = await axiosInstance.get('/file?includeDeleted=true')
        loading.value = false
        return response && response.data 
    }

    async function create(data) {
        loading.value = true
        const response = await axiosInstance.post('/file', data)
        loading.value = false
        return response && response.data 
    }
    
    async function getFile(id) {
        loading.value = true
        const response = await axiosInstance.get(`/file/${id}`)
        loading.value = false
        return response && response.data 
    }
    async function getStation(id) {
        loading.value = true
        const response = await axiosInstance.get(`/technician/${id}`)
        loading.value = false
        return response && response.data 
    }
    return {
        list,
        loading,
        getFile,
        getStation,
        create,
    }
}