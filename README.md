# Introduction:
The main purpose of this program was for a project my CS230 teacher gave the class. We were meant to create a self-checkout program that fit the picture description we were given. This program requires the user to self input certain values as well. It is possble to be simplified further with dictionary rather than lists. It is something I am currently working on. 

# Methodology
The way this program works starts at the very top. This code block is a return for sales taxes. In a real world scenario, there is a percentage of taxes on a subtotal before given the final total. It has interchangeable values to fitting for many scenarios. ***At least, within the U.S.***
Next, the second code block is used to gather information from the user's inputs to calculate the subtotal. This part will loop as many times required until the counter is equal to the total of items they are purchasing. _This will become important later._

Now the loop is set up, we need to start gathering information for the subtotal. There are two things required in order to get it. The first being the name of the item the user is purchasing and the second being the value of said item. These both are user-inputted from a prompt. The name and price are put in separate lists to be stored. After that, the price gets put in another function in order to be totaled up. When the loop finishes, the lists are printed in a format of **"Name: $ Price"**. It should look something like this.


![Programming Project 3 Results 1 1](https://github.com/trezzytorrinz/Self-Checkout/assets/146397231/5bae3594-b80b-49d5-9be7-422169249d3c)



While the lists are being printed, the subtotal is taken to be multiplied by the percented sales tax chosen. For the project I had to do, it was 9%. So, I took 9% and multiplied it to the subtotal. Whatever gets totaled, it will then be added to the subtotal to get the final total. The program will then ask the user to insert a cash value to pay for the items purchased. There will be two scenarios for this. If the user inputs a value higher than or equal the final total, it will display the cash returned to them ending the program. If the cash value is lower than the final total, it will display "insufficient funds" which also ends the program. 

It will look something like this for the first scenario.

![Programming Project 3 Results 1 2](https://github.com/trezzytorrinz/Self-Checkout/assets/146397231/c2363f7a-df9e-45fb-a03e-464a838e66f3)

It will look something like this for the second scenario.

![Programming Project 3 Results 2](https://github.com/trezzytorrinz/Self-Checkout/assets/146397231/7d425bbb-b06b-466f-97a7-1586ae803a08)






# Results

What makes the results so fascinating is this being the barebones of something larger. There is a lot that can be improved to this program and made significantly simpler than what I have here. There are also some flexibility with what is being displayed to suit other countries as well.


# Conclusion
Building this program has taught me to think of a bunch of ways I could improve this program. For example, I could use dictionaries instead to reduce the formatting needed for the same result. I am still learning to work with them so eventually I will come back to this. It has also taught me ways to handle values in a set seed and ways to display said values to make them look more professional. There is also a possibility of me turning this into a full program where the item name is only needed. It will take time, so this is mostly just my own conjecture. In the end, I have learned a lot and will continue to improve to do better.
