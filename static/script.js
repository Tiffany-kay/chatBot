document.getElementById("send-button").addEventListener("click", function() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        addMessage("user", userInput);
        fetchResponse(userInput);
        document.getElementById("user-input").value = "";  // Clear input field after sending
    }
});

function addMessage(sender, text) {
    const chatbox = document.getElementById("chatbox");
    const messageDiv = document.createElement("div");
    messageDiv.className = sender + "-message";
    messageDiv.textContent = text;
    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight;  // Scroll to the bottom of the chatbox
}

function fetchResponse(userInput) {
    fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: 'user_input=' + encodeURIComponent(userInput)
    })
    .then(response => response.json())
    .then(data => {
        addMessage("bot", data.response);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
