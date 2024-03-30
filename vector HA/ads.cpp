#include <iostream>


template <typename Key, std::size_t N = 3>
class ADS_set {
    // Existing ADS_set members...

    public:
    class Iterator {
        private:
        Bucket** buckets; // Pointer to the array of bucket pointers in ADS_set
        size_type bucketIndex; // Current bucket index
        size_type elemIndex; // Current element index within the bucket
        size_type directorySize; // Size of the directory

        public:
        // Constructor
        Iterator(Bucket** b, size_type bucketIdx, size_type elemIdx, size_type dirSize)
            : buckets(b), bucketIndex(bucketIdx), elemIndex(elemIdx), directorySize(dirSize) {
            skipEmptyBuckets();
        }

        // Dereference operator
        const Key& operator*() const {
            return buckets[bucketIndex]->get_value(elemIndex);
        }

        // Increment operator (prefix)
        Iterator& operator++() {
            if (++elemIndex >= buckets[bucketIndex]->get_size()) {
                elemIndex = 0;
                do {
                    ++bucketIndex;
                } while (bucketIndex < directorySize && buckets[bucketIndex]->get_size() == 0);
            }
            return *this;
        }

        // Equality check
        bool operator==(const Iterator& other) const {
            return bucketIndex == other.bucketIndex && elemIndex == other.elemIndex;
        }

        // Inequality check
        bool operator!=(const Iterator& other) const {
            return !(*this == other);
        }

        private:
        // Helper function to skip empty buckets
        void skipEmptyBuckets() {
            while (bucketIndex < directorySize && buckets[bucketIndex]->get_size() == 0) {
                ++bucketIndex;
            }
        }
    };

    // Existing ADS_set members...

    // Iterator begin and end functions
    Iterator begin() {
        return Iterator(buckets, 0, 0, directory_size);
    }

    Iterator end() {
        return Iterator(buckets, directory_size, 0, directory_size);
    }

    // Other ADS_set members...
};
