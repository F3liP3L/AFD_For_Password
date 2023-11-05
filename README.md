# AFD_For_Password
Programación y descripción de un autómata para validar una contraseña segura.

## Reglas
El autómata de contraseña que se piensa construir deberá soportar solo caracteres ASCII estándar y entre estos los símbolos que conformarán el alfabeto del autómata serán:

∑ = {A-Z, a-z, 0-9, !, ¡, @, #, $, %, ^, &, *, (,), _, +, {, }, [, ], :, ;, <, >, , , ., ¿, ?, ~, -, \, /, =}
Las reglas que el autómata deberá cumplir son las siguientes:
-	Debe poseer por lo menos 4 caracteres
-	Debe poseer por lo menos un número
-	Debe poseer por lo menos una letra mayúscula
-	Debe poseer por lo menos una letra minúscula
-	No debe poseer espacios en blanco
-	Debe poseer por lo menos un carácter especial. Los caracteres especiales permitidos son ∑ = {!, ¡, @, #, $, %, ^, &, *, (,), _, +, {, }, [, ], :, ;, <, >, , , ., ¿, ?, ~, -, \, /, =}
-	Estos 4 caracteres que debe poseer obligatoriamente pueden estar ubicados en cualquier orden

## Diagrama de Estados

![digrama-estados-automata-contraseña](https://github.com/F3liP3L/AFD_For_Password/blob/main/assets/Automata_Password_Diagrama.png)

