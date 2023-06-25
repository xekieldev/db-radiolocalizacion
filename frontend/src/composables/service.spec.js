import { useService } from './service'
const { servicio }  = useService()


import { it, expect } from 'vitest'

it('FM', () => {
  // prints name of the test
  const result = servicio[0].value === 'FM'
  expect(result).toBe(true)
  
})
it('AM', () => {
  // prints name of the test
  const result = servicio[1].value === 'AM'
  expect(result).toBe(true)
  
})
it('SEE', () => {
  // prints name of the test
  const result = servicio[2].value === 'SEE'
  expect(result).toBe(true)
  
})
it('MCREM', () => {
  // prints name of the test
  const result = servicio[3].value === 'MCREM'
  expect(result).toBe(true)
  
})