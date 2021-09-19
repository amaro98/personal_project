<h1>Rock Paper Scissors Game (Osom!)</h1>

Disclaimer: This is one of my early Python project, and there are still plenty of imperfections that need fixes (mentioned in the last part of this Readme)

<h2>Overview</h2>

A simple rock-paper-scissors game which used Tkinter to provide User Interface as shown below: <br><br>
![image](https://user-images.githubusercontent.com/88897287/133916795-a6c2c8fa-ba5a-4207-98ff-90271fb9d860.png) <br>

The result will be shown in the space as shown below:<br><br>
![image](https://user-images.githubusercontent.com/88897287/133916820-42046184-bc52-4d1e-9e92-43d8e2540810.png)





The "computer" opponent will return random selection between Air, Batu or Burung. This is done by creating this function to return random responses: <br>

```
''' AI CHOICE '''

def ran_comp_choice():
    return random.choice(['air','batu','burung'])
```


<h2>Flaws of this project</h2>
  

  * The comment section is still under amendment to make it more readable
  * The Computer opponent returns random response, thus this game is basically a game of luck
  * the score count is still not working
  * the UI sucks (I admit it) :/
