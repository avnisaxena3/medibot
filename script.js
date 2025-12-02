const chatWindow = document.getElementById("chat-window");
const typingIndicator = document.getElementById("typing-indicator");

document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", e => {
    if (e.key === "Enter") sendMessage();
});

// Load chat history on startup
window.onload = () => {
    const history = JSON.parse(localStorage.getItem("chatHistory")) || [];
    history.forEach(msg => appendMessage(msg.text, msg.sender));
};

// Save chat history
function saveHistory(text, sender) {
    const history = JSON.parse(localStorage.getItem("chatHistory")) || [];
    history.push({ text, sender });
    localStorage.setItem("chatHistory", JSON.stringify(history));
}

function appendMessage(text, sender) {
    const bubble = document.createElement("div");
    bubble.classList.add("message", sender === "user" ? "user-message" : "bot-message");
    bubble.innerHTML = text;
    chatWindow.appendChild(bubble);
    chatWindow.scrollTop = chatWindow.scrollHeight;
    saveHistory(text, sender);
}

function showTypingIndicator(show) {
    typingIndicator.style.display = show ? "flex" : "none";
}

async function sendMessage() {
    const input = document.getElementById("user-input");
    const text = input.value.trim();
    if (!text) return;

    appendMessage(text, "user");
    input.value = "";
    showTypingIndicator(true);

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: text })
        });

        const data = await response.json();
        showTypingIndicator(false);

        const res = data.result ? data.result : data;

        appendMessage(renderMedicalCard(res), "bot");

    } catch (error) {
        showTypingIndicator(false);
        appendMessage("⚠️ Error connecting to server.", "bot");
        console.error(error);
    }
}


function renderMedicalCard(res) {
    return `
    <div class="card"><b>Condition:</b> ${res.condition || "N/A"}</div>
    <div class="card"><b>Probable Causes:</b> ${(res.probable_causes || []).join(", ")}</div>
    <div class="card"><b>Recommended Drugs:</b> ${(res.recommended_drugs || []).join(", ")}</div>
    <div class="card"><b>Precautions:</b> ${(res.precautions || []).join(", ")}</div>
    <div class="card"><b>When to Visit Doctor:</b> ${(res.when_to_visit_doctor || []).join(", ")}</div>
    <div class="card"><b>Sources:</b> ${(res.sources || []).join(", ")}</div>
    <div class="card"><b>⚠️ Disclaimer:</b> ${res.disclaimer || "N/A"}</div>
    `;
}



/* ---------- DARK MODE TOGGLE ---------- */
document.getElementById("toggle-theme").addEventListener("click", () => {
    document.body.classList.toggle("dark");
    document.body.classList.toggle("light");

    document.getElementById("toggle-theme").innerText =
        document.body.classList.contains("dark") ? "☀️ Light Mode" : "🌙 Dark Mode";
});
