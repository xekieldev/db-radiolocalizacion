import axios from 'axios'

export function useApi() {
    const axiosInstance = axios.create({
        baseURL: 'http://127.0.0.1:5000',
    })

    function create(fields) {
        return axiosInstance.post('/tramites', { fecha: fields.fecha.replaceAll('-', '/') })
    }
    
    function list() {
        return axiosInstance.get('/tramites')
    }

    return {
        create,
        list,
    }
}