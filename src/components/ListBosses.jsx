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
  }

  useEffect(() => {
    FetchAxios()
  }, [])

  return (
    <div>
      {apiresult.map((item, index) => (
        <div key={index}>
          {item.name} = {item.location}
          <img src={base+item.boss_image} />
        </div>
      ))}
    </div>
  )
}