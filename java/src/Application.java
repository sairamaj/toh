import java.util.Scanner;

/*
 *	Class:
 *			Application
 *	Responsibilities
 *			User interaction
 *			Quit application upon user request
 *			Quits if game is over.
 *  Collaborations
 *  		Gamer
 */
public class Application {

	public static void main(String[] args) {
		printInitialMessage();
		Gamer g = new Gamer();
		g.create();

		Scanner scanner = new Scanner(System.in);
		boolean quit = false;
		do {
			System.out.print("command:");
			String command = scanner.next();
			if( command.equalsIgnoreCase("quit")) {
				quit = true;
			}else if( command.equalsIgnoreCase("move")) {
				System.out.print("from:");
				int from  = scanner.nextInt();
				System.out.print("to:");
				int to = scanner.nextInt();
				try{
					g.move(from, to);
					if(g.isGameOver()) {
						System.out.println("Congratulations, game over.");
						quit = true;
					}
				}catch(Exception e) {
					System.out.println(e.getMessage());
				}
			}else {
				System.out.println("invalid command(move or quit)");
			}
			
		}while(quit==false);
		
		System.out.println("Quitting...");
	}
	
	static void printInitialMessage() {
		System.out.println("----------------------------------");
		System.out.println("    Welcome to Tower of Honai     ");
		System.out.println("    Aim is to move all the discs from 1 to 2");
		System.out.println("----------------------------------");
		System.out.println("Commands");
		System.out.println("\tmove fromDisc toDisc (ex: move 1 3)");
		System.out.println("\tquit");
		
		System.out.println("");
	}
}

