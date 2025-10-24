
import { createContext, useContext, useEffect, useState } from "react"

const AuthContext = createContext(null)

export function AuthProvider({ children }){
  const [user, setUser] = useState(()=>{
    const raw = localStorage.getItem("cardioia_jwt")
    return raw ? { name:"Aluno", token: raw } : null
  })

  function login(username, password){
    const fake = btoa(username + ":" + password)
    localStorage.setItem("cardioia_jwt", fake)
    setUser({ name: username, token: fake })
  }
  function logout(){
    localStorage.removeItem("cardioia_jwt")
    setUser(null)
  }

  return <AuthContext.Provider value={{ user, login, logout }}>{children}</AuthContext.Provider>
}

export function useAuth(){
  return useContext(AuthContext)
}
