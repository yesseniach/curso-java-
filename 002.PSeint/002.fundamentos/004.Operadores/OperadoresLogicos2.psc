Algoritmo OperadoresLogicos2
	
	// Disyunci�n: O, or, ||
	// M�x flexible, con que una condici�n sea Verdadero el 
	// resultado es verdadero
	
	age <- 17
	hasTutor <- Verdadero // True
	hasAccess <- age >= 18 O hasTutor
	Escribir "has access:" hasAccess
	Escribir "isAdult: ", age >= 18, " hasTutor: ", hasTutor, " result:", hasAccess
	// Verdadero o Verdadero = Verdadero
	// Falso O Verdadero = Verdadero
	// Verdadero O Falso = Verdadero
	// Falso O Falso = Falso
	
	// EJEMPLO autoevaluaci�n + caso practico
	testMultipleChoice <- 5
	individualPractice <- 4
	// Obligatorio aprobado en test y pr�ctica 
	passed <- testMultipleChoice >= 5 Y individualPractice >= 5
	Escribir  "Usando Y: ", passed
	Escribir "Nota: " (testMultipleChoice + individualPractice) / 2
	// Suficiente con aprobar uno de los dos 
	passed <- testMultipleChoice >= 5 O individualPractice >= 5
	Escribir  "Usando O: ", passed
	
	


	
	
FinAlgoritmo
