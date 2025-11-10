agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono

agregar_contacto("Juan", "555-1234")
agregar_contacto("María", "555-5678")

print("Agenda de Contactos:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")
