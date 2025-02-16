#UNIVERSIDAD ESTATAL AMAZONICA
#tarea semana 9
#nombre: pamela morales
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            return resultados
        else:
            return "No se encontraron productos con ese nombre."

    def mostrar_inventario(self):
        return self.productos if self.productos else "El inventario está vacío."


# Cargar productos iniciales
inventario = Inventario()
inventario.agregar_producto(Producto(101, "Manzana", 50, 0.50))
inventario.agregar_producto(Producto(102, "Banana", 30, 0.30))
inventario.agregar_producto(Producto(103, "Leche", 20, 1.20))
inventario.agregar_producto(Producto(104, "Pan", 15, 1.00))
inventario.agregar_producto(Producto(105, "Queso", 10, 2.50))

# Simulación de menú sin input()
def menu_simulado(opciones):
    for opcion in opciones:
        print("\nSistema de Gestión de Inventarios")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Actualizar producto")
        print("5. Buscar producto por nombre")
        print("6. Salir")
        print(f"Opción seleccionada: {opcion}")

        if opcion == "1":
            print(inventario.mostrar_inventario())
        elif opcion == "2":
            nuevo_producto = Producto(106, "Yogur", 25, 1.50)
            inventario.agregar_producto(nuevo_producto)
        elif opcion == "3":
            inventario.eliminar_producto(102)
        elif opcion == "4":
            inventario.actualizar_producto(103, cantidad=25, precio=1.30)
        elif opcion == "5":
            print(inventario.buscar_por_nombre("Pan"))
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar simulación con opciones predefinidas
menu_simulado(["1", "2", "1", "3", "1", "4", "1", "5", "6"])
