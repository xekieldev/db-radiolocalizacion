export function useLink() {
    const tipoVinculo = [{
        value: 'Radioeléctrico',
        label: 'Radioeléctrico'
    }, {
        value: 'Físico',
        label: 'Físico'
    }, {
        value: 'No Aplica',
        label: 'No Aplica'
    }]

    return { tipoVinculo }
}