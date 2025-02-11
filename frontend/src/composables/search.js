import { useTerritory } from "./territory"

const { getNameByCode } = useTerritory()

export function useSearch() {
    function search(data, searchText, targetProps) {
        const searchString = searchText ? searchText.toLowerCase() : ''
        const searchResult = data.filter((item) => {
          const id = item.id
          let result = id == searchString
          for (let i = 0; i < targetProps.length; i++) {
            const prop = targetProps[i]            
            result = result || item[prop]?.toString?.().toLowerCase().includes(searchString)        
            // result = result || (item[prop] !== null && item[prop] !== undefined ? item[prop].toString() : '').toLowerCase().includes(searchString)        
          }
          return result
      })
      return searchResult
    }
    return { search }
}