
import { useReducer, useState } from "react"

function reducer(state, action){
  switch(action.type){
    case "set": return { ...state, [action.key]: action.value }
    case "reset": return { patient:"", date:"", notes:"" }
    default: return state
  }
}

export default function Schedule(){
  const [state, dispatch] = useReducer(reducer, { patient:"", date:"", notes:"" })
  const [items, setItems] = useState([])
  function submit(){
    setItems([...items, state])
    dispatch({type:"reset"})
  }
  return (
    <div>
      <h3>Agendar Consulta</h3>
      <input placeholder="Paciente" value={state.patient} onChange={e=>dispatch({type:"set", key:"patient", value:e.target.value})}/>
      <input type="datetime-local" value={state.date} onChange={e=>dispatch({type:"set", key:"date", value:e.target.value})}/>
      <textarea placeholder="Observações" value={state.notes} onChange={e=>dispatch({type:"set", key:"notes", value:e.target.value})}/>
      <button onClick={submit}>Agendar</button>
      <h4>Agendamentos</h4>
      <ul>
        {items.map((it,i)=>(<li key={i}>{it.patient} — {it.date} — {it.notes}</li>))}
      </ul>
    </div>
  )
}
