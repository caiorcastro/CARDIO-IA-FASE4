
import { useState } from "react"
import { useAuth } from "../contexts/AuthContext.jsx"
import { useNavigate } from "react-router-dom"

export default function Login(){
  const [username, setUsername] = useState("aluno")
  const [password, setPassword] = useState("123")
  const { login } = useAuth()
  const nav = useNavigate()
  return (
    <div style={{maxWidth:360, margin:"40px auto"}}>
      <h3>Entrar</h3>
      <label>Usuário</label>
      <input value={username} onChange={e=>setUsername(e.target.value)} style={{width:"100%", marginBottom:8}}/>
      <label>Senha</label>
      <input type="password" value={password} onChange={e=>setPassword(e.target.value)} style={{width:"100%", marginBottom:8}}/>
      <button onClick={()=>{ login(username,password); nav("/") }}>Entrar</button>
    </div>
  )
}
