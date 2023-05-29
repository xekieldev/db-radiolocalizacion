export function useLocalStorage() {
   const localStorageKey = 'rlocdb'


    function create(data) {
        // debugger
        const db = localStorage.getItem(localStorageKey)
        if (db === null) {
            localStorage.setItem(localStorageKey, JSON.stringify([data]))
        }
        const json = [...JSON.parse(db), data]
        localStorage.setItem(localStorageKey, JSON.stringify(json))
    }
    
    function list() {
        const db = localStorage.getItem(localStorageKey)
        return db === null ? [] : JSON.parse(db)
    }

    return {
        create,
        list,
    }
}