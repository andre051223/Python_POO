class Vehiculo:
    def __init__(self, marca, modelo, año, precio, combustible="Gasolina"):
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._precio = precio
        self._combustible = combustible
        self._vendido = False

    # Propiedades para encapsulamiento
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def año(self):
        return self._año

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser positivo")

    @property
    def combustible(self):
        return self._combustible

    @property
    def vendido(self):
        return self._vendido

    def marcar_vendido(self):
        """Marca el vehículo como vendido"""
        self._vendido = True

    def marcar_disponible(self):
        """Marca el vehículo como disponible"""
        self._vendido = False

    def obtener_info(self):
        """
        Retorna información básica del vehículo

        Returns:
            str: Información del vehículo
        """
        estado = "Vendido" if self._vendido else "Disponible"
        return f"{self._marca} {self._modelo} ({self._año}) - ${self._precio:,.2f} - {estado}"

    def __str__(self):
        return self.obtener_info()


class Auto(Vehiculo):
    """
    Clase para automóviles, hereda de Vehículo
    """

    def __init__(self, marca, modelo, año, precio, num_puertas=4, tipo_transmision="Manual", combustible="Gasolina"):
        """
        Inicializa un automóvil con características específicas

        Args:
            num_puertas (int): Número de puertas
            tipo_transmision (str): Tipo de transmisión (Manual/Automática)
        """
        super().__init__(marca, modelo, año, precio, combustible)
        self._num_puertas = num_puertas
        self._tipo_transmision = tipo_transmision
        self._tipo_vehiculo = "Automóvil"

    @property
    def num_puertas(self):
        return self._num_puertas

    @property
    def tipo_transmision(self):
        return self._tipo_transmision

    @property
    def tipo_vehiculo(self):
        return self._tipo_vehiculo

    def obtener_info(self):
        """
        Sobrescribe el método para incluir información específica del auto

        Returns:
            str: Información completa del automóvil
        """
        info_base = super().obtener_info()
        return f"{info_base} | {self._num_puertas} puertas | {self._tipo_transmision} | {self._combustible}"


class Motocicleta(Vehiculo):
    """
    Clase para motocicletas, hereda de Vehículo
    """

    def __init__(self, marca, modelo, año, precio, cilindraje, tipo_moto="Deportiva", combustible="Gasolina"):
        """
        Inicializa una motocicleta con características específicas

        Args:
            cilindraje (int): Cilindraje de la motocicleta
            tipo_moto (str): Tipo de motocicleta
        """
        super().__init__(marca, modelo, año, precio, combustible)
        self._cilindraje = cilindraje
        self._tipo_moto = tipo_moto
        self._tipo_vehiculo = "Motocicleta"

    @property
    def cilindraje(self):
        return self._cilindraje

    @property
    def tipo_moto(self):
        return self._tipo_moto

    @property
    def tipo_vehiculo(self):
        return self._tipo_vehiculo

    def obtener_info(self):
        """
        Sobrescribe el método para incluir información específica de la moto

        Returns:
            str: Información completa de la motocicleta
        """
        info_base = super().obtener_info()
        return f"{info_base} | {self._cilindraje}cc | {self._tipo_moto} | {self._combustible}"


class Cliente:
    """
    Clase para representar clientes del concesionario
    """

    def __init__(self, nombre, cedula, telefono, email):
        """
        Inicializa un cliente con su información personal

        Args:
            nombre (str): Nombre completo del cliente
            cedula (str): Número de cédula
            telefono (str): Número de teléfono
            email (str): Correo electrónico
        """
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono
        self._email = email
        self._vehiculos_comprados = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def cedula(self):
        return self._cedula

    @property
    def telefono(self):
        return self._telefono

    @property
    def email(self):
        return self._email

    @property
    def vehiculos_comprados(self):
        return self._vehiculos_comprados.copy()

    def agregar_vehiculo_comprado(self, vehiculo):
        """
        Agrega un vehículo a la lista de compras del cliente

        Args:
            vehiculo (Vehiculo): Vehículo comprado
        """
        self._vehiculos_comprados.append(vehiculo)

    def obtener_info(self):
        """
        Retorna información del cliente

        Returns:
            str: Información del cliente
        """
        return f"Cliente: {self._nombre} | Cédula: {self._cedula} | Tel: {self._telefono}"

    def __str__(self):
        return self.obtener_info()


