﻿using System;
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
            vending_search();
        }
        static void vending_search()
        {
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
        }

        static void vending_batch()
        {

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
                    Console.WriteLine("There is no other button aviable");
                }
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
                    file.WriteLine("marabo");
                    Console.Write("Your name: ");
                    string name = Console.ReadLine();
                    file.WriteLine(name);
                    file.Flush();
                    file.Close();
                }
            }

            Console.ReadLine();
        }
        static void vending()
        {
         
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
            
             
            
            string[] slot1 = { "Marabio", "Cocola", "Nudlar"};
            string[] slot2 = { "Kinderkex", "cocola-light", "Loka"};
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
                Console.WriteLine("There is no other button aviable");
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
                    file.WriteLine("marabo");
                    Console.Write("Your name: ");
                    string name = Console.ReadLine();
                    file.WriteLine(name);
                    file.Flush();
                    file.Close();
                }
            }

           Console.ReadLine();
        }
    }
}