const SOCKET_URL = "ws://127.0.0.1:8000/users"

async function createuser(event){
    event.preventDefault();
    try {
        user = document.querySelector("#user")
        const response = await fetch(SOCKET_URL, {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username})
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


async function getusers(event){
    event.preventDefault();
    const response = await fetch(SOCKET_URL)
    if(!response.ok){
        throw new Error("error to get users")
    }

    const users = await response.json();

    return users;
}

document.addEventListener("submit", createuser)