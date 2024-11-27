import math
from collections import defaultdict
import itertools
import binascii

class MultiMessageXORCracker:
        def __init__(self, hex_messages):
            """
            Initialize the cracker with multiple hex-encoded messages
            
            Args:
                hex_messages (list): List of hex-encoded ciphertext messages
            """
            # Convert hex messages to bytes
            self.messages = [bytes.fromhex(msg) for msg in hex_messages]
            
            # Find the shortest message length
            self.min_length = min(len(msg) for msg in self.messages)
            
            # Truncate all messages to the shortest length
            self.messages = [msg[:self.min_length] for msg in self.messages]
            
            self.key = None
            self.plaintexts = None

        def hamming_distance(self, bytes1, bytes2):
            """
            Calculate Hamming distance between two byte strings
            
            Args:
                bytes1 (bytes): First byte string
                bytes2 (bytes): Second byte string
            
            Returns:
                int: Hamming distance (number of differing bits)
            """
            return sum(bin(a ^ b).count('1') for a, b in zip(bytes1, bytes2))

        def guess_key_length(self, max_keysize=40):
            """
            Guess the key length using Hamming distance between messages
            
            Args:
                max_keysize (int): Maximum key length to test
            
            Returns:
                int: Most likely key length
            """
            distances = []
            
            for keysize in range(2, min(max_keysize, self.min_length)):
                # Calculate normalized Hamming distances between messages
                message_distances = []
                for i in range(len(self.messages)):
                    for j in range(i + 1, len(self.messages)):
                        # XOR messages and count differing bits
                        xored = bytes(a ^ b for a, b in zip(self.messages[i], self.messages[j]))
                        distance = sum(bin(byte).count('1') for byte in xored)
                        normalized_distance = distance / (keysize * 8)
                        message_distances.append(normalized_distance)
                
                # Average the distances
                avg_distance = sum(message_distances) / len(message_distances)
                distances.append((keysize, avg_distance))
            
            # Sort by lowest normalized Hamming distance
            return min(distances, key=lambda x: x[1])[0]

        def break_single_char_xor(self, bytes_list):
            """
            Break single-character XOR encryption across multiple messages
            
            Args:
                bytes_list (list): List of bytes to analyze
            
            Returns:
                tuple: (best key, best score, best text)
            """
            # English letter frequency (in percentage)
            ENGLISH_FREQ = {
                'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 13.0, 
                'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.15, 
                'k': 0.77, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 
                'p': 1.9, 'q': 0.095, 'r': 6.0, 's': 6.3, 't': 9.1, 
                'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.15, 'y': 2.0, 
                'z': 0.074, ' ': 13
            }
            
            best_score = float('-inf')
            best_key = None
            best_texts = None
            
            for key in range(256):
                # XOR each message with the current key
                decrypted_texts = []
                valid_decryption = True
                
                for message in bytes_list:
                    plaintext = bytes(b ^ key for b in message)
                    
                    try:
                        # Try to decode as ASCII
                        text = plaintext.decode('ascii').lower()
                        decrypted_texts.append(text)
                    except UnicodeDecodeError:
                        valid_decryption = False
                        break
                
                # If all messages decrypt successfully
                if valid_decryption:
                    # Score based on letter frequencies
                    score = sum(
                        sum(ENGLISH_FREQ.get(char, 0) for char in text) 
                        for text in decrypted_texts
                    )
                    
                    # Update best if this is the highest score
                    if score > best_score:
                        best_score = score
                        best_key = key
                        best_texts = decrypted_texts
            
            return best_key, best_score, best_texts

        def crack_repeating_key_xor(self):
            """
            Crack repeating key XOR encryption across multiple messages
            
            Returns:
                tuple: (decrypted key, decrypted plaintexts)
            """
            # Guess key length
            key_length = self.guess_key_length()
            print(f"Estimated key length: {key_length}")
            
            # Prepare key candidates
            key_candidates = []
            
            # Break each position in the key
            for i in range(key_length):
                # Collect bytes from this position across all messages
                position_bytes = [msg[i::key_length] for msg in self.messages]
                
                # Find the most likely single-char key for this position
                key_byte, _, _ = self.break_single_char_xor(position_bytes)
                key_candidates.append(key_byte)
            
            # Reconstruct the full key
            key = bytes(key_candidates)
            
            # Decrypt all messages
            plaintexts = []
            for message in self.messages:
                plaintext = bytes(c ^ key[i % len(key)] for i, c in enumerate(message))
                plaintexts.append(plaintext)
            
            self.key = key
            self.plaintexts = plaintexts
            
            return key, plaintexts

        def print_results(self):
            """
            Print decryption results
            """
            if self.key is None or self.plaintexts is None:
                print("No decryption results available. Run crack_repeating_key_xor() first.")
                return
            
            print("\n--- Decryption Results ---")
            print(f"Key (hex): {self.key.hex()}")
            print("\nDecrypted Messages:")
            for i, plaintext in enumerate(self.plaintexts, 1):
                try:
                    decoded = plaintext.decode('ascii', errors='ignore')
                    print(f"Message {i}: {decoded}")
                except Exception as e:
                    print(f"Message {i}: Decoding error - {e}")

