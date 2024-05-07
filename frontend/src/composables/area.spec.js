import { useArea } from './area'
const { area }  = useArea()


import { it, expect } from 'vitest'


it('AGCCTYL', () => {
  // prints name of the test
  const result = area[0].value === 'AGCCTYL'
  expect(result).toBe(true)
  
})
it('Buenos Aires', () => {
  // prints name of the test
  const result = area[1].value === 'Buenos Aires'
  expect(result).toBe(true)
  
})
it('Córdoba', () => {
  // prints name of the test
  const result = area[2].value === 'Cordoba'
  expect(result).toBe(true)
  
})
it('Salta', () => {
  // prints name of the test
  const result = area[3].value === 'Salta'
  expect(result).toBe(true)
  
})
it('Posadas', () => {
  // prints name of the test
  const result = area[4].value === 'Posadas'
  expect(result).toBe(true)
  
})
it('Neuquén', () => {
  // prints name of the test
  const result = area[5].value === 'Neuquen'
  expect(result).toBe(true)
  
})
it('Comodoro Rivadavia', () => {
  // prints name of the test
  const result = area[6].value === 'Comodoro Rivadavia'
  expect(result).toBe(true)
  
})