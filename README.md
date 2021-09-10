# GitDemo
This is my first repository. It is a software testing demo with pytest framework without reporting assets.<br/>
In this demo I insert from a user datasheet xlsx file values and implement them in tests impulsive.

$ TEST PLAN:<br/>
  * "I {user[0]} with last name {user[1]} love to {user[3]} {quantity}!"<br/>
  * "{user[0]} {user[1]} is {user[2]} years old!"
    
$ ENTRIES EXAMPLE:<br/>
  * user=["Nikos","Varelas","27","hiking"]<br/>
  * quantity: "a lot", "a little"
    
$ DESIRED OUTCOMES:<br/>
  * Test 1<br/>
    * "I **Nikos** with last name **Varelas** love to **hiking** a **lot**!"<br/>
    * "I **Nikos** with last name **Varelas** love to **hiking** a **little**!"<br/>
  * Test 2<br/>
    * "**Nikos** **Varelas** is **27** years old!"

$ UPDATES APPROACH:<br/>
  * MySQL data insertion instead of xlsx