def main():
        # The 17 hex-encoded messages
        hex_messages = [
            "0d465f575e4413415c5c49550145445b175a1915105e525e0358424d",
            "13035b5e1e1456475c41405b0b014a120d575c01111151120e5a53014d16",
            "0d08175f4b1451444a5a575c1716134b0c47191510544053145011055b4a44150a0142115f5d4a1500054453011f",
            "050853124b5b46455113504a440b5c1204475817035f445703155e0514510a0f0d12031058575c4b",
            "0d00174b5d411352585d1e4d44114147104619044242475b1546110155560f0410484213595946421646445e0011470e115f0544540d540011455f09",
            "0c0f4557125956115641195f0d1756120e5717450b45174146505f175d4a010d1b441714114c5d451c094518",
            "080343154114505e4c5d4d19100a13460b405c004c11495d131552025a18000e42100a05451412060408174245485f145c524103420c19045f551057461351535a0e1d41584d4643170a5d47430741000745584a11505d4b5a4b470c024a1d450a4b165f425b",
            "0c0f44465d464a115040571e1045585b0d5619110d115d570815460b5b18140d031d42035e5c1c",
            "13035b5e125e46424d135e56011613460c124a0d0d461c12085a110c5a5d4312420d0c00544b46171005445f075d554f",
            "0d415b5e12505c11585d404d0c0c5d5543545617425010450958500d144f0d150a4403445a565b030048",
            "100e52405713401158134a581d0c5d55435b5745075f575e075b5559144f0c0410014210595d400042151045085e5b044f13150c52105c424211565f14041e405641520d5d1909514101125c161019120152465645401b19445d130b164a45450751525811101355524713110b15415b404547134d03404f",
            "100e5646125852424d1351580a01135c06534b091b115b5b0a5954071455014f",
            "1709174b5d411346585d4d19090013460c125b004259515e00155c0c5a5348410a050e0211505b1108075e18",
            "13035b5e1e145a11555a525c44115c12075d19160d5c5512125d580d534b44150a01420b5d5c1f030415585f0a5f55054344001d19",
            "0d46435a5d4154594d135a51160c40460e534a450d5f5c4b46565e0e514b440e0c07074450184b0004141e",
            "100e56461547135b4c404d19051613500256190411115c5b1541540d5d560341160b4210595d12070007445a004210160a47090b4216190050435d4300074319",
            "05465a5340405a5f501d194a0c0458570d1e190b0d451041125c4311515c4a"

        ]
        
        # Create XOR cracker instance
        cracker = MultiMessageXORCracker(hex_messages)
        
        try:
            # Attempt to crack the encryption
            cracker.crack_repeating_key_xor()
            
            # Print results
            cracker.print_results()
        
        except Exception as e:
            print(f"Decryption failed: {e}")

if __name__ == '__main__':
        main()