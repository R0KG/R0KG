import {useState} from 'react'
import { View, Text, TouchableOpacity,FlatList,ActivityIndicator } from 'react-native'
import { useRouter } from 'expo-router'

import { COLORS,SIZES } from '../../../constants'
import styles from './populararts.style'
import PopularArtCard from '../../common/cards/popular/PopularArtCard'

import useFetch from '../../../hook/useFetch'

const Populararts = () => {

  const router = useRouter();
  const { data, isLoading, error} = useFetch(
      '', {}
  );
  const [activeParam, setactiveParam] = useState();

  const handleCardPress = (item) => {
    router.push(`/art_details/${item.id}`);
    setactiveParam(item.id);
  };

  return (
    <View style = {styles.container}>
      <View style = {styles.header}>
        <Text style= {styles.headerTitle}>Popular Art</Text>
        <TouchableOpacity>
          <Text style = {styles.headerBtn}> Show all</Text>
        </TouchableOpacity>
      </View>

      <View style = {styles.cardsContainer}>
        {isLoading ? (
          <ActivityIndicator size='large' color={COLORS.primary} />
        ) : error ? (
          <Text> Something went wrong</Text>
        ): (
          <FlatList 
            data={data}
            renderItem={ ({item}) => (
              <PopularArtCard 
                item = {item}
                handleCardPress={handleCardPress}
                imageUrl={`https://www.artic.edu/iiif/2/${item.image_id}/full/843,/0/default.jpg`}
              />
              
            )}
            keyExtractor={(item) => item.id}
            contentContainerStyle = {{columnGap : SIZES.medium}}
            horizontal
          />  
        )}

      </View>
    </View>
  )
}

export default Populararts