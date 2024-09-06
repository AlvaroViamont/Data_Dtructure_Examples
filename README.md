# <span style="color:#7D53DE">Ejemplos de Estructuras de datos con Python </span>

# <span style="color:#34F6F2">1. Simulación de Gestión de Producción en una Fábrica</span>

<span style="color:#EEF8FF">En una fábrica de manufactura, se reciben órdenes de producción de distintos productos. Estas órdenes deben pasar por varias fases de procesamiento, ensamblado y verificación de calidad antes de ser despachadas. El sistema que vas a simular debe gestionar estas fases de manera eficiente aplicando las siguientes estructuras de datos:</span>

* <span style="color:#EEF8FF">Pilas para gestionar las tareas de ensamblado de productos.</span>
* <span style="color:#EEF8FF">Colas para gestionar la verificación de calidad de los productos antes de su despacho.</span>
* <span style="color:#EEF8FF">Árboles binarios para organizar y archivar las órdenes completadas, permitiendo búsquedas rápidas de pedidos procesados.</span>
# <span style="color:#78E3FD">Requerimientos</span>
## <span style="color:#D1F5FF">1. Gestión de Ensamblado con Pilas</span>
<span style="color:#EEF8FF">Las piezas necesarias para ensamblar un producto se organizan en una pila. Las piezas más recientes que llegan deben ser las primeras en ser ensambladas.</span>

<span style="color:#EEF8FF">Cada pedido tiene un número de identificación, y las piezas necesarias para ensamblarlo se deben almacenar temporalmente en una pila.</span>
<span style="color:#EEF8FF">El sistema debe permitir:</span>

* <span style="color:#EEF8FF">Agregar piezas a la pila de ensamblado.</span>
* <span style="color:#EEF8FF">Procesar una pieza sacándola de la pila.</span>
* <span style="color:#EEF8FF">Verificar qué pieza está en la cima de la pila sin sacarla.</span>
* <span style="color:#EEF8FF">Verificar si la pila está vacía.</span>
## <span style="color:#D1F5FF">2. Gestión de Verificación de Calidad con Colas</span>
<span style="color:#EEF8FF">Una vez que un producto ha sido ensamblado, debe pasar a la fase de verificación de calidad. Los productos en esta fase se organizan en una cola, ya que los productos que se ensamblaron primero deben ser verificados primero.</span>

<span style="color:#EEF8FF">Cada producto que pasa la verificación de calidad puede ser despachado, y aquellos que no la pasan vuelven a la pila de ensamblado para correcciones. El sistema debe permitir:</span>

* <span style="color:#EEF8FF">Encolar productos en la cola de verificación de calidad.</span>
* <span style="color:#EEF8FF">Desencolar productos que han sido verificados y están listos para despacharse.</span>
* <span style="color:#EEF8FF">Verificar si la cola está vacía y mostrar el próximo producto a verificar.</span>
## <span style="color:#D1F5FF">3. Archivar Órdenes Completadas con Árboles Binarios</span>
<span style="color:#EEF8FF">Después de que un producto ha pasado por la verificación de calidad y ha sido despachado, la orden de producción debe ser archivada en un árbol binario de búsqueda según el número de identificación del pedido.</span>

<span style="color:#EEF8FF">El árbol debe permitir búsquedas eficientes para encontrar rápidamente órdenes procesadas en el pasado.</span>
<span style="color:#EEF8FF">El sistema debe permitir:</span>

* <span style="color:#EEF8FF">Insertar una nueva orden completada en el árbol binario de acuerdo a su número de identificación.</span>
* <span style="color:#EEF8FF">Buscar una orden completada utilizando su número de identificación.</span>
* <span style="color:#EEF8FF">Realizar un recorrido inorden para mostrar las órdenes completadas en orden ascendente según su número de identificación.</span>
# <span style="color:#78E3FD">Especificaciones Adicionales</span>
1. <span style="color:#EEF8FF">Interfaz de Usuario:</span>
<span style="color:#EEF8FF">El sistema debe tener un menú interactivo donde los usuarios puedan realizar las siguientes acciones:</span>
   * <span style="color:#EEF8FF">Agregar una pieza a la pila de ensamblado: Permitir al usuario ingresar los detalles del producto que está en ensamblado.</span>
   * <span style="color:#EEF8FF">Procesar una pieza: Extraer una pieza de la pila y completar su ensamblaje.</span>
   * <span style="color:#EEF8FF">Enviar a verificación: Enviar el producto ensamblado a la cola de verificación de calidad.</span>
   * <span style="color:#EEF8FF">Despachar un producto: Desencolar un producto que haya pasado la verificación de calidad.</span>
   * <span style="color:#EEF8FF">Archivar una orden: Archivar una orden completada en el árbol binario.</span>
   * <span style="color:#EEF8FF">Buscar una orden archivada: Permitir al usuario buscar una orden archivada mediante su número de identificación.</span>
1. <span style="color:#EEF8FF">Condiciones de la simulación:</span>
    * <span style="color:#EEF8FF">Cada pedido de producción tiene un número de identificación único y varias piezas que deben ser ensambladas.</span>
    * <span style="color:#EEF8FF">Los productos que no pasen la verificación de calidad deben volver al proceso de ensamblado (es decir, a la pila).</span>
    * <span style="color:#EEF8FF">Debe garantizarse que los productos más antiguos en la cola de verificación sean verificados primero.</span>
1. <span style="color:#EEF8FF">Consideraciones de Eficiencia:</span>
    * <span style="color:#EEF8FF">La simulación debe priorizar la eficiencia en la búsqueda de órdenes completadas utilizando el árbol binario, para que las consultas sobre pedidos antiguos sean rápidas.</span>
    * <span style="color:#EEF8FF">El ensamblado de piezas y el despacho de productos debe seguir los principios de LIFO (último en entrar, primero en salir) y FIFO (primero en entrar, primero en salir), respectivamente.</span>

# <span style="color:#78E3FD">Ejemplo de Flujo</span>
1. <span style="color:#EEF8FF">Se reciben piezas para ensamblar un producto con el ID 001, y estas se almacenan en una pila.</span>
2. <span style="color:#EEF8FF">El producto 001 es ensamblado completando todas sus piezas y se envía a la verificación de calidad (se encola en la cola de verificación).</span>
3. <span style="color:#EEF8FF">Después de que el producto 001 pasa la verificación, es despachado y la orden es archivada en el árbol binario de órdenes completadas.</span>
4. <span style="color:#EEF8FF">Más adelante, el usuario busca el pedido 001 en el archivo para revisar los detalles.</span>
# <span style="color:#78E3FD">Resumen de las Estructuras Utilizadas</span>
* <span style="color:#EEF8FF">Pila: Para el ensamblaje de piezas de productos en proceso.</span>
* <span style="color:#EEF8FF">Cola: Para gestionar la verificación de calidad de los productos, asegurando que los más antiguos se procesen primero.</span>
* <span style="color:#EEF8FF">Árbol Binario de Búsqueda: Para archivar las órdenes de producción completadas, permitiendo búsquedas eficientes por número de identificación.</span>

# <span style="color:#78E3FD">Solución:</span>