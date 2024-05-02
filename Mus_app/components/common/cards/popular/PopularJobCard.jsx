
import { View, Text, TouchableOpacity, Image } from 'react-native'

import styles from './popularjobcard.style'

const PopularJobCard = ({item, activeParam, handleCardPress}) => {
  return (
    <TouchableOpacity
      style = {styles.container( activeParam, item)}
      onPress={() => handleCardPress(item)}
    >
      <TouchableOpacity style = {styles.logoContainer(activeParam,item)}>
        <Image 
          source={{ uri : imageUrl}}
          resizeMode='contain'
          
        />
      </TouchableOpacity>
      <Text style={styles.companyName} numberOfLines={1}>
        {item.title}
      </Text>
    </TouchableOpacity>
  )
}

export default PopularJobCard