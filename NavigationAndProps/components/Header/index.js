import {View, Text, Button} from 'react-native'
import Styles from './styles'
import Body from '../Body'

export default function Header({navigation}){
    return(
        <View style={Styles.container}>
            <Text style={Styles.txt}>
                Header
            </Text>
        </View>
    )
}