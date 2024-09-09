import React from "react";
import { View, Text, Image } from "react-native";

import styles from "./company.style";

const Artwork = ({ artwork }) => {
  return (
    <View >
      

      <View >
        <Text >{artwork.title}</Text>
        <Text >{artwork.artist_display}</Text>
        <Text >{artwork.date_display}</Text>
        <Text >{artwork.medium_display}</Text>
        <Text >{artwork.dimensions}</Text>
      </View>
    </View>
  );
};

export default Artwork;