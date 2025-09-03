import java.util.Scanner;

public class VotingSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of candidates: ");
        int candidatesNumber = scanner.nextInt();
        scanner.nextLine(); 
        
String[] candidates = new String[candidatesNumber];
        int[] votes = new int[candidatesNumber];

        for (int index = 0; index < candidatesNumber; index++) {
            System.out.print("Enter candidate " + (index + 1) + " name: ");
            candidates[index] = scanner.nextLine();
}

        System.out.print("Enter number of voters: ");
        int votersNumber = scanner.nextInt();
}
}