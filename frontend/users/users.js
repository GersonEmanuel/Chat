const SOCKET_URL = "ws://127.0.0.1:8000/ws"
const username = prompt("inform us a username")

async function createuser(event){
    event.preventDefault();
    try {
        const response = await fetch(SOCKET_URL, {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(username)
        });

        if (!response.ok){
            throw new Error(`erro: ${response.status}`)
        }

        const resultado = await response.json();
        alert(resultado.message)
    } catch (error){
        alert("error to create the user");
    }
}