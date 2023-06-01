import { ref } from 'vue'
import provincesDataRaw from "../../../data/provincias.json"
import citiesDataRaw from "../../../data/localidades.json"

const provincesData = provincesDataRaw.provincias
const citiesData = citiesDataRaw.localidades
console.log(citiesData)
console.log(provincesData)

const ciudades = citiesData.map(ctemp => ctemp.nombre)
console.log(ciudades)

export function useTerritory() {
  const provinces = ref([])
  const cities = ref([])
  
  function getTerritories() {
    provinces.value = provincesData.map(p => ({ label: p.nombre, value: p.id }))
    cities.value = citiesData.filter(c => c.provinceId === 0).map(c => ({ label: c.nombre, value: c.id }))
  }
  
  function getProvinceCities(provinceId) {
    cities.value = citiesData.filter(c => c.provincia.id === provinceId).map(c => ({ label: c.nombre, value: c.id }))
  }
  
  getTerritories()

  return { provinces, cities, getProvinceCities }
}