import axios from 'axios'
import { useEffect, useState } from 'react'

export const ListBosses = () => {
  const [apiresult, setApiresult] = useState([{}])
  const base = "http://127.0.0.1:8000";

  const FetchAxios = () => {
    axios.get("http://127.0.0.1:8000/list/boss_show/list_bosses/")
      .then(response => {
        setApiresult(response.data)
      })
      console.log(apiresult)
  }

  useEffect(() => {
    FetchAxios()
  }, [])

  return (
    <div className="flex flex-col h-screen justify-center items-center bg-slate-800">
      <div className="text-6xl text-white mb-4">Elden Wiki</div>
      <div className="flex gap-32">
        {apiresult.map((item, index) => (
          <div className="bg-white w-96" key={index}>
            <img className="w-96 h-96" src={base + item.boss_image} />
            <div className="text-center text-3xl mt-4">
              Name:  {item.name}
            </div>
            <div className="text-center text-2xl mb-4">
              Location: {item.location}
            </div>
            <div className="text-center text-2xl">
              Loot: {item.loot}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}