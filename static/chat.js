
(() => {
  const root = document.getElementById("chatbot-root");
  const toggle = document.getElementById("chat-toggle");
  const win = document.getElementById("chat-window");
  const closeBtn = document.getElementById("chat-close");
  const messagesEl = document.getElementById("chat-messages");
  const form = document.getElementById("chat-form");
  const input = document.getElementById("chat-input");

  // Keep messages on the client; send the list to the backend each turn
  const messages = [
    { role: "assistant", content: "Olá! Sou seu assistente. Em que posso ajudar hoje?" }
  ];

  function render() {
    messagesEl.innerHTML = "";
    messages.forEach(m => {
      const div = document.createElement("div");
      div.className = "msg " + (m.role === "user" ? "user" : "assistant");
      div.textContent = m.content;
      messagesEl.appendChild(div);
    });
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function show() { win.classList.remove("hidden"); toggle.style.display = "none"; }
  function hide() { win.classList.add("hidden"); toggle.style.display = "inline-flex"; }

  toggle.addEventListener("click", show);
  closeBtn.addEventListener("click", hide);

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text) return;

    messages.push({ role: "user", content: text });
    render();
    input.value = "";
    input.focus();

    // optimistic typing indicator
    const typing = { role: "assistant", content: "digitando..." };
    messages.push(typing);
    render();

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages })
      });
      const data = await res.json();
      messages.pop(); // remove typing
      if (data.reply) {
        messages.push({ role: "assistant", content: data.reply });
      } else {
        messages.push({ role: "assistant", content: "Desculpe, ocorreu um erro." });
        console.error(data);
      }
    } catch (err) {
      messages.pop();
      messages.push({ role: "assistant", content: "Erro de rede ao contatar o servidor." });
      console.error(err);
    }
    render();
  });

  // start hidden; open on click
  render();
})();
