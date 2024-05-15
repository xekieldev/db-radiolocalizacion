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
      }, {
        value: 'Mixta',
        label: 'Mixta'
      }, {
        value: 'Oblicua',
        label: 'Oblicua'
      }, {
        value: 'Lineal',
        label: 'Lineal'
      }
      ]

    return { tipoPolarizacion }
}