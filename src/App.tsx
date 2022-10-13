import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './styles/global.css';

export function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1 className='font-bold text-5xl text-violet-500'>Hello World</h1>

      <button className='bg-violet-500 font-medium px-4 py-2 text-white hover:bg-violet-600'>
        Enviar
      </button>
    </>
  )
}


