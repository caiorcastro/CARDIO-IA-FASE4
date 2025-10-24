
import { Routes, Route, Link, Navigate } from "react-router-dom"
import { useAuth } from "./contexts/AuthContext.jsx"
import Login from "./pages/Login.jsx"
import Patients from "./pages/Patients.jsx"
import Schedule from "./pages/Schedule.jsx"
import Dashboard from "./pages/Dashboard.jsx"
import RouteGuard from "./components/RouteGuard.jsx"

export default function App(){
  const { user, logout } = useAuth()
  return (
    <div style={{fontFamily: "system-ui", padding: 16}}>
      <header style={{display:"flex", gap:12, alignItems:"center"}}>
        <h2 style={{marginRight: "auto"}}>CardioIA Portal</h2>
        <Link to="/">Dashboard</Link>
        <Link to="/patients">Pacientes</Link>
        <Link to="/schedule">Agendamentos</Link>
        {user ? <button onClick={logout}>Sair</button> : <Link to="/login">Entrar</Link>}
      </header>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<RouteGuard><Dashboard/></RouteGuard>} />
        <Route path="/patients" element={<RouteGuard><Patients/></RouteGuard>} />
        <Route path="/schedule" element={<RouteGuard><Schedule/></RouteGuard>} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </div>
  )
}
