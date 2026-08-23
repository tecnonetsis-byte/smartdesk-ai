# Requirements – SmartDesk AI

## Introducción
SmartDesk AI es una aplicación web para registrar solicitudes empresariales y apoyar su clasificación inicial mediante Inteligencia Artificial. El sistema propone una categoría, una prioridad y un nivel de confianza, manteniendo la posibilidad de revisión humana.

## RF-01 – Registro de solicitudes
**Historia de usuario:** Como solicitante, quiero registrar una solicitud con mis datos y una descripción para que pueda ser atendida y trazada.

### Criterios de aceptación
1. **CUANDO** el usuario envía nombre, correo, asunto y descripción válidos, **EL SISTEMA DEBERÁ** crear una solicitud con identificador único.
2. **SI** falta un campo obligatorio o no cumple validación, **EL SISTEMA DEBERÁ** rechazar el registro y devolver un mensaje de validación.
3. **CUANDO** una solicitud es creada, **EL SISTEMA DEBERÁ** asignar el estado inicial `Pendiente`.

## RF-02 – Clasificación inteligente
**Historia de usuario:** Como operador de soporte, quiero que el sistema analice automáticamente cada solicitud para priorizar mi trabajo con mayor rapidez.

### Criterios de aceptación
1. **CUANDO** se crea una solicitud, **EL SISTEMA DEBERÁ** analizar asunto y descripción con el clasificador IA.
2. **EL SISTEMA DEBERÁ** devolver una categoría de: Acceso, Soporte técnico, Facturación, Comercial, Administrativo u Otros.
3. **EL SISTEMA DEBERÁ** devolver una prioridad de: Baja, Media o Alta.
4. **SI** la confianza es menor a 60 %, **EL SISTEMA DEBERÁ** marcar la solicitud para revisión manual.
5. **EL SISTEMA DEBERÁ** permitir que un operador corrija categoría y prioridad.

## RF-03 – Seguimiento de solicitudes
**Historia de usuario:** Como operador, quiero consultar y actualizar solicitudes para gestionar su resolución.

### Criterios de aceptación
1. **EL SISTEMA DEBERÁ** listar las solicitudes registradas con id, asunto, categoría, prioridad, estado y fecha.
2. **EL SISTEMA DEBERÁ** permitir filtrar por categoría, prioridad y estado.
3. **CUANDO** un operador modifica el estado, categoría o prioridad, **EL SISTEMA DEBERÁ** persistir el cambio.

## Requisitos no funcionales principales
- API REST documentada mediante OpenAPI.
- Persistencia local con SQLite para el alcance académico.
- Pruebas unitarias y de integración automatizadas.
- Arquitectura modular cliente-servidor.
- Código versionado con Git y documentación del proyecto en el repositorio.
