using System.Text;

namespace Cryptopals
{
    class Set1
    {
        /*
            Convert hex to base64
            The string:

            49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
            Should produce:

            SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
            So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
        */
        public static void C1()
        {
            var hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";

            var raw = Helpers.HexDecode(hexString);
            var base64String = Convert.ToBase64String(raw);

            Console.WriteLine(base64String);
        }

        /*
            Fixed XOR
            Write a function that takes two equal-length buffers and produces their XOR combination.

            If your function works properly, then when you feed it the string:

            1c0111001f010100061a024b53535009181c
            ... after hex decoding, and when XOR'd against:

            686974207468652062756c6c277320657965
            ... should produce:

            746865206b696420646f6e277420706c6179
        */
        public static string C2(string s1, string s2)
        {
            var b1 = Helpers.HexDecode(s1);
            var b2 = Helpers.HexDecode(s2);

            return Convert.ToHexString(Helpers.BytewiseXOR(b1, b2));
        }

        /*
            Single-byte XOR cipher
            The hex encoded string:

            1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
            ... has been XOR'd against a single character. Find the key, decrypt the message.

            You can do this by hand. But don't: write code to do it for you.

            How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

            Achievement Unlocked
            You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
        */
        public static void C3()
        {
            // var cipher = "ETAOIN SHRDLU";
            // var cipherBytes = Encoding.UTF8.GetBytes(cipher);
            var cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
            var cipherBytes = Helpers.HexDecode(cipher);

            int score(char c)
            {
                var xor = Helpers.BytewiseXOR(cipherBytes, [(byte)c], true);

                int score = 0;
                foreach (char cc in xor)
                {
                    bool highFreq = "ETAOIN SHRDLU".Contains(cc.ToString().ToUpper());
                    score = highFreq ? score+1 : score;
                }

                return score;
            }

            var map = new Dictionary<char, int>();
            for (char i = (char)0; i < 256; ++i)
            {
                map[i] = score(i);
            }

            var kvps = map.OrderByDescending(x => x.Value).Take(5);
            foreach (var kvp in kvps)
            {
                var resultBytes = Helpers.BytewiseXOR(cipherBytes, [(byte)kvp.Key], true);
                var result = Encoding.UTF8.GetString(resultBytes);
                Console.WriteLine("[+] Cipher key: " + (int)kvp.Key + ", score: " + kvp.Value + ", decrypted: " + result);
            }
        }
    }
}