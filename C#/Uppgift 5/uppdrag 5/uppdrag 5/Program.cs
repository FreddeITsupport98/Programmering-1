using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;
using System.IO;

namespace vendingmachine
{
    class uppgift5
    {
        static void Main(string[] args)
        {
            /* 
            
            Denna kod är ofullständig som är demonstation vad riktiga koden kan göra i pyton. eftersom jag har vallt att skriva om koden i enkare sätt 
            Är i syftet fär att demonstrera mina IT-Kunskapen för att nå till betyg. den har alla delar som grundläggande programering behövs.

             */

            Console.WriteLine("This is a demo all funktion are limited for demostration of code to teacher judge. \n Please refer fully code in Python!");
            
            
            while (true)
            {
                Console.WriteLine("\n");
                Console.Write(" Kvitto: 1, \n kalkylator file: 2, \n rate: 3, \n kalkylator 4, \n vending search: 5 \n vending: 6 \n vending batch: 7 \n exit: 8 \n Input:  ");
                int menu = Convert.ToInt32(Console.ReadLine()); // menu
                Console.WriteLine("\n");
                if (menu == 1)
                {
                    Console.WriteLine("Enter kvitto ");
                    kvitto();
                }
                else if (menu == 2)
                {
                    Console.WriteLine("Enter kalkylator file ");
                    kalkylator_file();
                }
                else if (menu == 3)
                {
                    Console.WriteLine("Enter rate ");
                    rate();
                }
                else if (menu == 4)
                {
                    Console.WriteLine("Enter kalkylator ");
                    kalkylator();
                }
                else if (menu == 5)
                {
                    Console.WriteLine("Enter vending search ");
                    vending_search();

                }
                else if (menu == 6)
                {
                    Console.WriteLine("Enter vending ");
                    vending();
                }
                else if (menu == 7)
                {
                    Console.WriteLine("Enter vending batch ");
                    vending_batch();
                }
                else if (menu == 8)
                {
                    break;
                }
            }
            
        }

        static void kvitto()
        {
            Console.Write("Load file: load: ");
            string load = Console.ReadLine();
            if (load == "load")
            {
                try
                {
                    string path = "Kvitto.txt";// laddar filen lokalt i bin som visual studio kode sparar
                    List<string> lines = File.ReadAllLines(path).ToList();
                    // skriver lista på lath som lista ungefär som print statment i pyton
                    foreach (string line in lines)
                    {
                        Console.WriteLine(line);
                    }
                }
                catch // fångar error kod om filen inte existerar
                {
                    Console.WriteLine("Error file does not exisist");
                }

            }
        }

        static void kalkylator_file() // samma liknade struktur!
        {
            Console.Write("Load file: load: ");
            string load = Console.ReadLine();
            if (load == "load")
            {
                try
                {
                    string path = "kalkylator.txt";
                    List<string> lines = File.ReadAllLines(path).ToList();
                    foreach (string line in lines)
                    {
                        Console.WriteLine(line);
                    }
                }
                catch
                {
                    Console.WriteLine("Error file does not exisist");
                }

            }
        }

