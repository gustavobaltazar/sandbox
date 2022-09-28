import React, { useState } from 'react'
import { Text, View, Button, TextInput } from 'react-native'
import Estilos from './styles'
import Somar from './../Calcule'
export default function Body({ navigation }, c) {
  const [cont, setCont] = useState(0)
  const contar = () => {
    setCont(cont + 1)
  }
  const [resultado, setResultado] = useState('')
  const [operacao, setOperacao] = useState('')
  const [valorA, setValorA] = useState(0)
  const [valorB, setValorB] = useState(0)

  const operar = () => setResultado(eval(operacao))

  const [cor, setCor] = useState('write')
  function cores(type) {
    switch (type) {
      case 'red':
        return 'red'
      case 'green':
        return 'green'
      case 'blue':
        return 'blue'
      default:
        return 'write'
    }
  }

  return (
    <View style={{
      backgroundColor: cores(cor),
      alignItems: 'center',
      justifyContent: 'center',

    }}>
      <View style={Estilos.caixa2}>
        <Button title='Contador' onPress={() => contar()} />
      </View>
      <Text style={Estilos.txt}>{cont}</Text>
      <TextInput
        placeholder='Digite um cálculo '
        keyboardType='numeric'
        style={Estilos.caixa3}
        value={String(operacao)}
        onChangeText={m => {
          setOperacao(m)
        }}
      />
      <TextInput
        placeholder='Resultado'
        value={String(resultado)}
        style={Estilos.caixa3}
      />
      <View style={Estilos.botao}>
        <Button title='=' onPress={() => operar()} />
      </View>
      <View style={Estilos.botao}>
        <Button title='Vermelho' onPress={() => setCor('red')} />
      </View>
      <View style={Estilos.botao}>
        <Button title='Verde' onPress={() => setCor('green')} />
      </View>
      <View style={Estilos.botao}>
        <Button title='Azul' onPress={() => setCor('blue')} />
      </View>
      <View>
        <TextInput
          style={Estilos.caixa3}
          placeholder='Digite o Valor A'
          keyboardType='numeric'
          onChangeText={a => {
            setValorA(a)
          }}>
        </TextInput>
        <TextInput
          style={Estilos.caixa3}
          placeholder='Digite o Valor B'
          keyboardType='numeric'
          onChangeText={b => {
            setValorB(b)
          }}>
        </TextInput>
        <View>
          <Text style={Estilos.caixa3}>
            <Somar valora={valorA} valorb={valorB} />
          </Text>
        </View>
      </View>
    </View>
  )
}
