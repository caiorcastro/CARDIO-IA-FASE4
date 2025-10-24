
import { useEffect, useState } from "react"
import { getPatients } from "../services/api.js"

export default function Patients(){
  const [rows, setRows] = useState([])
  useEffect(()=>{ getPatients().then(setRows) },[])
  return (
    <div>
      <h3>Pacientes</h3>
      <table>
        <thead><tr><th>Nome</th><th>Idade</th><th>Condição</th></tr></thead>
        <tbody>
          {rows.map((r,i)=>(
            <tr key={i}><td>{r.name}</td><td>{r.age}</td><td>{r.condition}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
