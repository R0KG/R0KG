import React from 'react';
import { View, Text } from 'react-native';

const ArtAbout = ({ info }) => {
  return (
    <View>
      <Text style={{ fontSize: 16 }}>{info}</Text>
    </View>
  );
};

export default ArtAbout;