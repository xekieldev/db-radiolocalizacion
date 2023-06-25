import { usePolarization } from './polarization'
const { tipoPolarizacion }  = usePolarization()


import { it, expect } from 'vitest'

it('Vertical', () => {
  // prints name of the test
  const result = tipoPolarizacion[0].value === 'Vertical'
  expect(result).toBe(true)
  
})
it('Horizontal', () => {
  // prints name of the test
  const result = tipoPolarizacion[1].value === 'Horizontal'
  expect(result).toBe(true)
  
})
it('Circular', () => {
  // prints name of the test
  const result = tipoPolarizacion[2].value === 'Circular'
  expect(result).toBe(true)
  
})