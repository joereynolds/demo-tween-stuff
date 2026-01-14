`index.rst` - Go back

========
Tweening
========

The structure of tweens is a bit complicated but only because it needs
flexibility. Here it is:

``Tween`` - The main tween class that manages all the tween objects that belong
to it

``TweenFactory`` - Creates tweens from strings

``TweenRequest`` - Holds all the data a tween needs. We have this so we don't
duplicate constructors everywhere for different tweens.

``ease`` - The easing function(s)

When you're implementing your own new ``Tween``, there are 3 methods you need to implement

``tween_update`` - This gets called once per frame and is the main logic for updating that tween

``tween_reset`` - This gets called when our direction is ``pingpong``. It will reset things back to what they were

``tween_complete`` - This flags the tween as complete. A ``pingpong`` tween will not call this.
