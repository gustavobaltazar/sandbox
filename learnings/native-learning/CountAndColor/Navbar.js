import { View, Text, StyleSheet } from "react-native"

export const Navbar = () => {
    return (
        <>
            <View style={style.navbar}>
                <Text>Tarefa</Text>
            </View>
        </>
    )
}

const style = StyleSheet.create({
    navbar: {
        flex: 0.1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'red'
    }
})
