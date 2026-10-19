# Taguette con colores por etiqueta

Para iniciar esta copia en macOS, abrir `Iniciar Taguette.command` con doble clic. Mantener la ventana de Terminal abierta mientras se usa Taguette. Si ya está ejecutándose, usar la pestaña abierta del navegador.

En **Resaltados → Crear una etiqueta**, elegir uno de los seis círculos o **Color personalizado**. Este último permite elegir cualquier color con el selector visual o escribir su código hexadecimal, por ejemplo `#203864`. La vista previa muestra el resultado antes de guardar. Para cambiar una etiqueta existente, pulsar **Editar**, elegir otro color y **Guardar y cerrar**. Sus fragmentos se actualizan automáticamente.

Los colores se guardan en la base de datos local `local.sqlite3` y viajan con la exportación del proyecto completo. Al exportar un documento a HTML o PDF, se conservan los colores de sus códigos y las etiquetas junto a cada fragmento. Los formatos tabulares y los libros de códigos mantienen su estructura original.

El color personalizado queda guardado en la etiqueta; no hay un límite de seis colores para tus codificaciones. El texto cambia de color automáticamente para seguir siendo legible. Los fragmentos superpuestos muestran franjas; cuando se mezclan fondos claros y oscuros, las franjas aparecen al pie del texto para conservar el contraste. Las etiquetas anteriores reciben amarillo suave al migrar la base de datos. Taguette crea la copia de seguridad habitual antes de actualizar una base existente.

## Entorno y comprobaciones

- Python 3.13, dependencias instaladas dentro de `.venv`.
- Calibre se guarda en `.tools/calibre.app`; el acceso de inicio configura su ruta automáticamente.
- Traducciones compiladas con `PATH="$PWD/.venv/bin:$PATH" sh scripts/update_translations.sh`.
- Pruebas: `.venv/bin/python -m unittest tests` (suite completa; las pruebas Selenium necesitan un controlador de navegador).
- Verificación manual: crear etiqueta, elegir color, guardar, recargar, cambiar color y revisar fragmentos superpuestos.

## Instalar esta copia en otra computadora

Esta copia conserva la licencia BSD-3-Clause del proyecto original. El repositorio
incluye el código y las pruebas, no los proyectos de investigación ni los programas
instalados en esta Mac.

1. Instalar Python 3.10 o posterior y Calibre desde https://calibre-ebook.com/.
   En macOS, colocar `calibre.app` en `/Applications`.
2. Clonar este repositorio y entrar en su carpeta.
3. Crear e instalar el entorno de desarrollo:

   ```sh
   python3 -m venv .venv
   .venv/bin/python -m pip install -e . babel bcrypt aiohttp
   PATH="$PWD/.venv/bin:$PATH" sh scripts/update_translations.sh
   ```

4. En macOS, abrir `Iniciar Taguette.command` con doble clic. En otros sistemas,
   activar `.venv`, comprobar que `ebook-convert` esté en el PATH y ejecutar
   `taguette --browser --database local.sqlite3`.

La migración incorpora un campo de color a la base de datos. Taguette hace una
copia de seguridad antes de actualizar una base SQLite existente. El proyecto
completo exportado por esta copia requiere una instalación que conozca esta
migración para reabrirlo; conservar una copia del original antes de migrar.

## Prueba real de PDF

`scripts/create_pdf_test_fixture.py` genera un documento sintético para probar
la entrada de PDF, los seis colores rápidos y un color personalizado oscuro.
Además de las pruebas normales, se puede ejecutar la prueba de conversión real:

```sh
.venv/bin/python -m pip install reportlab
.venv/bin/python scripts/create_pdf_test_fixture.py tmp/pdfs/entrada-prueba.pdf
CALIBRE=/Applications/calibre.app/Contents/MacOS \
TAGUETTE_TEST_PDF_INPUT="$PWD/tmp/pdfs/entrada-prueba.pdf" \
.venv/bin/python -m unittest tests
```

En Linux, usar `CALIBRE=/usr/bin` si Calibre fue instalado allí. Las dos pruebas
Selenium necesitan un navegador y su controlador; sin esa configuración se omiten.
La prueba de PDF también se omite cuando no se suministran el conversor y el archivo
de prueba.

## Verificación final de esta copia

- Suite completa con Calibre y PDF real: 35 pruebas correctas, 2 pruebas Selenium omitidas.
- Estilo Python (`flake8`), sintaxis JavaScript y acceso de inicio: correctos.
- Guardado y recarga de un color personalizado: comprobados en el navegador.
- PDF exportado: comprobados los seis colores rápidos y un azul personalizado oscuro, con texto legible.
