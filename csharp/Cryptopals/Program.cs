using System.Diagnostics;

namespace Cryptopals
{
    class MainClass
    {
        static void Main()
        {
            Set1.C1();

            var s1c2 = Set1.C2("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965");
            Debug.Assert(s1c2.ToLower() == "746865206b696420646f6e277420706c6179");

            Set1.C3();
        }
    }
}


