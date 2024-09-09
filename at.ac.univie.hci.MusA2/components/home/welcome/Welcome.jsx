import { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Image,
  FlatList,
} from "react-native";
import { useRouter } from "expo-router";

import styles from "./welcome.style";
import { icons, SIZES } from "../../../constants";

const artParams = [
  "start_date",
  "place_of_origin",
  "has_educational_resources",
];

const Welcome = ({ searchTerm, setSearchTerm, handleClick }) => {
  const router = useRouter();
  const [activeParam, setactiveParam] = useState("");
  const [startDate, setStartDate] = useState("");
  const [placeOfOrigin, setPlaceOfOrigin] = useState("");
  const [hasEducationalResources, setHasEducationalResources] = useState(false);

  return (
    <View>
      <View style={styles.container}>
        <Text style={styles.userName}>Hello Mr</Text>
        <Text style={styles.welcomeMessage}>Find your Art</Text>
      </View>

      <View style={styles.searchContainer}>
        <View style={styles.searchWrapper}>
          <TextInput
            style={styles.searchInput}
            value={searchTerm}
            onChangeText={(text) => setSearchTerm(text)}
            placeholder="What are you looking for?"
          />
        </View>

        <TouchableOpacity style={styles.searchBtn} onPress={() => {
          router.push(`/search/${searchTerm}?startDate=${startDate}&placeOfOrigin=${placeOfOrigin}&hasEducationalResources=${hasEducationalResources}`);
        }}>
          <Image
            source={icons.search}
            resizeMode="contain"
            style={styles.searchBtnImage}
          />
        </TouchableOpacity>
      </View>
      <TextInput
        style={styles.searchInput}
        value={startDate}
        onChangeText={(text) => setStartDate(text)}
        placeholder="Start Date"
        keyboardType="numeric"
      />
      <TextInput
        style={styles.searchInput}
        value={placeOfOrigin}
        onChangeText={(text) => setPlaceOfOrigin(text)}
        placeholder="Place of Origin"
      />
      <TouchableOpacity
        onPress={() => setHasEducationalResources(!hasEducationalResources)}
      >
        <Text>
          {hasEducationalResources
            ? "Educational Resources: Yes"
            : "Educational Resources: No"}  
        </Text>
      </TouchableOpacity>
    </View>
  );
};

export default Welcome;
