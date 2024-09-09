import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';

const ArtTabs = ({ tabs, activeTab, setActiveTab }) => {
  return (
    <View>
      {tabs.map((tab, index) => (
        <TouchableOpacity key={index} onPress={() => setActiveTab(tab)}>
          <Text style={{ fontSize: 16, color: activeTab === tab ? '#007AFF' : '#666' }}>
            {tab}
          </Text>
        </TouchableOpacity>
      ))}
    </View>
  );
};

export default ArtTabs;