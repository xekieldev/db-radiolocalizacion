export function useAirport() {
    const airport = [
      {
        value: 'AEROPARQUE JORGE NEWBERY',
        label: 'AEROPARQUE JORGE NEWBERY',
        latitude: -34.558888,
        longitude: -58.416389,
      },
      {
        value: 'EZEIZA',
        label: 'EZEIZA',
        latitude: -34.82222222,
        longitude: -58.53583333,
      },
      {
        value: 'BAHIA BLANCA',
        label: 'BAHIA BLANCA',
        latitude: -38.7275,
        longitude: -62.15333333,	
      },
      {
        value: 'CATAMARCA',
        label: 'CATAMARCA',
        latitude: -28.59305556, 
        longitude: -65.75111111,
      },
      {
        value: 'PUERTO IGUAZÚ / CATARATAS DEL IGUAZÚ',
        label: 'PUERTO IGUAZÚ / CATARATAS DEL IGUAZÚ',
        latitude: -25.73722,
        longitude: -54.47354,
      },
      {
        value: 'COMODORO RIVADAVIA',
        label: 'COMODORO RIVADAVIA',
        latitude: -45.78527778,
        longitude: -67.46555556,
      },
      {
        value: 'AEROCLUB COMODORO RIVADAVIA',
        label: 'AEROCLUB COMODORO RIVADAVIA'
      },
      {
        value: 'CONCORDIA',
        label: 'CONCORDIA',
        latitude: -31.29694444,
        longitude: -57.99666667,
      },
      {
        value: 'CÓRDOBA',
        label: 'CÓRDOBA',
        latitude: -31.31,
        longitude: -64.20833333,
      },
      {
        value: 'CÓRDOBA - ESCUELA DE AVIACIÓN',
        label: 'CÓRDOBA - ESCUELA DE AVIACIÓN'
      },
      {
          value: 'CORRIENTES',
          label: 'CORRIENTES',
          latitude: -27.44555556,
          longitude: -58.76194444,
      },
      {
        value: 'DON TORCUATO',
        label: 'DON TORCUATO'
      },
      {
        value: 'EL CALAFATE',
        label: 'EL CALAFATE',
        latitude: -50.28,
        longitude: -72.05305556	
      },
      {
        value: 'EL PALOMAR',
        label: 'EL PALOMAR',
        latitude: -34.61,
        longitude: -58.6125,
      },
      {
        value: 'ESQUEL',
        label: 'ESQUEL',
        latitude: -42.90381,
        longitude: -71.13554,
      },
      {
        value: 'FORMOSA',
        label: 'FORMOSA',
        latitude: -26.21277778,
        longitude: -58.22805556,
      },
      {
        value: 'GENERAL PICO',
        label: 'GENERAL PICO'
      },
      {
        value: 'GOYA',
        label: 'GOYA',
        latitude: -29.10595,
        longitude: -59.21874,
      },
      {
        value: 'GUALEGUAYCHÚ',
        label: 'GUALEGUAYCHÚ',
        latitude: -33.00555556,
        longitude: -58.61277778,
      },
      {
        value: 'SAN SALVADOR DE JUJUY',
        label: 'SAN SALVADOR DE JUJUY',
        latitude:-24.3925,
        longitude:-65.09777778,
      },
      {
        value: 'JUNÍN',
        label: 'JUNÍN'
      },
      {
        value: 'LA PLATA',
        label: 'LA PLATA'
      },
      {
        value: 'LA RIOJA',
        label: 'LA RIOJA',
        latitude: -29.38055556,
        longitude: -66.79583333,
      },
      {
        value: 'AEROCLUB LUJÁN',
        label: 'AEROCLUB LUJÁN'
      },
      {
        value: 'MALARGÜE',
        label: 'MALARGÜE',
        latitude: -35.49527778,
        longitude: -69.57305556,
      },
      {
        value: 'MARCOS JUAREZ',
        label: 'MARCOS JUAREZ'
      },
      {
        value: 'MAR DEL PLATA',
        label: 'MAR DEL PLATA',
        latitude: -37.93416667,
        longitude: -57.57333333,
      },
      {
        value: 'MARIANO MORENO',
        label: 'MARIANO MORENO',
        latitude: -34.56,
        longitude: -58.78972222,	
      },
      {
        value: 'MENDOZA',
        label: 'MENDOZA',
        latitude: -32.83166667,
        longitude:  -68.79277778,
      },
      {
        value: 'MORON',
        label: 'MORON',
        latitude: -34.67916667,
        longitude: -58.64361111,
      },
      {
        value: 'NECOCHEA',
        label: 'NECOCHEA'
      },
      {
        value: 'NEUQUÉN',
        label: 'NEUQUÉN',
        latitude: -38.94888889,
        longitude: -68.15583333,	
      },
      {
        value: 'PARANÁ',
        label: 'PARANÁ',
        latitude: -31.79472222,
        longitude: -60.48027778,
      },
      {
        value: 'PASO DE LOS LIBRES',
        label: 'PASO DE LOS LIBRES',
        latitude: -29.68805556,
        longitude: -57.15222222,
      },
      {
        value: 'POSADAS',
        label: 'POSADAS',
        latitude: -27.38573,
        longitude: -55.97049,
      },
      {
        value: 'PUERTO MADRYN',
        label: 'PUERTO MADRYN',
        latitude: -42.75916667,
        longitude: -65.10277778,
      },
      {
        value: 'RESISTENCIA',
        label: 'RESISTENCIA',
        latitude: -27.45,
        longitude: -59.05611111,
      },
      {
        value: 'RÍO CUARTO',
        label: 'RÍO CUARTO'
      },
      {
        value: 'RÍO GALLEGOS',
        label: 'RÍO GALLEGOS',
        latitude: -51.60881,
        longitude: -69.31217,
      },
      {
        value: 'RIO GRANDE',
        label: 'RIO GRANDE',
        latitude: -53.7776,
        longitude: -67.74952,
      },
      {
        value: 'ROSARIO',
        label: 'ROSARIO',
        latitude: -32.90361111,
        longitude: -60.78444444,
      },
      {
        value: 'SALTA',
        label: 'SALTA',
        latitude: -24.85972222,
        longitude: -65.48694444,
      },
      {
        value: 'SAN CARLOS DE BARILOCHE',
        label: 'SAN CARLOS DE BARILOCHE',
        latitude: -41.15111111,
        longitude: -71.15777778,
      },
      {
        value: 'SAN FERNANDO',
        label: 'SAN FERNANDO',
        latitude: -34.45454,
        longitude: -58.59091,
      },
      {
        value: 'SAN JUAN',
        label: 'SAN JUAN',
        latitude: -31.57138889,
        longitude: -68.41833333,
      },
      {
        value: 'SAN LUIS',
        label: 'SAN LUIS',
        latitude: -33.27222222,
        longitude: -66.35666667,
      },
      {
        value: 'SAN RAFAEL',
        label: 'SAN RAFAEL',
        latitude: -34.58781667,
        longitude: -68.40358889,
      },
      {
        value: 'SANTA FE',
        label: 'SANTA FE',
        latitude: -31.71083333,
        longitude: -60.81138889,
      },
      {
        value: 'SANTA ROSA',
        label: 'SANTA ROSA',
        latitude: -36.58833333,
        longitude: -64.27583333,
      },
      {
        value: 'SANTIAGO DEL ESTERO',
        label: 'SANTIAGO DEL ESTERO',
        latitude: -27.76555556, 
        longitude: -64.31,
      },
      {
        value: 'TANDIL',
        label: 'TANDIL',
        latitude: -37.23437778,
        longitude: -59.22858611,	
      },
      {
        value: 'TERMAS DE RÍO HONDO',
        label: 'TERMAS DE RÍO HONDO',
        latitude: -27.49662,
        longitude: -64.93596,
      },
      {
        value: 'TRELEW',
        label: 'TRELEW',
        latitude: -43.21055556,
        longitude: -65.27027778,
      },
      {
        value: 'SAN MIGUEL DE TUCUMÁN',
        label: 'SAN MIGUEL DE TUCUMÁN',
        latitude: -26.84083333,
        longitude: -65.10472222,
      },
      {
        value: 'USHUAIA',
        label: 'USHUAIA',
        latitude: -54.84333333,
        longitude: -68.29555556,
      },
      {
        value: 'SANTA ROSA DE CONLARA',
        label: 'SANTA ROSA DE CONLARA',
        latitude: -32.38472222,
        longitude: -65.18583333,
      },
      {
        value: 'VIEDMA',
        label: 'VIEDMA',
        latitude: -40.87027778,
        longitude: -62.99666667,
      },
      {
        value: 'VILLA REYNOLDS',
        label: 'VILLA REYNOLDS',
        latitude: -33.73178,
        longitude: -65.37579,
      },
      {
        value: 'OTRO',
        label: 'OTRO',
      }]

    return { airport }
}


