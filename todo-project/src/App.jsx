import { useEffect } from 'react'
import { useState } from 'react'
import reactLogo from './assets/react.svg'

function App() {
  const [todos, setTodos] = useState([])
  const [message, setMessage] = useState('')


  return(
    <div className="bg-red-900">
        <input placeholder="Digite o TODO" type="text" value={message} onChange={(event) => setMessage(event.target.value)} />
        <button onClick={()=> setTodos( todos.concat({
          task: message,
          isComplete: false
        }))}>Create</button>
        {console.log(JSON.stringify(todos))}
        <ul>
          {todos.map((todo) => <li className='text-white'>{ todo.task } <button></button></li>)} 
        </ul>
    </div>
  )
}


export default App
