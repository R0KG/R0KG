import {useCallback,useState} from 'react'
import { Text,View,SafeAreaView,ScrollView,ActivityIndicator,RefreshControl } from 'react-native'
import { Stack,useRouter, useLocalSearchParams } from 'expo-router'

import { COLORS,icons,SIZES } from '../../constants'
import useFetch from '../../hook/useFetch'


const ArtDetails = () => {
    const params = useLocalSearchParams();
    const router = useRouter();


    const { data, isLoading, error , refetch} = useFetch('art_details', {
        art_id : params.id
    })

  return (
    <SafeAreaView style = {{flex : 1, backgroundColor: COLORS.lightWhite}}>
        <Stack.Screen></Stack.Screen>
    </SafeAreaView>
  )
}

export default ArtDetails