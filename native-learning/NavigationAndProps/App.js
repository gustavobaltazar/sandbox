import { View, StyleSheet } from 'react-native'
import Routers from './routers'
import Header from './components/Header'
import Body from './components/Body'
import Footer from './components/Footer'

export default function App () {
  return (
    <View style={styles.container}>
      <Routers />
    </View>
  )
}

const styles = StyleSheet.create({
  container:{
    flex:1,
    backgroundColor:'#099'
  }
})