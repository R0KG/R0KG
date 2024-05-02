import React from "react";
import { View, Text, Image } from "react-native";

import styles from "./company.style";

const Artwork = ({ artwork }) => {
  return (
    <View style={styles.container}>
      <View style={styles.thumbnailBox}>
        <Image
          source={{
            uri: artwork.thumbnail.lqip,
          }}
          style={styles.thumbnailImage}
        />
      </View>

      <View style={styles.infoBox}>
        <Text style={styles.title}>{artwork.title}</Text>
        <Text style={styles.artist}>{artwork.artist_display}</Text>
        <Text style={styles.date}>{artwork.date_display}</Text>
        <Text style={styles.medium}>{artwork.medium_display}</Text>
        <Text style={styles.dimensions}>{artwork.dimensions}</Text>
      </View>
    </View>
  );
};

export default Artwork;