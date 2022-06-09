using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace bilspekulanten
{
    class program
    {
        static void Main(string[] args)
        {
            //int drive;
            //Console.Write(" What is your car brand: ");
            //string car_make = Console.ReadLine();
            //Console.Write(" What year modell is your car?:  ");
            //string model = Console.ReadLine();
            //Console.Write("What year model does your car have?: ");
            //string year_model = Console.ReadLine();
            //Console.Write("how far do you drove om Km ?: ");
            //string drive_distance = Console.ReadLine();
            //drive = int.Parse(drive_distance);

            //Console.WriteLine(" Well you have a " + car_make + " of " + model + " and already from " + year_model + " but it has not gone more than " + drive_distance + " it sounds intresting! ");

            int money = 1500;
            int sale = 0;
            int car1 = 250;
            int car2 = 300;
            int car3 = 400;
            bool exit = false;
            string car_Name1 = "volvo v100, model 2005";
            string car_Name2 = "volvo v200, model 2010";
            string car_Name3 = "volvo v300, model 2022";

            string[] ownedcar = {""};

            while (money > car1 && money > car2 && money > car3 && exit != true)
            {
                Console.Write("Choose menu 1: to buy, 2 sale, 3 exit: ");
                string menu = Console.ReadLine();
                if (menu == "1")
                {
                    Console.Write(" Do you want to buy? Volvo v100 (1), volvo v200, (3) volvo v300: ");
                    string menu2 = Console.ReadLine();
                    if (menu2 == "1")
                    {
                        money -= car1;
                        Console.WriteLine(money);
                        sale++;
                        Console.WriteLine(sale);
                    }
                    else if (menu2 == "2")
                    {
                        Console.WriteLine("2");
                    }
                    else if (menu2 == "3")
                    {
                        Console.WriteLine("3");
                    }
                    else
                    {
                        Console.WriteLine("Du skrev fel på keyboard");
                    }

                    
                }
                else if (menu == "2")
                {
                    Console.WriteLine("menu 2");
                }
                else if (menu == "3")
                {
                    Console.WriteLine("menu 3");
                    exit = true;
                }
                else
                {
                    Console.WriteLine("Du skrev fel");
                }
            }
            Console.WriteLine("du har slut på pengar eller avslutade handel");

            Console.ReadLine();
        }
    }
}