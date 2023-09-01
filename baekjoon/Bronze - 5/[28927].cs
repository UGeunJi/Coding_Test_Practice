namespace Solution {
  class Program {
    static void Main(string[] args) {

      var maxTimes = Console.ReadLine()!.Split(' ').Select(int.Parse).ToArray();
      var melTimes = Console.ReadLine()!.Split(' ').Select(int.Parse).ToArray();

      int maxTime = 3 * maxTimes[0] + 20 * maxTimes[1] + 120 * maxTimes[2];
      int melTime = 3 * melTimes[0] + 20 * melTimes[1] + 120 * melTimes[2];

      if (maxTime > melTime) Console.WriteLine("Max");
      else if (maxTime < melTime) Console.WriteLine("Mel");
      else Console.WriteLine("Draw");

    }
  }
}
