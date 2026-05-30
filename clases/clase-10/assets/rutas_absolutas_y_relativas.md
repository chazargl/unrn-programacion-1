# Enlaces en GitHub Markdown: Rutas Absolutas y Relativas

En los archivos Markdown de GitHub, la sintaxis básica para crear un enlace es `[Texto del enlace](URL)`. Al vincular archivos dentro de tu propio repositorio, puedes usar rutas relativas o absolutas. De acuerdo con la [documentación oficial de GitHub sobre enlaces relativos](https://docs.github.com/es), la plataforma procesa automáticamente estas rutas según el contexto.

---

## 1. Rutas Relativas

Se basan en la ubicación del archivo Markdown actual. Son la opción recomendada porque no se rompen si clonas el repositorio, creas un *fork* o le cambias el nombre.

* **Mismo nivel:** Enlaza un archivo en la misma carpeta.

  ```markdown
  [Ir al archivo](archivo.md)
  ```

* **Subcarpeta:** Entra a una carpeta dentro de tu ubicación actual.

  ```markdown
  [Ver documentación](docs/instrucciones.md)
  ```

* **Directorio superior:** Usa `../` para subir un nivel en el árbol de carpetas.

  ```markdown
  [Volver al inicio](../README.md)
  ```

---

## 2. Rutas Absolutas

En GitHub, una ruta absoluta dentro del repositorio comienza con una barra diagonal `/`. Esta barra representa la **raíz del repositorio** (la carpeta principal). Funcionará igual sin importar en qué subcarpeta esté el archivo Markdown.

* **Desde la raíz del proyecto:**

  ```markdown
  [Ir a la guía principal](/docs/guia_total.md)
  ```

* **A un archivo en la raíz:**

  ```markdown
  [Ver colaboradores](/CONTRIBUTING.md)
  ```

---

## 3. Casos Especiales: Carpetas y Secciones de GitHub

GitHub interpreta los enlaces a carpetas usando su interfaz web (`/tree/` o `/blob/`). Para asegurar la compatibilidad:

* **Enlaces a carpetas:** Termina siempre la ruta con una barra diagonal.

  ```markdown
  [Carpeta de imágenes](assets/)
  ```

* **Saltar a Issues o Pull Requests:** Puedes salir del árbol de archivos usando rutas relativas superiores (`../../`) para conectar con herramientas del proyecto.

  ```markdown
  [Ver los Issues del proyecto](../../issues)
  ```

---
***Fuentes y lecturas sugeridas:***

* [GitHub Docs - Autolinked references and URLs](https://docs.github.com/es/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls)
* [GitHub Docs - Getting started with writing and formatting on GitHub](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github)
