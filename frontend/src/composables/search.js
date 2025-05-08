import { useTerritory } from "./territory"

const { getNameByCode } = useTerritory()

export function useSearch() {
    function search(data, searchText, targetProps) {
        const twoParamsText = searchText ?  searchText.toLowerCase().split('=') : ''
        if(twoParamsText !== '' && twoParamsText.length > 1) {
          const prop = twoParamsText[0]
          const twoParamsSearchResult = data.filter((item) => {
            if (!item[prop]) return false
            return String(item[prop]).toLowerCase() === String(twoParamsText[1]).toLowerCase()
            }) 
            let result = twoParamsSearchResult            
            return result
            
        } else {
            const searchString = searchText ? searchText.toLowerCase() : ''
            const searchResult = data.filter((item) => {
            const id = item.id
            let result = id == searchString
            for (let i = 0; i < targetProps.length; i++) {
              const prop = targetProps[i]            
              result = result || item[prop]?.toString?.().toLowerCase().includes(searchString)        
            }
            return result
        })
      return searchResult
    }}
    return { search }
}