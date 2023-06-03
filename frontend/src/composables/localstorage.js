import { ref } from 'vue'
const LOCAL_STORAGE_KEY = 'mykey'

export function useLocalStorage(delay=0) {
  var loading = ref(false);

  /**
  * Returns a promise that resolves after the amount of milliseconds from the
  * 'ms' paramter
  */
  function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  /**
  * Returns a promise that resolves to the value from the 'value' paramter
  * after waiting the time from the 'delay' parameter
  */
  function resolveWithDelay(value) {
    return wait(delay).then(() => {
      loading.value = false
      return Promise.resolve(value)
    })
  }

  /**
  * Returns a rejected promise with the value from the 'value' paramter
  * after waiting the time from the 'delay' parameter
  */
  function rejectWithDelay(value) {
    return wait(delay).then(() => {
      loading.value = false
      return Promise.reject(value)
    })
  }

  /**
  * Returns the full list of items from localstorage
  */
  function getCurrentData() {
    const db = window.localStorage.getItem(LOCAL_STORAGE_KEY)
    return db === null ? [] : JSON.parse(db)
  }

  /**
  * Adds an item to the local storage and returns a promise
  */
  function create(item) {
    // Before even star processing, set loading to true
    loading.value = true
    
    try {
      const currentData = getCurrentData()
      const newData = [...currentData, item]
      window.localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(newData))
      return resolveWithDelay(newData)
    } catch (error) {
      return rejectWithDelay({ error: 'Local storage error' })
    }
  }
  
  /**
  * Returns the full list of items from localstorage with a resolved promise
  */
  function list() {
    loading.value = true
     try {
      return resolveWithDelay(getCurrentData())
    } catch (error) {
      return rejectWithDelay({ error: 'Local storage error' })
    } 
  }
  
  return { create, list, loading }
}