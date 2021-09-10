# GitDemo
This is my first repository. It is a software testing demo with pytest framework without reporting assets
In this demo I insert from a user datasheet xlsx file values and implement them in tests impulsive

$ TEST PLAN:<br/>
    1) "I {user[0]} with last name {user[1]} love to {user[3]} {quantity}!"
    2) "{user[0]} {user[1]} is {user[2]} years old!"
    
$ ENTRIES EXAMPLE:
    1) user=["Nikos","Varelas","27","hiking"]
    2) quantity: "a lot", "a little"
    
$ DESIRED OUTCOMES:
    Test 1
      "I Nikos with last name Varelas love to hiking a lot!"
      "I Nikos with last name Varelas love to hiking a little!"
    Test 2
      "Nikos Varelas is 27.0 years old!"

$ UPDATES APPROACH:
    1) MySQL data insertion instead of xlsx