// latitude:,
// longitude:,

// AEROPARQUE JORGE NEWBERY (CABA)
// EZEIZA (BA)
// BAHIA BLANCA (BA)
// CATAMARCA (CA)
// PUERTO IGUAZÚ / CATARATAS DEL IGUAZÚ (MS)
// COMODORO RIVADAVIA (CH)
// AEROCLUB COMODORO RIVADAVIA (CH)
// CONCORDIA (ER)
// CÓRDOBA (CD)
// CÓRDOBA - ESCUELA DE AVIACIÓN (CD)
// CORRIENTES (CO)
// DON TORCUATO (BA)
// EL CALAFATE (SC)
// EL PALOMAR (BA)
// ESQUEL (CH)
// FORMOSA (FM)
// GENERAL PICO (LP)
// GOYA (CO)
// GUALEGUAYCHÚ (ER)
// SAN SALVADOR DE JUJUY (JJ)
// JUNÍN (BA)
// LA PLATA (BA)
// LA RIOJA (LR)
// AEROCLUB LUJAN (BA)
// MALARGÜE (MZ)
// MARCOS JUAREZ (CD)
// MAR DEL PLATA (BA)
// MARIANO MORENO (BA)
// MENDOZA (MZ)
// MORON (BA)
// NECOCHEA (BA)
// NEUQUÉN (NQ)
// PARANÁ (ER)
// PASO DE LOS LIBRES (CO)
// PEHUAJÓ (BA)
// POCITO (SJ)
// POSADAS (MS)
// PRESIDENCIA ROQUE SAENZ PEÑA (CC)
// PUERTO MADRYN (CH)
// QUILMES (BA)
// RAFAELA (SF)
// RESIDENCIA DE OLIVOS (BA)
// RECONQUISTA (SF)
// RESISTENCIA (CC)
// RINCÓN DE LOS SAUCES (NQ)
// RÍO CUARTO (CD)
// RÍO GALLEGOS (SC)
// RIO GRANDE (TF)
// ROSARIO (SF)
// SALTA (SA)
// SAN CARLOS DE BARILOCHE (RN)
// SAN FERNANDO (BA)
// SAN JUAN (SJ)
// SAN JUSTO (BA)
// SAN LUIS (SL)
// SAN MARTÍN DE LOS ANDES (NQ)
// SAN RAFAEL (MZ)
// SANTA FE (SF)
// SANTA ROSA (LP)
// SANTIAGO DEL ESTERO (SE)
// TANDIL (BA)
// TARTAGAL (SA)
// TERMAS DE RÍO HONDO
// TRELEW (CH)
// SAN MIGUEL DE TUCUMÁN (TC)
// USHUAIA (TF)
// VALLE DEL CONLARA (SL)
// VIEDMA (RN)
// VILLA GESELL (BA)
// VILLA REYNOLDS (SL)
