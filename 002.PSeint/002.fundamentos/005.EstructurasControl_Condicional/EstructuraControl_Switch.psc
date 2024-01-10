Algoritmo EstructuraControl_Switch
	
	Escribir "Introduce un d�a de la semana: (LUNES, MARTES...)"
	Leer dayName
	// Transforma a may�sculas
	dayName <- Mayusculas(dayName)
	// Normalmente declaramos una variable antes de 
	// rellenarla en un bloque If else o switch para poder 
	// usarla fuera de ese bloque
	dayNumber <- 0 // 0 valor por defecto
	
	// Bloque que nos dice el n�mero al que corresponde
	// un dia de la semana
	
	Segun dayName Hacer
		"LUNES":
			dayNumber <- 1
		"MARTES":
			dayNumber <- 2
		"MIERCOLES":
			dayNumber <- 3
		"JUEVES":
			dayNumber <- 4
		"VIERNES":
			dayNumber <- 5
		"SABADO":
			dayNumber <- 6
		"DOMINGO":
			dayNumber <- 7
		De Otro Modo:
			Escribir "Incorrecto, ejecuta de nuevo el programa"
	Fin Segun
	
	Si dayNumber = 0 Entonces
		Escribir "Incorrect day introduced"
	SiNo
		Escribir "Dia numero ", dayNumber
	FinSi
	
	
FinAlgoritmo