class Concesionario:
    """
    Clase principal que gestiona el concesionario de vehículos
    """

    def __init__(self, nombre, direccion, telefono):
        """
        Inicializa el concesionario

        Args:
            nombre (str): Nombre del concesionario
            direccion (str): Dirección del concesionario
            telefono (str): Teléfono de contacto
        """
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._inventario = []
        self._clientes = []
        self._ventas_realizadas = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def direccion(self):
        return self._direccion

    @property
    def telefono(self):
        return self._telefono

    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un vehículo al inventario

        Args:
            vehiculo (Vehiculo): Vehículo a agregar
        """
        self._inventario.append(vehiculo)
        print(f"✅ Vehículo agregado al inventario: {vehiculo.obtener_info()}")

    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente

        Args:
            cliente (Cliente): Cliente a registrar
        """
        # Verificar si ya existe
        for c in self._clientes:
            if c.cedula == cliente.cedula:
                print(f"⚠️  Cliente con cédula {cliente.cedula} ya está registrado")
                return False

        self._clientes.append(cliente)
        print(f"✅ Cliente registrado: {cliente.nombre}")
        return True

    def buscar_cliente_por_cedula(self, cedula):
        """
        Busca un cliente por su cédula

        Args:
            cedula (str): Cédula del cliente

        Returns:
            Cliente: Cliente encontrado o None
        """
        for cliente in self._clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    def consultar_vehiculos_disponibles(self, tipo_vehiculo=None):
        """
        Muestra todos los vehículos disponibles

        Args:
            tipo_vehiculo (str): Filtro por tipo de vehículo (opcional)
        """
        vehiculos_disponibles = [v for v in self._inventario if not v.vendido]

        if tipo_vehiculo:
            vehiculos_disponibles = [v for v in vehiculos_disponibles if v.tipo_vehiculo.lower() == tipo_vehiculo.lower()]

        if not vehiculos_disponibles:
            print("❌ No hay vehículos disponibles")
            return []

        print(f"\n🚗 Vehículos Disponibles ({len(vehiculos_disponibles)}):")
        print("-" * 80)
        for i, vehiculo in enumerate(vehiculos_disponibles, 1):
            print(f"{i}. {vehiculo.obtener_info()}")

        return vehiculos_disponibles

    def buscar_vehiculo_por_marca_modelo(self, marca, modelo):
        """
        Busca vehículos por marca y modelo

        Args:
            marca (str): Marca del vehículo
            modelo (str): Modelo del vehículo

        Returns:
            list: Lista de vehículos encontrados
        """
        vehiculos_encontrados = []
        for vehiculo in self._inventario:
            if (vehiculo.marca.lower() == marca.lower() and
                vehiculo.modelo.lower() == modelo.lower() and
                not vehiculo.vendido):
                vehiculos_encontrados.append(vehiculo)

        return vehiculos_encontrados

    def consultar_disponibilidad(self, marca, modelo):
        """
        Consulta si hay vehículos disponibles de una marca y modelo específicos

        Args:
            marca (str): Marca del vehículo
            modelo (str): Modelo del vehículo

        Returns:
            bool: True si hay disponibilidad, False si no
        """
        vehiculos = self.buscar_vehiculo_por_marca_modelo(marca, modelo)

        if vehiculos:
            print(f"\n✅ Tenemos {len(vehiculos)} vehículo(s) {marca} {modelo} disponible(s):")
            for i, vehiculo in enumerate(vehiculos, 1):
                print(f"  {i}. {vehiculo.obtener_info()}")
            return True
        else:
            print(f"\n❌ No tenemos vehículos {marca} {modelo} disponibles")
            return False

    def vender_vehiculo(self, vehiculo, cliente):
        """
        Realiza la venta de un vehículo a un cliente

        Args:
            vehiculo (Vehiculo): Vehículo a vender
            cliente (Cliente): Cliente que compra

        Returns:
            bool: True si la venta fue exitosa, False si no
        """
        if vehiculo.vendido:
            print("❌ Este vehículo ya ha sido vendido")
            return False

        if vehiculo not in self._inventario:
            print("❌ Este vehículo no está en nuestro inventario")
            return False

        # Realizar la venta
        vehiculo.marcar_vendido()
        cliente.agregar_vehiculo_comprado(vehiculo)

        # Registrar la venta
        venta = {
            'vehiculo': vehiculo,
            'cliente': cliente,
            'fecha': "2026-01-12",  # En un sistema real usaríamos datetime
            'precio': vehiculo.precio
        }
        self._ventas_realizadas.append(venta)

        print(f"\n🎉 ¡Venta realizada exitosamente!")
        print(f"Cliente: {cliente.nombre}")
        print(f"Vehículo: {vehiculo.obtener_info()}")
        print(f"Total: ${vehiculo.precio:,.2f}")

        return True

    def mostrar_ventas_realizadas(self):
        """
        Muestra todas las ventas realizadas
        """
        if not self._ventas_realizadas:
            print("❌ No se han realizado ventas")
            return

        print(f"\n📊 Ventas Realizadas ({len(self._ventas_realizadas)}):")
        print("-" * 100)
        total_ventas = 0

        for i, venta in enumerate(self._ventas_realizadas, 1):
            vehiculo = venta['vehiculo']
            cliente = venta['cliente']
            precio = venta['precio']
            fecha = venta['fecha']

            print(f"{i}. {fecha} | {cliente.nombre} | {vehiculo.marca} {vehiculo.modelo} | ${precio:,.2f}")
            total_ventas += precio

        print("-" * 100)
        print(f"💰 Total en ventas: ${total_ventas:,.2f}")

    def mostrar_estadisticas(self):
        """
        Muestra estadísticas del concesionario
        """
        total_vehiculos = len(self._inventario)
        vehiculos_vendidos = len([v for v in self._inventario if v.vendido])
        vehiculos_disponibles = total_vehiculos - vehiculos_vendidos
        total_clientes = len(self._clientes)

        print(f"\n📈 Estadísticas del Concesionario {self._nombre}:")
        print("-" * 50)
        print(f"Total de vehículos en inventario: {total_vehiculos}")
        print(f"Vehículos vendidos: {vehiculos_vendidos}")
        print(f"Vehículos disponibles: {vehiculos_disponibles}")
        print(f"Total de clientes registrados: {total_clientes}")

        if self._ventas_realizadas:
            total_ingresos = sum(venta['precio'] for venta in self._ventas_realizadas)
            print(f"Total de ingresos: ${total_ingresos:,.2f}")


