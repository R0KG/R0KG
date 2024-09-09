import { View, Text, ScrollView,SafeAreaView } from 'react-native';
import { useState } from 'react';
import { Stack, useRouter } from 'expo-router';

import { COLORS, SIZES } from '../constants';


const Index = () => {
    const router = useRouter();

    return(
        <SafeAreaView>
            <Text>Home</Text>
        </SafeAreaView>
    )


}

export default Index;

