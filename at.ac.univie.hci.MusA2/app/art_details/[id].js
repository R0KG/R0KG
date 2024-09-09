import { useCallback, useState } from "react";
import {
  Text,
  View,
  SafeAreaView,
  ScrollView,
  ActivityIndicator,
  RefreshControl,
  Image
} from "react-native";
import { Stack, useRouter, useLocalSearchParams } from "expo-router";
import { PinchGestureHandler, State } from 'react-native-gesture-handler';

import { COLORS, icons, SIZES } from "../../constants";
import useFetch from "../../hook/useFetch";


const ArtDetails = () => {
  const params = useLocalSearchParams();
  const router = useRouter();

  const { data, isLoading, error, refetch } = useFetch(params.id, {});

  const [scale, setScale] = useState(1);

  const onPinchGestureEvent = useCallback((event) => {
    if (event.nativeEvent.state === State.ACTIVE) {
      setScale(event.nativeEvent.scale);
    } else if (event.nativeEvent.state === State.END) {
      setScale(1);
    }
  }, []);
  
  const FONT = {
    regular: 'DMRegular',
    bold: 'DMBold',
    italic: 'DMIitalic',
    // add more font families as needed
  };
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: COLORS.lightWhite }}>
      <Text 
        style={{
          fontSize: SIZES.medium,
          fontFamily: FONT.regular,
          color: COLORS.gray,
          marginBottom: SIZES.small, // add some margin bottom for spacing
        }}
      >{data.title}</Text>
      <Text 
        style={{
          fontSize: SIZES.medium,
          fontFamily: FONT.regular,
          color: COLORS.gray,
          marginBottom: SIZES.small, // add some margin bottom for spacing
        }}
      >{data.artist_display}</Text>
      <Text 
        style={{
          fontSize: SIZES.medium,
          fontFamily: FONT.regular,
          color: COLORS.gray,
          marginBottom: SIZES.small, // add some margin bottom for spacing
        }}
      >{data.date_display}</Text>
      <Text 
        style={{
          fontSize: SIZES.medium,
          fontFamily: FONT.regular,
          color: COLORS.gray,
          marginBottom: SIZES.small, // add some margin bottom for spacing
        }}
      >{data.medium_display}</Text>
      <Text 
        style={{
          fontSize: SIZES.medium,
          fontFamily: FONT.regular,
          color: COLORS.gray,
        }}
      >{data.dimensions}</Text>
      <PinchGestureHandler
        onGestureEvent={onPinchGestureEvent}
        onHandlerStateChange={onPinchGestureEvent}
      >
<PinchGestureHandler
  minScale={0.5}
  maxScale={2}
  onGestureEvent={onPinchGestureEvent}
  onHandlerStateChange={onPinchGestureEvent}
>
<Image 
  source={{ uri : `https://www.artic.edu/iiif/2/${data.image_id}/full/843,/0/default.jpg`}}
  style={{
    width: 300, // fixed width
    height: 300, // fixed height
    transform: [{ scale }],
    borderRadius: SIZES.medium,
    borderWidth: 1,
    borderColor: COLORS.gray,
    resizeMode: 'contain',
  }}
/>
</PinchGestureHandler>
      </PinchGestureHandler>
    </SafeAreaView>
  );
};

export default ArtDetails;