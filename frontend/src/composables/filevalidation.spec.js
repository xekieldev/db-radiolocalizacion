import { useFileValidation } from './filevalidation'
const { validateFile }  = useFileValidation()


import { it, expect } from 'vitest'

it('Sin expediente', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'A definir'}))
  expect(result).toBe(true)
  
})
it('Expediente GDE', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'EX-2020-12345672-  -APN-SDYME#ENACOM'}))
  expect(result).toBe(true)
  
})
it('Informe GDE', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'IF-2020-12345672-APN-SDYME#ENACOM'}))
  expect(result).toBe(true)
  
})
it('Expediente antiguo', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'EXPCNC 1234/2021'}))
  expect(result).toBe(true)
  
})
it('Expediente antiguo 2', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'EXPCNT E 1234/1985'}))
  expect(result).toBe(true)
  
})
it('Trámite Externo CCTE', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'TREENACOMCECOSAL 45/2016'}))
  expect(result).toBe(true)
  
})
it('Trámite Externo', (ctx) => {
  // prints name of the test
  const result = (validateFile({value: 'TRECNC 456/2012'}))
  expect(result).toBe(true)
  
})
