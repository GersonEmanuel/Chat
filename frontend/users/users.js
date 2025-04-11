const API_URL = "http://localhost:8000/users/";


async function createuser(event){
    event.preventDefault();
    try {
        user_input = document.querySelector("#user").value
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username: user_input})
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


async function getusers(){
    const response = await fetch(API_URL)
    if(!response.ok){
        throw new Error("error to get users")
    }

    const users = await response.json();

    return users;
}


async function add_user_to_p(){
    const div = document.querySelector("#users");
    const users = await getusers();

    users.forEach(user => {
        const p = document.createElement("p");
        p.innerText = user.username;
        div.appendChild(p);
    })

}

document.addEventListener("DOMContentLoaded", add_user_to_p)
document.querySelector("#senduser").addEventListener("submit", createuser)
