import { useLink } from './link'
const { tipoVinculo }  = useLink()


import { it, expect } from 'vitest'

it('Radioeléctrico', () => {
  // prints name of the test
  const result = tipoVinculo[0].value === 'Radioeléctrico'
  expect(result).toBe(true)
  
})
it('Físico', () => {
  // prints name of the test
  const result = tipoVinculo[1].value === 'Físico'
  expect(result).toBe(true)
  
})
it('No Aplica', () => {
  // prints name of the test
  const result = tipoVinculo[2].value === 'No Aplica'
  expect(result).toBe(true)
  
})