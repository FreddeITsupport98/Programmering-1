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

            int money = 1250;
            int sale = 0;
            int car1 = 250;
            int car2 = 300;
            int car3 = 400;
            bool exit = false;
            string car_Name1 = "volvo v100, model 2005";
            string car_Name2 = "volvo v200, model 2010";
            string car_Name3 = "volvo v300, model 2022";

            string[] cars = new string[10];

            cars[0] = "";
            cars[1] = "";
            cars[2] = "";

            
            
            cars.Append(cars[3] = "volvo v300, model 2022");


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
                        cars.Append(cars[0] = "volvo v100, model 2005");
                    }
                    else if (menu2 == "2")
                    {
                        money -= car2;
                        Console.WriteLine("Money: " + money);
                        sale++;
                        Console.WriteLine("Owned cars: " + sale);
                        cars.Append(cars[1] = "volvo v200, model 2010");
                    }
                    else if (menu2 == "3")
                    {
                        money -= car3;
                        Console.WriteLine("Money: " + money);
                        sale++;
                        Console.WriteLine("Owned cars: " + sale);
                        cars.Append(cars[2] = "volvo v300, model 2022");
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
                    Console.WriteLine(cars[0] + " Owned cars! ");
                    Console.WriteLine(cars[1] + " Owned cars! ");
                    Console.WriteLine(cars[2] + " Owned cars! ");
                    if (menu3 == "1" && sale > 0)
                    {
                        money += car1;
                        Console.WriteLine("Money: " + money);
                        sale--;
                        Console.WriteLine("Owned cars: " + sale);
                        cars.Append(cars[0] = "");
                    }
                    else if (menu3 == "2" && sale > 0)
                    {
                        money += car1;
                        Console.WriteLine("Money: " + money);
                        sale--;
                        Console.WriteLine("Owned cars: " + sale);
                        cars.Append(cars[1] = "");
                    }
                    else if (menu3 == "3" && sale > 0)
                    {
                        money += car1;
                        Console.WriteLine("Money: " + money);
                        sale--;
                        Console.WriteLine("Owned cars: " + sale);
                        cars.Append(cars[2] = "");
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
            Console.WriteLine("du har slut på pengar eller avslutade handel");
            Console.WriteLine(cars[0] + " Owned cars! ");
            Console.WriteLine(cars[1] + " Owned cars! ");
            Console.WriteLine(cars[2] + " Owned cars! ");

            Console.ReadLine();
        }
    }
}