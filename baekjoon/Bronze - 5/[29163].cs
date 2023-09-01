namespace Solution {
  class Program {
    static void Main(string[] args) {

      var n = int.Parse(Console.ReadLine()!);

      var numbers = Console.ReadLine()!.Split(' ').Select(int.Parse).ToArray();

      int eventCount = 0;
      for (int i = 0; i < n; i++) {
        if (numbers[i] % 2 == 0)
          eventCount++;
      }

      if (eventCount > n / 2) Console.WriteLine("Happy");
      else Console.WriteLine("Sad");

    }
  }
}
