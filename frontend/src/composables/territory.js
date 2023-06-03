import { ref } from 'vue'
import provincesDataRaw from "../../../data/provincias.json"
import citiesDataRaw from "../../../data/localidades.json"

function capitalizeWords(str) {
  return str
      .toLowerCase()
      .split(' ')
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ')
}



const provincesData = provincesDataRaw.provincias
const citiesData = citiesDataRaw.localidades
// console.log(citiesData.map(capitalizeWords(citiesData.nombre)))

// const e = "HOLA"
// console.log(capitalizeWords(e))
// console.log(citiesData)
// console.log(provincesData)

export function useTerritory() {
  const provinces = ref([])
  const cities = ref([])
  
  function getTerritories() {
    provinces.value = provincesData.map(p => ({ label: p.nombre.toUpperCase(), value: p.id }))
    cities.value = citiesData.filter(c => c.provincia.id === "54").map(c => ({ label: c.nombre, value: c.id }))
  }
  
  function getProvinceCities(provinceId) {
    cities.value = citiesData.filter(c => c.provincia.id === provinceId).map(c => ({ label: c.nombre, value: c.id }))
  }
  
  getTerritories()

  return { provinces, cities, getProvinceCities }
}