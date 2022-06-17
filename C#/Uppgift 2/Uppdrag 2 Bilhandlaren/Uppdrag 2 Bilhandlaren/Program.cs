using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

namespace bilhandlaren
{
    class uppgift2
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello and welcome!"); // welcome
            int pinAccess = 0; // set as tries
            int menu = 0; // obsolet
            Console.Write("Whats your name?: ");
            string name = Console.ReadLine();
            Console.WriteLine(" Welcome " + name);
            while (pinAccess < 3) // set while loop to break if pinaAccess set to 3
            {
                int pin = 1234; // secret pin
                Console.Write("Please login with your pin: ");
                int userPin = Convert.ToInt32(Console.ReadLine());  
                if (userPin != pin) 
                {
                    Console.WriteLine("Wrong input");
                    pinAccess++;
                    Console.WriteLine("Number of tries: " + pinAccess);
                }
                else if (pin == userPin)
                {
                    Console.WriteLine("Welcome customer!");
                    pinAccess = 3;
                }
                while (menu < 4) // menu 1 buy, menu 2 sell, menu 3 break loop
                {
                    Console.Clear();
                    Console.WriteLine("Welcome to car-dealership " + name + "!");
                    Console.WriteLine("Menu 1: buy car, Menu 2: sell cars, menu 3:exit: ");
                    int answer = Convert.ToInt32(Console.ReadLine());

                    if (answer == 1)
                    {
                        Console.WriteLine("What do you want to buy");
                        Console.Write("Car1 (1), car2 (2), car3 (3), car4 (4): ");
                        int answer2 = Convert.ToInt32(Console.ReadLine());
                        if (answer2 == 1)
                        {
                            Console.WriteLine("Car1");
                            Console.ReadLine();
                        }
                        else if (answer2 == 2)
                        {
                            Console.WriteLine("Car2");
                            Console.ReadLine();
                        }
                        else if (answer2 == 3)
                        {
                            Console.WriteLine("Car3");
                            Console.ReadLine();
                        }
                        else if (answer2 == 4)
                        {
                            Console.WriteLine("Car4");
                            Console.ReadLine();
                        }
                    }
                    else if (answer == 2)
                    {
                        Console.WriteLine("What do you want to sell?");
                        Console.Write("Car1 (1), car2 (2), car3 (3), car4 (4): ");
                        int answer3 = Convert.ToInt32(Console.ReadLine());

                        if (answer3 == 1)
                        {
                            Console.WriteLine("Car1");
                            Console.ReadLine();
                        }
                        else if (answer3 == 2)
                        {
                            Console.WriteLine("Car2");
                            Console.ReadLine();
                        }
                        else if (answer3 == 3)
                        {
                            Console.WriteLine("Car3");
                            Console.ReadLine();
                        }
                        else if (answer3 == 4)
                        {
                            Console.WriteLine("Car4");
                            Console.ReadLine();
                        }
                    }
                    else if (answer == 3)
                    {
                      Console.WriteLine("exiting");
                      Console.ReadLine();
                      break;
                    }
                    

                }
            }

        }
    }
}
