import { View, Text, StyleSheet, TouchableOpacity } from 'react-native'
import colors from './config/colors'
import icons from './config/icons'
import { StatusBar } from 'expo-status-bar'
import { MaterialCommunityIcons } from '@expo/vector-icons'


export function Botao({ children, bg, icon, origin, color, onPress }) {
    return (
        <TouchableOpacity style={[styles.button, { backgroundColor: colors[bg], flexDirection: origin === 'left' ? 'row-reverse' : 'row' }]} onPress={onPress}>
            <Text style={[styles.textButton, { color: color }]}>
                {children}
            </Text>
            <MaterialCommunityIcons name={icons[icon]} size={23} />
        </TouchableOpacity>
    )
}
const styles = StyleSheet.create({
    button: {
        backgroundColor: colors.secundary,
        fontSize: 14,
        padding: 10,
        marginHorizontal: 10,
        borderRadius: 10,
        margin: 10,
    },
    textButton: {
        color: "#fff",
    }
})