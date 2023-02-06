import { StatusBar } from 'expo-status-bar';
import { ImageBackground, StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <View style={styles.alignLine}>
        <View style={styles.txt1}>
          <ImageBackground source={} resizeMode="cover" style={styles.image}></ImageBackground>
          <Text style={{ color: 'white' }}>Gustavo Baltazar</Text>
        </View>
        <View style={styles.txt2}>
          <Text style={{ color: 'white' }}>Sussy Baka</Text>
        </View>
      </View>
      <View style={styles.alignLine}>
        <View style={styles.txt3}>
          <Text style={{ color: 'white' }}>Sussy Baka</Text>
        </View>
        <View style={styles.txt4}>
          <Text style={{ color: 'white' }}>Sussy Baka</Text>
        </View>
      </View>
    </View >
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '16px',
    flexDirection: 'row',
    width: '100%',
  },

  alignLine: {
    flexDirection: 'column',
  },

  txt1: {
    display: 'flex',
    justifyContent: 'center',
    width: '500px',
    height: '45vh',
    color: 'white',
    backgroundColor: 'blue',
    textAlign: 'center',
  },

  txt2: {
    display: 'flex',
    justifyContent: 'center',
    width: '500px',
    height: '45vh',
    color: 'white',
    backgroundColor: 'red',
    textAlign: 'center',
  },

  txt3: {
    display: 'flex',
    justifyContent: 'center',
    width: '500px',
    height: '45vh',
    color: 'white',
    backgroundColor: 'red',
    textAlign: 'center',
  },

  txt4: {
    display: 'flex',
    justifyContent: 'center',
    width: '500px',
    height: '45vh',
    color: 'white',
    backgroundColor: 'red',
    textAlign: 'center',
  },

});
