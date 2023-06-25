import { useStationType } from './stationtype'
const { emplazamiento }  = useStationType()


import { it, expect } from 'vitest'

it('Estudio y Planta Transmisora', () => {
  // prints name of the test
  const result = emplazamiento[0].value === 'Estudio y Planta Transmisora'
  expect(result).toBe(true)
  
})
it('Planta Transmisora', () => {
  // prints name of the test
  const result = emplazamiento[1].value === 'Planta Transmisora'
  expect(result).toBe(true)
  
})
it('Estudio', () => {
  // prints name of the test
  const result = emplazamiento[2].value === 'Estudio'
  expect(result).toBe(true)
  
})
it('FX', () => {
  // prints name of the test
  const result = emplazamiento[3].value === 'FX'
  expect(result).toBe(true)
  
})
it('FB', () => {
  // prints name of the test
  const result = emplazamiento[4].value === 'FB'
  expect(result).toBe(true)
  
})