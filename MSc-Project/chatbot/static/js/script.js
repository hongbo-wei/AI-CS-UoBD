function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    document.getElementById('user-input').value = '';
    
    displayMessage(userInput, 'user-message');
    console.log(userInput);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/chat', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            displayMessage(response.response, 'bot-message');
        }
    };
    xhr.send(JSON.stringify({ message: userInput }));
}

function displayMessage(message, className) {
    var conversation = document.getElementById('conversation');
    var messageElement = document.createElement('div');
    messageElement.innerText = message;
    messageElement.classList.add('message', className);
    conversation.appendChild(messageElement);

    // Scroll to the bottom of the conversation window
    conversation.scrollTop = conversation.scrollHeight;
}
