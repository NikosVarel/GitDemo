# GitDemo
This is my first repository. It is a software testing demo with pytest framework without reporting assets
In this demo I insert from a user datasheet xlsx file values and implement them in tests impulsive

$ TEST PLAN:<br/>
    1) "I {user[0]} with last name {user[1]} love to {user[3]} {quantity}!"<br/>
    2) "{user[0]} {user[1]} is {user[2]} years old!"
    
$ ENTRIES EXAMPLE:<br/>
    1) user=["Nikos","Varelas","27","hiking"]<br/>
    2) quantity: "a lot", "a little"
    
$ DESIRED OUTCOMES:<br/>
    Test 1<br/>
      "I Nikos with last name Varelas love to hiking a lot!"<br/>
      "I Nikos with last name Varelas love to hiking a little!"<br/>
    Test 2<br/>
      "Nikos Varelas is 27.0 years old!"

$ UPDATES APPROACH:<br/>
    1) MySQL data insertion instead of xlsx
