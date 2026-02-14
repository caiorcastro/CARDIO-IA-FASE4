
export async function getPatients(){
  // Fake base local
  return [
    { name: "Maria Silva", age: 62, condition: "Hipertensão" },
    { name: "João Souza", age: 55, condition: "Angina estável" },
    { name: "Ana Lima", age: 48, condition: "Insuficiência cardíaca" },
  ]
}

export async function getAppointmentsCount(){
  return 7
}
