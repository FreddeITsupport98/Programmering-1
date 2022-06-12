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
            int drive; // starting do parse program into int value
            Console.Write(" What is your car brand: "); // qestion mark
            string car_make = Console.ReadLine(); // car_make store value
            Console.Write(" What year modell is your car?:  "); // question mark
            string model = Console.ReadLine(); // store value in model
            Console.Write("What year model does your car have?: "); // same statement"
            string year_model = Console.ReadLine(); // same statement"
            Console.Write("how far do you drove om Km ?: "); // same statement"
            string drive_distance = Console.ReadLine(); // same statement"
            drive = int.Parse(drive_distance); // same statement for intenger perse"

            // Concategnet value bt string and varibels
            Console.WriteLine(" Well you have a " + car_make + " of " + model + " and already from " + year_model + " but it has not gone more than " + drive_distance + " it sounds intresting! ");

            int money = 1250; // money
            int sale = 0; // Sale
            int car1 = 250; // car value
            int car2 = 300; // car value
            int car3 = 400; // car value
            bool exit = false; // If menu true while loop breaks
            string car_Name1 = "volvo v100, model 2005";
            string car_Name2 = "volvo v200, model 2010";
            string car_Name3 = "volvo v300, model 2022";

            string[] cars = new string[10]; // car indexes stored for later pruchase

            cars[0] = "";
            cars[1] = "";
            cars[2] = ""; // index value stored empty string


            while (money > car1 && money > car2 && money > car3 && exit != true) // if loops it breaks "car value - money"
            {
                Console.Write("Choose menu 1: to buy, 2 sale, 3 exit: "); // menu 1.2.3
                string menu = Console.ReadLine();
                if (menu == "1")
                {
                    Console.Write(" Do you want to buy? Volvo v100 (1), volvo v200, (3) volvo v300: ");
                    string menu2 = Console.ReadLine();
                    if (menu2 == "1")
                    {
                        money -= car1; // money - car1
                        Console.WriteLine("Money: " + money); // print money value
                        sale++; // adds sale value by incrementing number upp!
                        Console.WriteLine("Owned cars: " + sale); // print sale value
                        cars.Append(cars[0] = "volvo v100, model 2005"); // appends to index 0, only once it can append
                    }
                    else if (menu2 == "2")
                    {
                        money -= car2; //same statment!
                        Console.WriteLine("Money: " + money); //same statment!
                        sale++; //same statment!
                        Console.WriteLine("Owned cars: " + sale); //same statment!
                        cars.Append(cars[1] = "volvo v200, model 2010");//same statment!
                    }
                    else if (menu2 == "3")
                    {
                        money -= car3; //same statment!
                        Console.WriteLine("Money: " + money);//same statment!
                        sale++; //same statment!
                        Console.WriteLine("Owned cars: " + sale); //same statment!
                        cars.Append(cars[2] = "volvo v300, model 2022"); //same statment!
                    }
                    else
                    {
                        Console.WriteLine("Du skrev fel på keyboard");
                    }
                }
                else if (menu == "2")
                {
                    Console.Write(" Do you want to sell? Volvo v100 (1), volvo v200, (3) volvo v300: "); //menu 2
                    string menu3 = Console.ReadLine();
                    Console.WriteLine(cars[0] + " Owned cars! "); //print out index
                    Console.WriteLine(cars[1] + " Owned cars! ");
                    Console.WriteLine(cars[2] + " Owned cars! ");
                    if (menu3 == "1" && sale > 0)
                    {
                        money += car1;
                        Console.WriteLine("Money: " + money);
                        sale--;
                        Console.WriteLine("Owned cars: " + sale);
                        cars.Append(cars[0] = ""); // appends index change to string of nothing
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