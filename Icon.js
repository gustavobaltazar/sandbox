import { MaterialCommunityIcons } from '@expo/vector-icons'

const Icon = ( icon, color ) => {
    return (
        <MaterialCommunityIcons style={[styles.icon, {color: color}]} name={icons[icon]} size={23} />
    )
}