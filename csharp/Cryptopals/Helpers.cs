namespace Cryptopals
{
    class Helpers
    {
        public static byte[] HexDecode(string s)
        {
            return Convert.FromHexString(s);
        }

        public static byte[] BytewiseXOR(byte[] b1, byte[] b2, bool repeatChar = false)
        {
            var result = new byte[b1.Length];
            for (int i = 0; i < result.Length; ++i)
            {
                var mask = repeatChar ? b2[0] : b2[i];
                result[i] = (byte)(b1[i] ^ mask);
            }

            return result;
        }
    }
}