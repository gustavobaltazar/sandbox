import { StyleSheet, Text, View } from 'react-native';
import Header from './components/Header'
import Body from './components/Body'
import Footer from './components/Footer'
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Home from './components/Home';
import { Screen } from 'react-native-screens';

const Pilha=createStackNavigator()

export default function Routers() {
  return (
      <NavigationContainer>
        <Pilha.Navigator>
          <Pilha.Screen 
            name='Home'          
            component={Home}
            options={{headerShown:false}}
          />
          <Pilha.Screen 
            name='Header'          
            component={Header}
            options={{headerShown:false}}
          />
          <Pilha.Screen 
            name='Body'          
            component={Body}
            options={{headerShown:false}}
          />
          <Pilha.Screen 
            name='Footer'          
            component={Footer}
            options={{headerShown:false}}
          />
        </Pilha.Navigator>
      </NavigationContainer>
    );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
