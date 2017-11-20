// fundamental data types: "string", boolean(true/false), 'C' or 8 
/* multi
line
comment */

public class Variables {
    public static void main(String[] args) {
                          // they like whitespace here?
    int myNumber = 42;    // semicolons
    int myNumber = 2 * 5;  // maths is simple
    int mySecondNumber = myNumber / 4; 
    System.out.println(myNumber);  // print is ugly
    System.out.println(2 < 4);  // false. Relational operators can be used in print statement
    System.out.println(2 != 4);  // true
    System.out.println( !(5>=1) ); // false
    System.out.println(2 > 1 && 4 < 6);
    boolean isFun = true; 
    char movieRating ='A'; // specificy var type before assigning var
    int myRemainder = 10 % 4; // =2 % is modulus, i.e. remainder.
  }
}

// loops. 
public class IfElseIf {
	public static void main(String[] args) {

		int round = 2;

		if (round > 12) {

			System.out.println("This won't print");

		} else if (round > 0) {

			System.out.println("This will");

		}	else {

			System.out.println("This won't print.");

		}	
	}
}

// ternary conditional - if/else on "one" line of code
public class Ternary {
	public static void main(String[] args) {
		
		int fuelLevel = 3;

		char canDrive = (fuelLevel > 0) ? 'Y' : 'N'; // so IF fuelLevel > 0, True = Y: False = N
		System.out.println(canDrive);

	}
}

//switch statement. Run code if value = value
public class Switch {
	public static void main(String[] args) {
		
		char switchTest = 'A';

		switch (switchTest) {

			case 'A': System.out.println("Option A was typed");
								break;  //break works same as other languages
			case 'B': System.out.println("blah");
								break;
			case 'C': System.out.println("blah");
								break;
			default:
				System.out.println("your var was neither A, B or C"); // works for integers and prob boolean/strings too

		}

	}
}
