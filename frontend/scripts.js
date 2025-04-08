const username = prompt("inform us a username")
const chat = document.querySelector("#chat")
const input = document.querySelector("#messageInput")
const socket = new WebSocket("ws://localhost:8000/ws")



socket.onmessage = function(event) {
    const msg = document.createElement("p");
    msg.innerText = event.data;
    chat.appendChild(msg);

};

function sendMessage() {
    const message = input.value;
    socket.send(message);
    input.value = '';
}

input.addEventListener("keypress", function(press) {
    if (press.key == "Enter"){
        sendMessage();
    }
})