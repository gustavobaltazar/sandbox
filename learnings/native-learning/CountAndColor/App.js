import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import React, { useState } from 'react';
import { Navbar } from './Navbar';
import { Buttton } from './Button';


function Increase({ someCount }) {
  return (
    <Button onPress={someCount}>+</Button>
  )
}

export default function App() {
  const [count, setCount] = useState(0);
  const [color, setColor] = useState("white");

  const changeRed = () => {
    setColor("red")
  }

  const changeBlue = () => {
    setColor("blue")
  }

  const changeGreen = () => {
    setColor("green")
  }

  const reset = () => {
    setColor("white")
  }

  return (
    <>
      <Navbar />
      <View style={[styles.container, {backgroundColor: color}]}>
        {count}
        {/* <button onClick={() => setCount(count + 1)}>+</button> */}
        <Increase someCount={() => setCount(count + 1)} />
        <Buttton func={changeBlue} color="blue" title="Azul" />
        <Buttton func={changeGreen} color="green" title="Verde"/>
        <Buttton func={changeRed} color="red" title="Vermelho"/>
        <Buttton func={reset} color="white" title="Branco"/>
      </View>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    gap: '10px',
  },
  color: {
    backgroundColor: ''
  }
});
