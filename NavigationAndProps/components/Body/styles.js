import { StyleSheet } from "react-native";

export default StyleSheet.create({
    container:{
        flex:1,
        backgroundColor: 'blue',
        alignItems:'center',
        justifyContent:'center',
      },
      caixa1:{
        flex:0.45,
        backgroundColor:'#0f0',
        width:'90%',
        alignItems:'center',
      },
      caixa2:{
        backgroundColor:'#080',
        width:200,
      },
      txt:{
        fontWeight:'bold',
        fontSize: 30,
      },
      caixa3:{
        border: 'solid 1px #444',
        width:'60%',
        margin: 10,
        padding:10,
        textAlign:"center",
      },
      botao:{
        margin:10,
        width:'50%',
      }
})