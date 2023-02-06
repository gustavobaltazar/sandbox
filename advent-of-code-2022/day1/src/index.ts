import * as fs from 'fs'
import { resolve } from 'path';

fs.readFile(resolve(__dirname, "./inputs.txt"), (err: any, data: any) => {
    if (err) console.log(err)

    let total: number[] = []
    let aux: number = 0

    data.toString().split('\n').map((item: string) => {
        if (item.length > 1) {
            let auxSim: number = +item.split('\r')[0]
            aux = auxSim + aux
        } else {
            total.push(aux)
            aux = 0
        }
    })

    let largest = total.sort((a, b) => a - b).reverse()[0]

    console.log(largest)
});