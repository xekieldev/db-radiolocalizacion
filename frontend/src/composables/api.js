import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { loggedIn } from './loginstatus';


export function useApi() {
    const router = useRouter()
    var loading = ref(false);    
    const axiosInstance = axios.create({
        baseURL: import.meta.env.VITE_APP_API_URL,
        withCredentials: true,
        xsrfCookieName: 'csrf_access_token'
    })

    axiosInstance.interceptors.response.use(
        response => response, // Si la respuesta es exitosa, la retorna sin cambios
        error => {
            if (error.response && error.response.status === 401) {
                loggedIn.value = false                
                router.push({ name: 'login' }) // Redirige al login si hay un 401
            }
            return Promise.reject(error)
        }
    )

    async function list(includeDeleted = false, fileStatus) {
        loading.value = true
        const response = await axiosInstance.get('/file', {
            params: {
                fileStatus: fileStatus,
                includeDeleted: includeDeleted,
            },
        })
        loading.value = false
        return response && response.data 
    }

    async function newFile(data) {
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

    async function editFile(id, data) {
        loading.value = true
        const response = await axiosInstance.put(`/file/${id}`, data)
        loading.value = false
        return response && response.data 
    }

    async function patchFile(file_id, data) {
        loading.value = true
        const response = await axiosInstance.patch(`/file/${file_id}`, data)
        loading.value = false
        return response && response.data 
    }

    async function deleteFile(id) {
        loading.value = true
        const response = await axiosInstance.delete(`/file/${id}`)
        loading.value = false
        return response && response.data
    }
    
    async function create(id, data, rloc = true) {
        loading.value = true
        const response = await axiosInstance.post(`/file/${id}/station`, data, {
            params: {
                rloc: rloc
            }
        })
        loading.value = false
        return response && response.data 
    }

    async function edit(file_id, id, data) {
        loading.value = true
        const response = await axiosInstance.put(`/file/${file_id}/station/${id}/edit`, data)
        loading.value = false
        return response && response.data 

    }
    
    async function getStation(id) {
        loading.value = true
        const response = await axiosInstance.get(`/station/${id}`)
        loading.value = false
        return response && response.data 
    }

    async function deleteStation(file_id, id) {
        loading.value = true
        const response = await axiosInstance.delete(`/file/${file_id}/station/${id}`)
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

    async function create_tech_measurement(file_id, id, data) {
        loading.value = true
        const response = await axiosInstance.post(`/file/${file_id}/station/${id}/create_tech_measurement`, data)
        loading.value = false
        return response && response.data 
    }

    async function getTechMeasurement(file_id, id, includeDeleted = false) {
        loading.value = true
        const response = await axiosInstance.get(`/file/${file_id}/station/${id}/tech_measurement`, {
            params: {
                includeDeleted: includeDeleted
            }
        })
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

    async function stationsPerFile(file_id) {
        loading.value = true
        const response = await axiosInstance.get(`/file/${file_id}/stations`, {
            file_id: file_id
        })
        loading.value = false
        return response && response.data 
    }

    async function updateRelatedStation(file_id, id, relatedStationId) {
        loading.value = true
        const response = await axiosInstance.put(`/file/${file_id}/station/${id}`, 
            {
                related_station_id: relatedStationId
            })
        loading.value = false
        return response && response.data
    }

    async function delete_tech_measurement(file_id, id, id_tech_measurement) {
        loading.value = true
        const response = await axiosInstance.delete(`/file/${file_id}/station/${id}/delete_tech_measurement/${id_tech_measurement}`)
        loading.value = false
        return response && response.data 
    }
    async function getAllNonIonizingRadiation() {
        loading.value = true
        const response = await axiosInstance.get(`/non_ionizing_radiation/`)
        loading.value = false
        return response && response.data 
    }

    async function getNonIonizingRadiation(id) {
        loading.value = true
        const response = await axiosInstance.get(`/non_ionizing_radiation/${id}`)
        loading.value = false
        return response && response.data 
    }

    async function getNIRMeasurementInFile(file_id) {
        loading.value = true
        const response = await axiosInstance.get(`/file/${file_id}/non_ionizing_radiation`)
        loading.value = false
        return response && response.data 
    }

    async function create_non_ionizing_radiation(id, data) {
        loading.value = true
        const response = await axiosInstance.post(`/file/${id}/non_ionizing_radiation`, data)
        loading.value = false
        return response && response.data 
    }
    async function delete_nir_measurement(id) {
        loading.value = true
        const response = await axiosInstance.delete(`/non_ionizing_radiation/${id}/delete_non_ionizing_radiation`)
        loading.value = false
        return response && response.data 
    }

    async function newActivity(file_id, data) {
        loading.value = true
        const response = await axiosInstance.post(`/file/${file_id}/activity`, data)
        loading.value = false
        return response && response.data 
    }

    async function getActivities(file_id) {
        loading.value = true
        const response = await axiosInstance.get(`/file/${file_id}/activities`)
        loading.value = false
        return response && response.data 
    }

    async function getStatistics(startDate, endDate, type, area) {
        loading.value = true
        
        const response = await axiosInstance.get(`/statistics`, {
            params: {
                startDate: startDate,
                endDate: endDate,
                type : type,
                area: area,
                
            }
        })
        loading.value = false
        return response && response.data 
    }

    return {
        list,
        newFile,
        getFile,
        editFile,
        deleteFile,
        patchFile,
        loading,
        getStation,
        deleteStation,
        create,
        edit,
        getAllTechnicians,
        getTechnician,
        delete_technician,
        create_technician,
        create_tech_measurement,
        getTechMeasurement,
        listStations,
        stationsPerFile,
        updateRelatedStation,
        delete_tech_measurement,
        getAllNonIonizingRadiation,
        getNonIonizingRadiation,
        create_non_ionizing_radiation,
        delete_nir_measurement,
        getNIRMeasurementInFile,
        newActivity,
        getActivities,
        getStatistics,
    }
}