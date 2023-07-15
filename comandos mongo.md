`db` > muestra la base de datos que estamos utilizando

# Insertar un registro:

```
db.alumnos.insertOne({
    nombre: 'Eduardo',
    apellido: 'de Rivero',
    departamento: 'Arequipa'
})
```

# Insertar varios registros:

```
db.alumnos.insertMany([
    {
        nombre: 'Juanita',
        departamento: 'Ica'
    },
    {
        apellido: 'Rodriguez',
        sexo: 'Masculino'
    },
    {
        nombre: 'Rosa',
        apellido: 'Mogrovejo',
        departamento: 'Trujillo',
        sexo: 'Femenino'
    }
])
```

# Devolver los documentos

```
db.alumnos.find()
```

# Utilizando paginacion en nuestro find

```
db.alumnos.find().skip(0).limit(2)
```

# Buscar alumnos con filtro de busqueda

Seria en SQL `SELECT * FROM alumnos WHERE nombre ='Eduardo';`

```
db.alumnos.find({nombre: 'Eduardo' })
```

# Ejercicios

1. Encuentren todas las personas que sean de Arequipa o Ica

   Resultado

   `db.alumnos.find({ $or: [ {departamento: 'Arequipa' }, {departamento: 'Ica'} ] })`

2. Encuentren todas las personas que no sean de Arequipa

   Resultado

   `db.alumnos.find({ departamento: { $ne: 'Arequipa' } })`
   `db.alumnos.find({ departamento: { $not: { $eq: 'Arequipa' } } })`
   ` db.alumnos.find({$and: [{departamento : {$ne: null } }, {departamento: {$ne: 'Arequipa'}} ]})`

3. Encuentren todas las personas Femenino y que se llamane Laura o Rosa

   Resultado  
   `db.alumnos.find({ sexo: 'Femenino', $or: [{nombre:'Laura'}, {nombre:'Rosa'}] })`
