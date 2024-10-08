# {{PROBLEM}} Class Design Recipe

# Copy this into a `recipe.md` in your project and fill it out.

# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface

# _Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        self.name = name
        self.to_do_list = []
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        

    def remind_me_to(self, task):
        self.to_do_list.append(task)
        

        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
       

    def remind(self):
        if len(self.to_do_list) == 0:
            raise Exception("No tasks set")
        return self.name + "! Remember to: " + ", ".join(self.to_do_list)
      

        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def complete_task(self, task):
        self.to_do_list.remove(task)

# ```

## 3. Create Examples as Tests

# _Make a list of examples of how the class will behave in different situations._

# ``` python
# # EXAMPLE

# """
# Given a name and a task
# #remind reminds the user to do the task
# """
# reminder = Reminder("Kay")
# reminder.remind_me_to("Walk the dog")
# reminder.remind() # => "Walk the dog, Kay!"

# """
# Given a name and no task
# #remind raises an exception
# """
# reminder = Reminder("Kay")
# reminder.remind() # raises an error with the message "No task set."

# """
# Given a name and an empty task
# #remind still reminds the user to do the task, even though it looks odd
# """
# reminder = Reminder("Kay")
# reminder.remind_me_to("")
# reminder.remind() # => ", Kay!"
# ```

# _Encode each example as a test. You can add to the above list as you go._

# ## 4. Implement the Behaviour

# _After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
