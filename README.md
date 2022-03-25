## Pacman - Diego Carrillo
En la actividad se presentaron dos retos: Cambiar el tablero y aumentar la velocidad de los fantasmas.<br/>
<br/>Para cambiar el tablero fue necesario modificar los valores de la matriz de posiciones, estos valores pueden ser 1 o 0, donde 0 es color negro, las cuales representan "muros" o "paredes", y 1 el cual es color azul, y representa el camino por donde tanto pacman y los fantasmas pueden desplazarse. Modifique algunos de estos valores para cambiar el diseño del tablero.<br/>
<br/>Para aumentar la velocidad de los fantasmas fue necesario modificar la función de Move que venía definida en el código fuente. En esta función la velocidad de movimiento estaba definida en una sola línea de código y aplicaba para tanto pacman como para todos los fantasmas, para poder aumentar la velocidad de los fantasmas fue necesario dividir la función de Move en dos partes, las cuales son movePacman y moveGhosts. La velocidad se define usando el método onTimer(), que tiene como argumentos la función de movimiento y un valor en milisegundos, el cual es cada cuanto hay un cambio de posición (ej. onTimer(moveGhosts, 10). Los fantasmas se mueven cada 10 ms mientras que pacman cada 100, es decir, los fantasmas ahora se mueven 10 veces más rápido que Pacman.

## Tic Tac Toe - Julio César Gómez
Primero, se descargo el codigo del juego TicTacToe de la pagina proporcionada por el profesor. Despues siguiendo las intruccione, se analizo el codigo y se fueron haciendo prubas como cambiar valores para ver como funcionaba el codigo. De esta manera, haciendo pruebas modificando los valores de "x y "y" se cambio los tamaños y la posicion de los simbolos "X" y "0" respectivamente. Despues de una breve investigacion en internet, pude cambiar el color en el cual la libreria dibujaba las lineas de los simbolos, mediante la funcion color(). De la misma manera encontre una forma de revisar si una casilla ya estaba ocupada mediante el uso de un arreglo de ceros y condiciones if y else.

## Memory - Gabriel Delfín
Primero se descargó el código del juego Memory de la página proporcionada por el profesor. Se probó y se analizó el juego, para poder ver cómo trabajaba el código. Siguiendo las instrucciones de agregar dos nuevas funciones dentro del juego, se añadió un contador donde se pudieran contar y mostrar el número clicks o taps que da el usuario mediante un contador básico. Después se hizo otro contador, que, al lograr desbloquear todos las parejas (32 totales) se muestra un mensaje en pantalla mediante un print que dijera "Felicidades, lo lograste".