        static void rate() // samma liknade struktur!
        {
            while (true)
            {
                Console.Write("Load file: load or append or exit: ");
                string load = Console.ReadLine();
                if (load == "load")
                {
                    try
                    {
                        string path = "rate.txt";
                        List<string> lines = File.ReadAllLines(path).ToList();
                        foreach (string line in lines)
                        {
                            Console.WriteLine(line);
                        }
                    }
                    catch
                    {
                        Console.WriteLine("Error file does not exisist");
                    }

                }
                else if (load == "append") // samma liknade struktur dock kan skriva variabel till filen som angivits
                {
                    StreamWriter file = new StreamWriter("rate.txt");
                    Console.Write("Your name: ");

                    string name = Console.ReadLine();
                    Console.Write("how manu stars do you want to rate it?: ");
                    string rate = Console.ReadLine();
                    Console.Write("Rate our service: ");
                    string service = Console.ReadLine();
                    Console.Write("Comments: ");
                    string comments = Console.ReadLine();
                    file.WriteLine(name);
                    file.WriteLine("*");
                    file.WriteLine("*");
                    file.WriteLine("**************");
                    file.WriteLine("Rate in stars: " + rate + "\n" + "Name and surname: " + name + "\n" + service + "\n" + "comments: " + comments + "\n");
                    file.WriteLine("**************");
                    file.Flush(); // Denna kod tömmer buffer minnet i filen
                    file.Close(); // stänger filen!
                    Console.WriteLine("File written");
                }
                else if (load == "exit")
                {
                    break;
                }
            }
        }
        static void kalkylator()
        {
            while (true)
            {
                Console.Write("Want use vending search mode?: Yes or No: ");
                string enter = Console.ReadLine();
                if (enter == "yes")
                {
                    vending_search();
                }
                else if (enter == "no")
                {
                    Console.WriteLine("good luck");
                }

                Console.Write("How many do you want to buy (Rekomended use vending search mode) ?: 1,2,3,4,5, 6: exit program: ");
                int menu = Convert.ToInt32(Console.ReadLine());
                if (menu == 1)
                {
                    Console.WriteLine("Single mode"); // samma liknade struktur på python!
                    Console.Write("Enter item name: ");
                    string item1 = Console.ReadLine();
                    Console.Write("Enter amount kcal: ");
                    int kcal1 = Convert.ToInt32(Console.ReadLine());
                    int kcal1_rec = 250;
                    if (kcal1 > kcal1_rec) // samma liknade struktur om kcal1 överstiger rekommenderad angivilse
                    {
                        Console.WriteLine(item1);
                        Console.WriteLine(" Recomended intake " + kcal1_rec + " kcal " + " your is: " + kcal1 + "\n");
                        StreamWriter file = new StreamWriter("kalkylator.txt");
                        file.WriteLine("Items: " + item1 + "," + "\n" + "Rekommended kcal intake: " + kcal1_rec + "," + "\n" + "Your kcal intake: " + kcal1);
                        file.Flush();
                        file.Close();
                        Console.WriteLine("File written");
                    }
                    else if (kcal1 < kcal1_rec) // samma liknade struktur om kcal understiger angivelse!
                    {
                        Console.WriteLine(item1);
                        Console.WriteLine("You are in recomended intake " + kcal1_rec + " kcal " + " your is: " + kcal1 + "\n");
                        StreamWriter file = new StreamWriter("kalkylator.txt");
                        file.WriteLine("Items: " + item1 + "," + "\n" + "Rekommended kcal intake: " + kcal1_rec + "," + "\n" + "Your kcal intake: " + kcal1);
                        file.Flush();
                        file.Close();
                        Console.WriteLine("File written");
                    }
                }
                else if (menu == 6)
                {
                    Console.WriteLine("Exiting");
                    break;
                }

                else
                {
                    Console.WriteLine("This is a demo not fully featured program!");
                }
            }

        }
        static void vending_search()
        {
            /*
             Denna använder swtich case som i C# erbjuder på pyton måste vara siffror för att användaren ska navigera
            men denna behövs inte det gör skriva olika siffror som får inga svar av programmen!
             */
            while (true)
            {
                Console.WriteLine("\n");
                string[] slot1 = { "Marabio", "Cocola", "Nudlar" };
                string[] slot2 = { "Kinderkex", "cocola-light", "Loka" };
                string[] slot3 = { "Grill-chips", "viniger-chips", "cocola-chips" };
                string[] slot4 = { "rizz", "fronzies", "nutella-cokies" };
                string[] slot5 = { "twix", "water", "snacks" };

                Console.WriteLine(slot1[0] + "             " + slot1[1] + "                   " + slot1[2]);
                Console.WriteLine("E1 15.5 kr" + "         " + "E2 20 kr" + "                  " + "E3 30 kr");
                Console.WriteLine(slot2[0] + "               " + slot2[1] + "         " + slot2[2]);
                Console.WriteLine("E4 12.12 kr" + "              " + "E5 15kr" + "            " + "E6 25 kr");
                Console.WriteLine(slot3[0] + "        " + slot3[1] + "       " + slot3[2]);
                Console.WriteLine("E7 14 kr" + "              " + "E8 25 kr" + "            " + "E9 15 kr");
                Console.WriteLine(slot4[0] + "                  " + slot4[1] + "                " + slot4[2]);
                Console.WriteLine("E10 10 kr" + "              " + "E11 12 kr" + "            " + "E12 45 kr");
                Console.WriteLine(slot5[0] + "                    " + slot5[1] + "               " + slot5[2]);
                Console.WriteLine("E13 17 kr" + "              " + "E14 10 kr" + "            " + "E15 14 kr");

                Console.Write("\n E1, E2, E3,\n E4, E5, E6\n E7, E8, E9 \n E10, E11 E12 \n E13, E14, E15 \n Input machine: ");
                string input = Console.ReadLine();
                switch (input)
                {
                    case "E1":
                        Console.WriteLine("\n");
                        Console.WriteLine("E1");
                        Console.WriteLine("Marabo");
                        Console.WriteLine("15.5 kr");
                        Console.WriteLine("500 kcal");
                        Console.WriteLine("200 g");
                        Console.WriteLine("lactose");
                        Console.WriteLine("\n");
                        break;
                    case "E2":
                        Console.WriteLine("\n");
                        Console.WriteLine("E2");
                        Console.WriteLine("cocola");
                        Console.WriteLine("20 kr");
                        Console.WriteLine("1000 kcal");
                        Console.WriteLine("450 g");
                        Console.WriteLine("Sugar and chemicals");
                        Console.WriteLine("\n");
                        break;

                }
                Console.Write("Want to exit?: Exit or press enter to continue: ");
                string exit = Console.ReadLine();
                if (exit == "exit")
                {
                    Console.WriteLine("exiting...");
                    break;
                }
            }

        }

