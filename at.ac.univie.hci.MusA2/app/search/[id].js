import {React,  useEffect, useState } from 'react';
import { ActivityIndicator, FlatList, Image, TouchableOpacity, View } from 'react-native';
import { Stack, useRouter, usePathname, useLocalSearchParams } from 'expo-router';
import { Text, SafeAreaView } from 'react-native';
import axios from 'axios';


import { ScreenHeaderBtn } from '../../components';
import { COLORS, icons, SIZES } from '../../constants';
import styles from '../../styles/search';
import PopularJobCard from '../../components/common/cards/popular/PopularArtCard'
import useFetch from '../../hook/useFetch';
const ArtSearch = () => {
    const pathname = usePathname();
    const searchParams = useLocalSearchParams();
    const router = useRouter();

    const startDate = searchParams.startDate;
    const placeOfOrigin = searchParams.placeOfOrigin;
    const hasEducationalResources = searchParams.hasEducationalResources;
    
    const [searchResult, setSearchResult] = useState([]);
    const [searchLoader, setSearchLoader] = useState(false);
    const [searchError, setSearchError] = useState(null);
    const [page, setPage] = useState(1);
    

    const handleSearch = async () => {
        setSearchLoader(true);
        setSearchResult([]);    
    
        let url = `https://api.artic.edu/api/v1/artworks/search?q=${searchParams.id}`;
        let firstTermAdded = false; // Track if any term has been added
      
        if (startDate) {
          url += `&query[term][date_start]=${startDate}`;
          firstTermAdded = true;
        }
        if (placeOfOrigin) {
          url += `${firstTermAdded ? '&' : '&query'}[match][place_of_origin]=${placeOfOrigin}`;
          firstTermAdded = true;
        }
        if (hasEducationalResources) {
          url += `${firstTermAdded ? '&' : '&query'}[term][has_educational_resources]=true`;
          firstTermAdded = true;
        }
        url += `&page=${page.toString()}`;
      


    
        try {
            const options = {
                method: 'GET',
                url: url, 
              }
            console.log(options)
            const response = await axios.request(options);
            setSearchResult(response.data.data);
        } catch (error) {
            setSearchError(error);
            console.log(error);
        } finally {
            setSearchLoader(false);
        }
    };

    const handlePagination = (direction) => {
        if (direction === 'left' && page > 1) {
            setPage(page - 1);
            handleSearch();
        } else if (direction === 'right') {
            setPage(page + 1);
            handleSearch();
        }
    };

    useEffect(() => {
        handleSearch();
    }, []);
    const { temp, isLoading, error} = useFetch(
        searchParams.id, {}
    );
    return (
        <SafeAreaView style={{ flex: 1, backgroundColor: COLORS.lightWhite }}>
            <Stack.Screen
                options={{
                    headerStyle: { backgroundColor: COLORS.lightWhite },
                    headerShadowVisible: false,
                    headerLeft: () => (
                        <ScreenHeaderBtn
                            iconUrl={icons.left}
                            dimension='60%'
                            handlePress={() => router.back()}
                        />
                    ),
                    headerTitle: "",
                }}
            />
        
            <FlatList
                data={searchResult}
                renderItem={({ item }) => {
                    
                    
                    return (
                    <PopularJobCard
                        item={item}
                        handleCardPress={() => router.push(`/art_details/${item.id}`)}
                        imageUrl={'undef'}                    />
                    );
                }}
                keyExtractor={(item) => item.id}
                contentContainerStyle={{ padding: SIZES.medium, rowGap: SIZES.medium }}
                ListHeaderComponent={() => (
                    <>
                        <View style={styles.container}>
                            <Text style={styles.searchTitle}>{searchParams.id}</Text>
                            <Text style={styles.noOfSearchedJobs}>Artwork Results</Text>
                        </View>
                        <View style={styles.loaderContainer}>
                            {searchLoader ? (
                                <ActivityIndicator size='large' color={COLORS.primary} />
                            ) : searchError && (
                                <Text>Oops something went wrong</Text>
                            )}
                        </View>
                    </>
                )}
                ListFooterComponent={() => (
                    <View style={styles.footerContainer}>
                        <TouchableOpacity
                            style={styles.paginationButton}
                            onPress={() => handlePagination('left')}
                        >
                            <Image
                                source={icons.chevronLeft}
                                style={styles.paginationImage}
                                resizeMode="contain"
                            />
                        </TouchableOpacity>
                        <View style={styles.paginationTextBox}>
                            <Text style={styles.paginationText}>{page}</Text>
                        </View>
                        <TouchableOpacity
                            style={styles.paginationButton}
                            onPress={() => handlePagination('right')}
                        >
                            <Image
                                source={icons.chevronRight}
                                style={styles.paginationImage}
                                resizeMode="contain"
                            />
                        </TouchableOpacity>
                    </View>
                )}
            />
        </SafeAreaView>
    );
};

export default ArtSearch;