def main():
    """
    Función principal para demostrar el funcionamiento del concesionario
    """
    print("🚗 Sistema de Concesionario de Vehículos 🚗")
    print("=" * 50)

    # Crear el concesionario
    concesionario = Concesionario(
        nombre="AutoMax Premium",
        direccion="Av. Principal 123, Ciudad",
        telefono="123-456-7890"
    )

    # Agregar vehículos al inventario
    print("\n📦 Agregando vehículos al inventario...")

    auto1 = Auto("Toyota", "Corolla", 2023, 85000000, 4, "Automática", "Híbrido")
    auto2 = Auto("Honda", "Civic", 2022, 75000000, 4, "Manual", "Gasolina")
    auto3 = Auto("Mazda", "CX-5", 2023, 120000000, 4, "Automática", "Gasolina")

    moto1 = Motocicleta("Yamaha", "R1", 2023, 45000000, 1000, "Deportiva")
    moto2 = Motocicleta("Honda", "CB650", 2022, 28000000, 650, "Naked")

    concesionario.agregar_vehiculo(auto1)
    concesionario.agregar_vehiculo(auto2)
    concesionario.agregar_vehiculo(auto3)
    concesionario.agregar_vehiculo(moto1)
    concesionario.agregar_vehiculo(moto2)

    # Registrar clientes
    print("\n👥 Registrando clientes...")
    cliente1 = Cliente("Juan Pérez", "12345678", "300-123-4567", "juan@email.com")
    cliente2 = Cliente("María García", "87654321", "300-765-4321", "maria@email.com")

    concesionario.registrar_cliente(cliente1)
    concesionario.registrar_cliente(cliente2)

    # Consultar vehículos disponibles
    concesionario.consultar_vehiculos_disponibles()

    # Consultar disponibilidad específica
    print("\n🔍 Consultas de disponibilidad...")
    concesionario.consultar_disponibilidad("Toyota", "Corolla")
    concesionario.consultar_disponibilidad("BMW", "X5")

    # Realizar algunas ventas
    print("\n💰 Realizando ventas...")
    vehiculos_toyota = concesionario.buscar_vehiculo_por_marca_modelo("Toyota", "Corolla")
    if vehiculos_toyota:
        concesionario.vender_vehiculo(vehiculos_toyota[0], cliente1)

    vehiculos_yamaha = concesionario.buscar_vehiculo_por_marca_modelo("Yamaha", "R1")
    if vehiculos_yamaha:
        concesionario.vender_vehiculo(vehiculos_yamaha[0], cliente2)

    # Mostrar estadísticas finales
    concesionario.mostrar_ventas_realizadas()
    concesionario.mostrar_estadisticas()

    # Mostrar vehículos disponibles después de las ventas
    print("\n🚗 Vehículos disponibles después de las ventas:")
    concesionario.consultar_vehiculos_disponibles()


if __name__ == "__main__":
    main()
