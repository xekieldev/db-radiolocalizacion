export function usePolarization() {
    
    const tipoPolarizacion = [{
        value: 'Vertical',
        label: 'Vertical'
      }, {
        value: 'Horizontal',
        label: 'Horizontal'
      }, {
        value: 'Circular',
        label: 'Circular'
      }
      ]

    return { tipoPolarizacion }
}