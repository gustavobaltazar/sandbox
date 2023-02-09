import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { Botao } from './Botao';

export default function App() {
  const logar = () => {
    alert("Logou")
  }
  const logout = () => {
    alert("Logout sucessfully!")
  }
  return (
    <View style={styles.container}>
      <Botao bg="primary" icon="login" onPress={logar}>
        Login
      </Botao>
      <Botao bg="secondary"  icon="logout" origin="left" onPress={logout}>
        Logout
      </Botao>
      <StatusBar style="auto" />
    </View>
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
