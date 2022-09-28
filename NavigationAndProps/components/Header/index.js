import {View, Text, Button} from 'react-native'
import Styles from './styles'
import Body from '../Body'

export default function Header({navigation}){
    return(
        <View style={{flex:0.2}}>
            <Text style={Styles.txt}>
                Header
            </Text>
            <View>
                <Button 
                    title='Body'
                    onPress={()=>navigation.navigate(Body)}
                />

            </View>
        </View>
    )
}