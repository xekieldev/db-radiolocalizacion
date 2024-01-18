export function useTechnician() {
    // const tecnico = [{
    //     'nombre': 'N_Técnico1',
    //     'apellido': 'A_Técnico1'
    //     },
    //     {
    //     'nombre': 'N_Técnico2',
    //     'apellido': 'A_Técnico2'},
    // ]
    // const tecnico = [{
    //     value: 'Tecnico1',
    //     label: 'Técnico1'
    // },
    // {
    //     value: 'Tecnico2',
    //     label: 'Técnico2'
    // }]
    const tecnico = [{
        id: '1',
        nombre: 'Roberto',
        apellido: 'Sanchez'
    },
    {
        id:'2',
        nombre: 'Juan',
        apellido: 'Perez'
    },
    {
        id:'3',
        nombre: 'Jose',
        apellido: 'Altamirano'
    },
    {
        id:'4',
        nombre: 'Raul',
        apellido: 'Perez'
    }]
    return { tecnico }
}