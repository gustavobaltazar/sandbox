import React from 'react'
import {View, Text} from 'react-native'
import Styles from './styles'

export default function Body({navigation}){
  return(
    <View style={Styles.container}>
      <Text style={Styles.txt}>
        Body
      </Text>      
    </View>
  )
}