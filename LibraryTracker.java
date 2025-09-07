public class LibraryTracker {
    public static void main(String[] args) {
        
        String book1 = "The Great Gatsby";
        boolean book1Free = true;

        String book2 = "To Kill a Mockingbird";
        boolean book2Free = true;

        String book3 = "1984";
        boolean book3Free = true;

 Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. View Books");
            System.out.println("2. Borrow Book");
            System.out.println("3. Return Book");
            System.out.println("4. Exit");
            System.out.print("Choose (1-4): ");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
if (book1Free) {
    System.out.println("1. " + book1 + " Free");
} else {
    System.out.println("1. " + book1 + "  Taken");
}

if (book2Free) {
    System.out.println("2. " + book2 + "  Free");
} else {
    System.out.println("2. " + book2 + "  Taken");
}

if (book3Free) {
    System.out.println("3. " + book2+ " Taken");
}

   break;


		case 2:

System.out.print("Book number (1-3): ");
int borrowBook= scanner.nextInt();
	
	switch (borrowBook) {
   if (book1Free) {

book1Free = false;

System.out.println("Borrowed " + book1);

  }
  break;
                       
if (book2Free) {

book2Free = false;

System.out.println("Borrowed " + book2);
 
}
   break;

                      
if (book3Free) {

 book3Free = false;

System.out.println("Borrowed " + book3);
} else {
System.out.println(book3 + " is taken.");
}
break;
default:

}
}
}






                       