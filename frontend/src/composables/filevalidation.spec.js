import { useFileValidation } from './filevalidation'
const { validateFile }  = useFileValidation()


import { it, expect } from 'vitest'

it('Sin expediente', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'A d                       efinir'}))
  expect(result).toBe(true)
  
})
it('should work', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'EX-2020-12345672-  -APN-SDYME#ENACOM'}))
  expect(result).toBe(true)
  
})
it('should work', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'IF-2020-12345672-APN-SDYME#ENACOM'}))
  expect(result).toBe(true)
  
})
it('should work', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'EXPCNC 1234/2021'}))
  expect(result).toBe(true)
  
})
it('should work', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'EXPCNT E 1234/1985'}))
  expect(result).toBe(true)
  
})
it('should work', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'TREENACOMCECOSAL 45/2016'}))
  expect(result).toBe(true)
  
})
it('should work', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'TRECNC 456/2012'}))
  expect(result).toBe(true)
  
})
