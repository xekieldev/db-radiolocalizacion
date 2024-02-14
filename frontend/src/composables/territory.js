import { ref } from 'vue'
import provincesDataRaw from "../../../data/provincias.json"
import citiesDataRaw from "../../../data/localidades.json"

const provincesData = provincesDataRaw.provincias
const citiesData = citiesDataRaw.localidades

export function useTerritory() {
  const provinces = ref([])
  const cities = ref([])
  
  function getTerritories() {
    provinces.value = provincesData.map(p => ({ label: p.nombre.toUpperCase(), value: p.id }))
    cities.value = citiesData.map(c => ({ label: c.nombre, value: c.id }))
  }

  function getProvinceCities(provinceId) {
    cities.value = citiesData.filter(c => c.provincia.id === provinceId).map(c => ({ label: c.nombre, value: c.id , province: c.provincia.id }))
  }

  function getNameByCode(kind, code){
    const data = kind === "city" ? citiesData : provincesData
    return data.find(x => x.id === code).nombre.toUpperCase()
  }
  
  getTerritories()

  return { provinces, cities, getProvinceCities, getNameByCode }
  
}
