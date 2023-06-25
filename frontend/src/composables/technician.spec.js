import { useTechnician } from './technician'
const { tecnico }  = useTechnician()


import { it, expect } from 'vitest'

it('Técnico 1', () => {
  // prints name of the test
  const result = tecnico[0].value === 'Técnico 1'
  expect(result).toBe(true)
  
})
it('Técnico 2', () => {
  // prints name of the test
  const result = tecnico[1].value === 'Técnico 2'
  expect(result).toBe(true)
  
})
