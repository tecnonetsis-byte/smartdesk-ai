import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { BrainCircuit, PlusCircle, RefreshCw } from "lucide-react";
import "./styles.css";

const API = "http://localhost:8000/api/v1/tickets";

function App() {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState({ requester_name: "", email: "", subject: "", description: "" });

  async function loadTickets() {
    const res = await fetch(API);
    setTickets(await res.json());
  }

  useEffect(() => { loadTickets(); }, []);

  async function submit(e) {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      if (!res.ok) throw new Error("No se pudo registrar la solicitud");
      setForm({ requester_name: "", email: "", subject: "", description: "" });
      await loadTickets();
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="shell">
      <header className="hero">
        <div className="brand"><BrainCircuit size={34} /><span>SmartDesk AI</span></div>
        <h1>Soporte empresarial con clasificación inteligente</h1>
        <p>Registra solicitudes y obtén una categoría y prioridad sugeridas por IA.</p>
      </header>

      <section className="grid">
        <form className="panel" onSubmit={submit}>
          <div className="panel-title"><PlusCircle size={20}/> Nueva solicitud</div>
          <label>Nombre<input required minLength="2" value={form.requester_name} onChange={e=>setForm({...form, requester_name:e.target.value})}/></label>
          <label>Correo<input required type="email" value={form.email} onChange={e=>setForm({...form, email:e.target.value})}/></label>
          <label>Asunto<input required minLength="3" value={form.subject} onChange={e=>setForm({...form, subject:e.target.value})}/></label>
          <label>Descripción<textarea required minLength="5" rows="5" value={form.description} onChange={e=>setForm({...form, description:e.target.value})}/></label>
          <button disabled={loading}>{loading ? "Analizando..." : "Registrar y clasificar"}</button>
        </form>

        <section className="panel">
          <div className="panel-title"><span>Solicitudes recientes</span><button className="ghost" onClick={loadTickets}><RefreshCw size={16}/></button></div>
          <div className="tickets">
            {tickets.length === 0 && <p className="muted">Todavía no hay solicitudes registradas.</p>}
            {tickets.map(ticket => (
              <article className="ticket" key={ticket.id}>
                <div className="ticket-head"><strong>#{ticket.id} {ticket.subject}</strong><span className={`priority ${ticket.predicted_priority.toLowerCase()}`}>{ticket.predicted_priority}</span></div>
                <p>{ticket.description}</p>
                <div className="meta"><span>{ticket.predicted_category}</span><span>{Math.round(ticket.confidence*100)}% confianza</span><span>{ticket.status}</span></div>
                {ticket.manual_review && <div className="review">Requiere revisión manual</div>}
              </article>
            ))}
          </div>
        </section>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App/>);
