## Usuario

Hola requiero un script de python que lea la información de un archivo de documentación markdown y la muestre en consola, como ves el .md se divide en capítulos (titulares h2 o ##) requiero que el programa solicite al usuario la elección de un capítulo debe tener mensaje de bienvenida y despedida así como opción para finalizar el ciclo de peticiones al usuario, adapta automáticamente la ruta de ingreso del archivo.

## Copilot

Excelente 
Tu requerimiento está claro: quieres un programa en Python que:

1. Lea el contenido del archivo Markdown (`.md`).
    
2. Identifique los capítulos (líneas que empiezan con `##`).
    
3. Permita al usuario elegir uno para mostrar su contenido.
    
4. Tenga un mensaje de bienvenida y despedida.
    
5. Funcione en bucle hasta que el usuario decida salir.
    

Aquí tienes el **script Python completo** y comentado, listo para ejecutarse:

```text
# programa: leer_markdown.py
# Descripción: Lee el archivo Documentacion.md y permite al usuario elegir un capítulo (##) para visualizar su contenido.

def leer_markdown(ruta_archivo):
    """Lee el archivo markdown y devuelve su contenido línea por línea."""
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.readlines()

def obtener_capitulos(lineas):
    """Devuelve un diccionario con los títulos de nivel 2 (##) y su contenido."""
    capitulos = {}
    titulo_actual = None
    contenido_actual = []

    for linea in lineas:
        if linea.startswith("## "):
            # Si ya había un capítulo previo, lo guardamos antes de iniciar el nuevo
            if titulo_actual:
                capitulos[titulo_actual] = "".join(contenido_actual).strip()
                contenido_actual = []
            titulo_actual = linea.strip().replace("## ", "")
        elif titulo_actual:
            contenido_actual.append(linea)

    # Guarda el último capítulo
    if titulo_actual:
        capitulos[titulo_actual] = "".join(contenido_actual).strip()

    return capitulos

def mostrar_menu(capitulos):
    """Muestra el menú de capítulos disponibles."""
    print("\nCapítulos disponibles:\n")
    for i, capitulo in enumerate(capitulos.keys(), 1):
        print(f"{i}. {capitulo}")
    print(f"{len(capitulos) + 1}. Salir")

def main():
    print("👋 Bienvenido al lector de capítulos del archivo Documentacion.md 📘")

    ruta = "Proyecto Aurelion/Documentacion.md"

    try:
        lineas = leer_markdown(ruta)
        capitulos = obtener_capitulos(lineas)

        if not capitulos:
            print("⚠️ No se encontraron capítulos (##) en el archivo.")
            return

        while True:
            mostrar_menu(capitulos)
            opcion = input("\nSeleccione un capítulo por número: ")

            try:
                opcion = int(opcion)
            except ValueError:
                print("❌ Por favor ingrese un número válido.\n")
                continue

            if opcion == len(capitulos) + 1:
                print("\n👋 Gracias por usar el lector de Markdown. ¡Hasta pronto!")
                break
            elif 1 <= opcion <= len(capitulos):
                titulo = list(capitulos.keys())[opcion - 1]
                print(f"\n--- {titulo} ---\n")
                print(capitulos[titulo])
                print("\n" + "-" * 50 + "\n")
            else:
                print("⚠️ Opción fuera de rango.\n")

    except FileNotFoundError:
        print("❌ No se encontró el archivo README.md en el directorio actual.")

if __name__ == "__main__":
    main()
```

