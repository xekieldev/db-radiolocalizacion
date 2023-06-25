import { useUnit } from './unit'
const { unidad }  = useUnit()


import { it, expect } from 'vitest'

it('KHz', () => {
  // prints name of the test
  const result = unidad[0].value === 'KHz'
  expect(result).toBe(true)
  
})
it('MHz', () => {
  // prints name of the test
  const result = unidad[1].value === 'MHz'
  expect(result).toBe(true)
  
})
it('GHz', () => {
  // prints name of the test
  const result = unidad[2].value === 'GHz'
  expect(result).toBe(true)
  
})