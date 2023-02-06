import { View, Text, StyleSheet, Button } from "react-native"


export const Buttton = (props) => {
    return (
        <>
            <View style={{}}>
                <Button onPress={props.func} color={props.color} title={props.title}></Button>
            </View>
        </>
    )
}
