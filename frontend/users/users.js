const API_URL = "http://localhost:8000/users/";


async function createuser(event){
    event.preventDefault();
    try {
        user_input = document.querySelector("#user")
        user = user_input.value;
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({user})
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
    const response = await fetch(API_URL)
    if(!response.ok){
        throw new Error("error to get users")
    }

    const users = await response.json();

    return users;
}


async function add_user_to_p(){
    const div = document.querySelector("#users");
    const users = getusers();

    users.forEach(user => {
        const p = document.createElement("p");
        p.innerText(`${user}`)
    })

}

document.querySelector("#senduser").addEventListener("submit", createuser)