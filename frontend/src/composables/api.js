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

    async function edit(id, data) {
        const caseOmit = ['unidadVinc', 'unidad']
        const payload = { ...data }
        Object.keys(data).forEach( key => { 
            if (typeof data[key] === 'string' || data[key] instanceof String)
                if (!caseOmit.includes(key))
                    payload[key] = data[key].toUpperCase()
        })
        loading.value = true
        const response = await axiosInstance.put(`/file/${id}/edit`, payload)
        loading.value = false
        return response && response.data 
    }
    
    async function getFile(id) {
        loading.value = true
        const response = await axiosInstance.get(`/file/${id}`)
        loading.value = false
        return response && response.data 
    }
   
    async function getAllTechnicians() {
        loading.value = true
        const response = await axiosInstance.get(`/technician/`)
        loading.value = false
        return response && response.data 
    }

    async function getTechnician(id) {
        loading.value = true
        const response = await axiosInstance.get(`/technician/${id}`)
        loading.value = false
        return response && response.data 
    }

    async function create_technician(data) {
        loading.value = true
        const response = await axiosInstance.post('/technician', data)
        loading.value = false
        return response && response.data 
    }
    async function delete_technician(id) {
        loading.value = true
        const response = await axiosInstance.delete(`/technician/${id}/delete_technician`)
        loading.value = false
        return response && response.data 
    }

    async function create_tech_measurement(id, data) {
        loading.value = true
        const response = await axiosInstance.post(`/file/${id}/create_tech_measurement`, data)
        loading.value = false
        return response && response.data 
    }

    async function getTechMeasurement(id) {
        loading.value = true
        const response = await axiosInstance.get(`/file/${id}/tech_measurement`)
        loading.value = false
        return response && response.data 
    }
    return {
        list,
        loading,
        getFile,
        create,
        edit,
        getAllTechnicians,
        getTechnician,
        delete_technician,
        create_technician,
        create_tech_measurement,
        getTechMeasurement,
    }
}