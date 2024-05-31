import axios from 'axios'
import { ref } from 'vue'



export function useApi() {
    var loading = ref(false);
    const axiosInstance = axios.create({
        baseURL: import.meta.env.VITE_APP_API_URL,
        headers: { Authorization: `Basic ${document.cookie.split('appAuth=')[1]}`}
    })

    async function list(includeDeleted = false) {
        loading.value = true
        const response = await axiosInstance.get('/file', {
            params: {
                includeDeleted: includeDeleted
            }
        })
        loading.value = false
        return response && response.data 
    }

    async function create(data, rloc = true) {
        loading.value = true
        const response = await axiosInstance.post('/file', data, {
            params: {
                rloc: rloc
            }
        })
        loading.value = false
        return response && response.data 
    }

    async function edit(id, data) {
        loading.value = true
        const response = await axiosInstance.put(`/file/${id}/edit`, data)
        loading.value = false
        return response && response.data 

    }
    
    async function getFile(id) {
        loading.value = true
        const response = await axiosInstance.get(`/file/${id}`)
        loading.value = false
        return response && response.data 
    }

    async function deleteFile(id) {
        loading.value = true
        const response = await axiosInstance.delete(`/file/${id}`)
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

    async function listStations(includeDeleted = false) {
        loading.value = true
        const response = await axiosInstance.get('/station', {
            params: {
                includeDeleted: includeDeleted
            }
        })
        loading.value = false
        return response && response.data 
    }

    async function getStation(id) {
        loading.value = true
        const response = await axiosInstance.get(`/station/${id}`)
        loading.value = false
        return response && response.data 
    }
    async function updateRelatedStation(id, relatedStationId) {
        loading.value = true
        const response = await axiosInstance.put(`/file/${id}`, 
            {
                related_station_id: relatedStationId
            })
        loading.value = false
        return response && response.data
    }

    return {
        list,
        loading,
        getFile,
        deleteFile,
        create,
        edit,
        getAllTechnicians,
        getTechnician,
        delete_technician,
        create_technician,
        create_tech_measurement,
        getTechMeasurement,
        listStations,
        getStation,
        updateRelatedStation,
    }
}