using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

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

            string[] ownedcar = new string [3];

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
                        Console.WriteLine("Money: " + money);
                        sale++;
                        Console.WriteLine("Owned cars: " + sale);
                    }
                    else if (menu2 == "2")
                    {
                        money -= car2;
                        Console.WriteLine("Money: " + money);
                        sale++;
                        Console.WriteLine("Owned cars: " + sale);
                    }
                    else if (menu2 == "3")
                    {
                        money -= car3;
                        Console.WriteLine("Money: " + money);
                        sale++;
                        Console.WriteLine("Owned cars: " + sale);
                    }
                    else
                    {
                        Console.WriteLine("Du skrev fel på keyboard");
                    }
                }
                else if (menu == "2")
                {
                    Console.Write(" Do you want to sell? Volvo v100 (1), volvo v200, (3) volvo v300: ");
                    string menu3 = Console.ReadLine();
                    if (menu3 == "1" && sale > 0)
                    {
                        money += car1;
                        Console.WriteLine("Money: " + money);
                        sale--;
                        Console.WriteLine("Owned cars: " + sale);
                    }
                    else if (menu3 == "2" && sale > 0)
                    {
                        money += car1;
                        Console.WriteLine("Money: " + money);
                        sale--;
                        Console.WriteLine("Owned cars: " + sale);
                    }
                    else if (menu3 == "3" && sale > 0)
                    {
                        money += car1;
                        Console.WriteLine("Money: " + money);
                        sale--;
                        Console.WriteLine("Owned cars: " + sale);
                    }
                    else
                    {
                        Console.WriteLine("wrong keyboard input or you don't own a car");
                    }
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
            if (sale == 1)
            {
                Console.WriteLine("Volvo v100, model 2005");
            }
            else if (sale == 2) 
            {
                Console.WriteLine("Volvo v100, model 2005");
                Console.WriteLine("Volvo v200, model 2010");
            }
            else if (sale == 3)
            {
                Console.WriteLine("Volvo v100, model 2005");
                Console.WriteLine("Volvo v200, model 2010");
                Console.WriteLine("Volvo v300, model 2022");
               
            }
            else if (sale == 4)
            {
                Console.WriteLine("Volvo v100, model 2005");
                Console.WriteLine("Volvo v100, model 2005");
                Console.WriteLine("Volvo v200, model 2010");
                Console.WriteLine("Volvo v300, model 2022");

            }
            else if (sale == 5)
            {
                Console.WriteLine("Volvo v100, model 2005");
                Console.WriteLine("Volvo v100, model 2005");
                Console.WriteLine("Volvo v200, model 2010");
                Console.WriteLine("Volvo v200, model 2010");
                Console.WriteLine("Volvo v300, model 2022");

            }
            Console.WriteLine("du har slut på pengar eller avslutade handel");
            Console.WriteLine(ownedcar);

            Console.ReadLine();
        }
    }
}