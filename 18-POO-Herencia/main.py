
import clases

persona = clases.Persona()
persona.setNombre("Victor")
persona.setApellidos("Robles")
persona.setAltura("190 cm")
persona.setEdad("800 años")

print(f"La persona es {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("----------------------------------------\n")

informatico = clases.Informatico()
informatico.setNombre("Unai")
informatico.setApellidos("Torrecillas")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()} ")
print(informatico.getLenguajes())
print(informatico.caminar())

print("----------------------------------------\n")
tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")

print(tecnico.auditarRedes, tecnico.getLenguajes())
