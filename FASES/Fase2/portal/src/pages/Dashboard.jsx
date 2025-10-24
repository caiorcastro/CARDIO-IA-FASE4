
import { useEffect, useState } from "react"
import { getPatients, getAppointmentsCount } from "../services/api.js"

export default function Dashboard(){
  const [stats, setStats] = useState({ patients:0, appointments:0 })
  useEffect(()=>{
    Promise.all([getPatients(), getAppointmentsCount()])
      .then(([p,a])=> setStats({ patients: p.length, appointments: a }))
  },[])
  return (
    <div>
      <h3>Dashboard</h3>
      <div style={{display:"grid", gridTemplateColumns:"1fr 1fr", gap:12}}>
        <div style={{border:"1px solid #ddd", padding:16, borderRadius:8}}>
          <div>Total de Pacientes</div>
          <div style={{fontSize:28}}>{stats.patients}</div>
        </div>
        <div style={{border:"1px solid #ddd", padding:16, borderRadius:8}}>
          <div>Consultas Agendadas</div>
          <div style={{fontSize:28}}>{stats.appointments}</div>
        </div>
      </div>
    </div>
  )
}
