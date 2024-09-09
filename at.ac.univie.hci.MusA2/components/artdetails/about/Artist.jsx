import React from 'react';
import { View, Text, Image } from 'react-native';

const Artist = ({ artistImage, artTitle, artistName }) => {
  return (
    <View>
      <Image source={{ uri: artistImage }} style={{ width: 100, height: 100 }} />
      <Text style={{ fontSize: 18, fontWeight: 'bold' }}>{artTitle}</Text>
      <Text style={{ fontSize: 16 }}>{artistName}</Text>
    </View>
  );
};

export default Artist;