















# List < string > list = Console.ReadLine().Split().ToList();
#
# string
# input = string.Empty;
# int
# counter = 0;
# bool
# end = false;
# while ((input=Console.ReadLine()) != "end")
# {
#     string[]
# command = input.Split();
# string
# firstIndex = command[0];
# string
# secondIndex = command[1];
# int
# startIndex = int.Parse(firstIndex);
# int
# endIndex = int.Parse(secondIndex);
# if (list.Count == 0 | | list.Count == 1)
# {
#     end = true;
# Console.WriteLine($"You have won in {counter} turns!");
# break;
# }
# if (startIndex < 0 | | startIndex >= list.Count)
# {
# Console.WriteLine("Invalid input! Adding additional elements to the board");
# counter + +;
# string
# added = "-" + counter + "a";
# list.Insert(list.Count / 2, added);
# list.Insert(list.Count / 2, added);
#
# }
# else if (endIndex < 0 | | endIndex >= list.Count)
# {
# Console.WriteLine("Invalid input! Adding additional elements to the board");
# counter + +;
# string
# added = "-" + counter + "a";
# list.Insert(list.Count / 2, added);
# list.Insert(list.Count / 2, added);
#
# }
# else if (startIndex == endIndex)
# {
# Console.WriteLine("Invalid input! Adding additional elements to the board");
# counter + +;
# string
# added = "-" + counter + "a";
# list.Insert(list.Count / 2, added);
# list.Insert(list.Count / 2, added);
# }
# else
# {
#
# counter + +;
# if (list[startIndex] == list[endIndex])
#     {
#         Console.WriteLine($"Congrats! You have found matching elements - {list[startIndex]}!");
#     if (firstIndex == "0")
#     {
#     list.Remove(list[startIndex]);
#     list.Remove(list[endIndex-1]);
#     }
#     else
#     {
#     list.Remove(list[startIndex]);
#     list.Remove(list[endIndex]);
#     }
#
#     }
#     else Console.WriteLine("Try again!");
# }
# }
# if (end == false)
# {
# Console.WriteLine($"Sorry you lose :(");
# Console.WriteLine(String.Join(" ", list));

