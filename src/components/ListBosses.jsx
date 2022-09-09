import axios from 'axios'
export const ListBosses = () => {

  const api = axios.create({
    baseURL: `http://127.0.0.1:8000/list/boss_show/list_bosses/`
  })
  
  function Api(){
    api.get('/').then(res => {
      console.log(res.data)
    })
  }
  return (
    <>
      <h1 className="text-red-500">bobo</h1>

    </>
  )
}