        static void vending_batch()
        {
            /*
             Denna är vending batch och har endast 1 knapp att använda dock listor som kallas array har sämre hantering och därför inkludera jag inte array
            i programmen. använder print liknade sats och värde på pengar stiger ner endast en gång. Den har while loop som i pyton.
            dock kvitto lät jag hålla simpelt och behöver inte kvitto 1 eller 2. 
             */
            float money; // måste vara utanför scope av while loop efter den värden sparas inte inom while loop.

            while (true) // insättning
            {
                Console.Write("How much do yo want to input money? ");
                string text = Console.ReadLine();
                money = float.Parse(text);
                if (money > 100)
                {
                    Console.WriteLine("This machine accepts only 100 kr");



                }
                else if (money <= 100)
                {
                    Console.WriteLine("This machine accepts money");
                    break;

                }
            }


            // menu
            string[] slot1 = { "Marabio", "Cocola", "Nudlar" };
            string[] slot2 = { "Kinderkex", "cocola-light", "Loka" };
            string[] slot3 = { "Grill-chips", "viniger-chips", "cocola-chips" };
            string[] slot4 = { "rizz", "fronzies", "nutella-cokies" };
            string[] slot5 = { "twix", "water", "snacks" };

            Console.WriteLine(slot1[0] + "             " + slot1[1] + "                   " + slot1[2]);
            Console.WriteLine("E1 15.5 kr" + "         " + "E2 20 kr" + "                  " + "E3 30 kr");
            Console.WriteLine(slot2[0] + "               " + slot2[1] + "         " + slot2[2]);
            Console.WriteLine("E4 12.12 kr" + "              " + "E5 15kr" + "            " + "E6 25 kr");
            Console.WriteLine(slot3[0] + "        " + slot3[1] + "       " + slot3[2]);
            Console.WriteLine("E7 14 kr" + "              " + "E8 25 kr" + "            " + "E9 15 kr");
            Console.WriteLine(slot4[0] + "                  " + slot4[1] + "                " + slot4[2]);
            Console.WriteLine("E10 10 kr" + "              " + "E11 12 kr" + "            " + "E12 45 kr");
            Console.WriteLine(slot5[0] + "                    " + slot5[1] + "               " + slot5[2]);
            Console.WriteLine("E13 17 kr" + "              " + "E14 10 kr" + "            " + "E15 14 kr");

            // menu och knappar
            int sale = 0;
            while (true)
            {
                Console.Write("\n E1, E2, E3,\n E4, E5, E6\n E7, E8, E9 \n E10, E11 E12 \n E13, E14, E15 \n Input machine: ");
                string input = Console.ReadLine();
                Console.WriteLine("\n");

                if (input == "E1" && money > 15)
                {
                    Console.WriteLine("It cost you 15 kr!");
                    if (sale < 1)
                    {
                        money -= 15;
                        sale++;
                    }
                    else if (sale <= 2)
                    {
                        Console.WriteLine("You already own item!");
                    }
                    string item1 = "Marabo";
                    Console.WriteLine(money);
                    Console.WriteLine(slot1[0]);
                    Console.WriteLine("Selected item: Marabo");
                    Console.WriteLine("500 kcal");
                    Console.WriteLine("laktose");
                    Console.WriteLine("200 g");
                    Console.WriteLine("\n");
                    for (int i = 1; i < slot1.Length; i++) ;
                    Console.WriteLine(slot1[0] + " " + slot1[1] + " " + slot1[2]);
                    Console.WriteLine(slot2[0] + " " + slot2[1] + " " + slot2[2]);
                    Console.WriteLine(slot3[0] + " " + slot3[1] + " " + slot3[2]);
                    Console.WriteLine(slot4[0] + " " + slot4[1] + " " + slot4[2]);
                    Console.WriteLine(slot5[0] + " " + slot5[1] + " " + slot5[2]);
                }
                else if (input == "exit")
                {
                    Console.WriteLine("Exiting");
                    break;
                }
                else
                {
                    Console.WriteLine("There is no other button aviable in this demo");
                }
            }


            while (true)
            {
                Console.Write("Load file: load or append: "); // ladda eller skriv
                string load = Console.ReadLine();
                if (load == "load")
                {
                    try
                    {
                        string path = "Kvitto.txt";
                        List<string> lines = File.ReadAllLines(path).ToList();
                        foreach (string line in lines)
                        {
                            Console.WriteLine(line);
                        }
                    }
                    catch
                    {
                        Console.WriteLine("Error file does not exisist");
                    }

                }
                else if (load == "append")
                {
                    StreamWriter file = new StreamWriter("Kvitto.txt");
                    file.WriteLine(money);
                    money -= money;
                    Console.WriteLine("Here is your money back" + money);
                    file.WriteLine("marabo");
                    Console.Write("Your name: ");
                    string name = Console.ReadLine();
                    file.WriteLine(name);
                    file.Flush();
                    file.Close();
                }
            }

             
        }
        static void vending()
        {
            /*
             Denna är vending som har liknade struktur utan while loop. meningen är att användare ska köpa engång få kvitto där efter.
             */

            float money;

            while (true)
            {
                Console.Write("How much do yo want to input money? ");
                string text = Console.ReadLine();
                money = float.Parse(text);
                if (money > 100)
                {
                    Console.WriteLine("This machine accepts only 100 kr");



                }
                else if (money <= 100)
                {
                    Console.WriteLine("This machine accepts money");
                    break;

                }
            }



            string[] slot1 = { "Marabio", "Cocola", "Nudlar" };
            string[] slot2 = { "Kinderkex", "cocola-light", "Loka" };
            string[] slot3 = { "Grill-chips", "viniger-chips", "cocola-chips" };
            string[] slot4 = { "rizz", "fronzies", "nutella-cokies" };
            string[] slot5 = { "twix", "water", "snacks" };

            Console.WriteLine(slot1[0] + "             " + slot1[1] + "                   " + slot1[2]);
            Console.WriteLine("E1 15.5 kr" + "         " + "E2 20 kr" + "                  " + "E3 30 kr");
            Console.WriteLine(slot2[0] + "               " + slot2[1] + "         " + slot2[2]);
            Console.WriteLine("E4 12.12 kr" + "              " + "E5 15kr" + "            " + "E6 25 kr");
            Console.WriteLine(slot3[0] + "        " + slot3[1] + "       " + slot3[2]);
            Console.WriteLine("E7 14 kr" + "              " + "E8 25 kr" + "            " + "E9 15 kr");
            Console.WriteLine(slot4[0] + "                  " + slot4[1] + "                " + slot4[2]);
            Console.WriteLine("E10 10 kr" + "              " + "E11 12 kr" + "            " + "E12 45 kr");
            Console.WriteLine(slot5[0] + "                    " + slot5[1] + "               " + slot5[2]);
            Console.WriteLine("E13 17 kr" + "              " + "E14 10 kr" + "            " + "E15 14 kr");

            Console.Write("\n E1, E2, E3,\n E4, E5, E6\n E7, E8, E9 \n E10, E11 E12 \n E13, E14, E15 \n Input machine: ");
            string input = Console.ReadLine();
            Console.WriteLine("\n");

            if (input == "E1" && money > 15)
            {
                Console.WriteLine("It cost you 15 kr!");
                money -= 15;
                string item1 = "Marabo";
                Console.WriteLine(money);
                Console.WriteLine(slot1[0]);
                Console.WriteLine("\n");
                for (int i = 1; i < slot1.Length; i++) ;
                Console.WriteLine(slot1[0] + " " + slot1[1] + " " + slot1[2]);
                Console.WriteLine(slot2[0] + " " + slot2[1] + " " + slot2[2]);
                Console.WriteLine(slot3[0] + " " + slot3[1] + " " + slot3[2]);
                Console.WriteLine(slot4[0] + " " + slot4[1] + " " + slot4[2]);
                Console.WriteLine(slot5[0] + " " + slot5[1] + " " + slot5[2]);
            }
            else
            {
                Console.WriteLine("There is no other button aviable in this demo");
            }

            while (true)
            {
                Console.Write("Load file: load or append: ");
                string load = Console.ReadLine();
                if (load == "load")
                {
                    try
                    {
                        string path = "Kvitto.txt";
                        List<string> lines = File.ReadAllLines(path).ToList();
                        foreach (string line in lines)
                        {
                            Console.WriteLine(line);
                        }
                    }
                    catch
                    {
                        Console.WriteLine("Error file does not exisist");
                    }

                }
                else if (load == "append")
                {
                    StreamWriter file = new StreamWriter("Kvitto.txt");
                    file.WriteLine(money);
                    money -= money;
                    Console.WriteLine("Here is your money back" + money);
                    file.WriteLine("marabo");
                    Console.Write("Your name: ");
                    string name = Console.ReadLine();
                    file.WriteLine(name);
                    file.Flush();
                    file.Close();
                }
            }

         
           
        }
    }
}