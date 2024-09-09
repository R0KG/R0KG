
import { View, Text, TouchableOpacity, Image } from 'react-native'
import useFetch from '../../../../hook/useFetch';
import styles from './popularartcard.style'

const PopularArtCard = ({item, activeParam, handleCardPress,imageUrl}) => {
  
    const { data, isLoading, error} = useFetch(
      item.id, {}
  );
  return (
    <TouchableOpacity
      style = {styles.container( activeParam, item)}
      onPress={() => handleCardPress(item)}
    >
      <TouchableOpacity style = {styles.logoContainer(activeParam,item)}>
        <Image 
          source={{ uri : imageUrl === 'undef' ? `https://www.artic.edu/iiif/2/${data.image_id}/full/843,/0/default.jpg` : imageUrl}}
          resizeMode='contain'
          style={styles.logoImage}
        />
      </TouchableOpacity>
      <Text style={styles.companyName} numberOfLines={1}>
        {item.title}
      </Text>
    </TouchableOpacity>
  )
}

export default PopularArtCard