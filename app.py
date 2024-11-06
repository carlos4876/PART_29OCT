import sqlite3

# Conexión a la base de datos 'restaurante.db'
conn = sqlite3.connect("restaurante.db")

# Creación de la tabla Platos
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS platos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
    """
)

# Creación de la tabla Mesas
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS mesas (
        id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL
    )
    """
)

# Creación de la tabla Pedidos
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (plato_id) REFERENCES platos(id),
        FOREIGN KEY (mesa_id) REFERENCES mesas(id)
    )
    """
)

# Insertar 5 platos
conn.execute("INSERT INTO platos(nombre, precio) VALUES ('CHICARRON', 35.00)")
conn.execute("INSERT INTO platos(nombre, precio) VALUES ('SAJTA', 30.00)")
conn.execute("INSERT INTO platos(nombre, precio) VALUES ('FRICASE', 25.00)")
conn.execute("INSERT INTO platos(nombre, precio) VALUES ('PAVO', 50.00)")
conn.execute("INSERT INTO platos(nombre, precio) VALUES ('PIQUEMACHO', 40.00)")

# Insertar 5 mesas
conn.execute("INSERT INTO mesas(numero) VALUES (1)")
conn.execute("INSERT INTO mesas(numero) VALUES (2)")
conn.execute("INSERT INTO mesas(numero) VALUES (3)")
conn.execute("INSERT INTO mesas(numero) VALUES (4)")
conn.execute("INSERT INTO mesas(numero) VALUES (5)")

# Insertar 5 pedidos
conn.execute("INSERT INTO pedidos(plato_id, mesa_id, cantidad, fecha) VALUES (1, 1, 2, '2024-11-01')")
conn.execute("INSERT INTO pedidos(plato_id, mesa_id, cantidad, fecha) VALUES (2, 2, 1, '2024-11-01')")
conn.execute("INSERT INTO pedidos(plato_id, mesa_id, cantidad, fecha) VALUES (3, 3, 3, '2024-11-02')")
conn.execute("INSERT INTO pedidos(plato_id, mesa_id, cantidad, fecha) VALUES (4, 4, 1, '2024-11-02')")
conn.execute("INSERT INTO pedidos(plato_id, mesa_id, cantidad, fecha) VALUES (5, 5, 2, '2024-11-03')")

# Confirmar cambios en la base de datos
conn.commit()

# Consultar y mostrar los pedidos con el nombre del plato, número de mesa, cantidad y fecha
print("\nDETALLE DE PEDIDOS")
cursor = conn.execute(
    """
    SELECT platos.nombre AS plato, mesas.numero AS mesa, pedidos.cantidad, pedidos.fecha
    FROM pedidos
    JOIN platos ON pedidos.plato_id = platos.id
    JOIN mesas ON pedidos.mesa_id = mesas.id
    """
)
for row in cursor:
    print(f"Plato: {row[0]}, Mesa: {row[1]}, Cantidad: {row[2]}, Fecha: {row[3]}")

# Cerrar la conexión
conn.close()
