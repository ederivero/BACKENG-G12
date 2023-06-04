const email = document.getElementById('email')
const password = document.getElementById('password')
const iniciarSesionButton = document.getElementById('btn-iniciar-sesion')

iniciarSesionButton.addEventListener('click', async (e) => {
    e.preventDefault()
    const data = {
        email: email.value,
        password: password.value
    }
    console.log(data)

    const resultado = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    })

    const json = await resultado.json()
    console.log(json)
})