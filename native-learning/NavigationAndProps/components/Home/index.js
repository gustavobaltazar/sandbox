import React from 'react'
import { View, Text } from 'react-native'
import Styles from './styles'
import Header from '../Header'
import Body from '../Body'
import Footer from '../Footer'

export default function Home ({ navigation }) {
  return (
    <View style={Styles.container}>
        <Header />
        <Body />
        <Footer />
    </View>
  )
}
