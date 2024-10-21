from threading import Thread, Condition
from pynput import mouse, keyboard


class InputManager:
    
    on_key_press_event = []
    on_key_release_event = []
    on_mouse_press_event = []
    on_mouse_release_event = []
    mouse_position = (0,0)
    held_mouse_buttons = set()
    held_keys = set()
    
    def __init__(self, app):
        self.stop_mouse_condition = Condition()
        self.stop_keyboard_condition = Condition()
        Thread(target=self.mouse_listener_thread,args=(app,self.stop_mouse_condition,)).start()
        Thread(target=self.keyboard_listener_thread,args=(app,self.stop_keyboard_condition,)).start()
        pass
    
    def stop(self):
        with self.stop_mouse_condition:
            self.stop_mouse_condition.notify()
            pass
        with self.stop_keyboard_condition:
            self.stop_keyboard_condition.notify()
            pass
        pass
    
    def mouse_listener_thread(app, stop_condition):
        with mouse.Listener(on_move=app.on_mouse_move, on_click=app.on_mouse_click) as listener:
            with stop_condition:
                stop_condition.wait()
                pass
            listener.stop()
            pass
        pass

    def keyboard_listener_thread(app, stop_condition):
        with keyboard.Listener(on_press=app.on_key_press, on_release=app.on_key_release) as listener:
            with stop_condition:
                stop_condition.wait()
                pass
            listener.stop()
            pass
        pass
    
    def on_mouse_move(self, x,y):
        #print(f"{x} {y}")
        InputManager.mouse_position = (x,y)
        pass
    
    def on_mouse_press(self,x,y,button,press_or_release):
        #print(f"{x} {y} {button} {press_or_release}")
        if press_or_release:
            InputManager.held_mouse_buttons.add(button)
            for subscriber in InputManager.on_mouse_press_event:
                try:
                    subscriber((x,y),button,press_or_release)
                except Exception as e:
                    print(f"Error while passing click press event: {e}")
                pass
        else:
            InputManager.held_mouse_buttons.remove(button)
            for subscriber in InputManager.on_mouse_release_event:
                try:
                    subscriber((x,y),button,press_or_release)
                except Exception as e:
                    print(f"Error while passing click release event: {e}")
                pass
        pass
    
    def on_key_release(self, keycode):
        #print(f"released {keycode}")
        InputManager.held_keys.remove(keycode)
        for subscriber in InputManager.on_key_release_event:
            try:
                subscriber(keycode)
            except Exception as e:
                print(f"Error while passing key release event: {e}")
            pass
        pass
    
    def on_key_press(self, keycode):
        #print(f"pressed {keycode}")
        InputManager.held_keys.add(keycode)
        for subscriber in InputManager.on_key_press_event:
            try:
                subscriber(keycode)
            except Exception as e:
                print(f"Error while passing key press event: {e}")
            pass
        pass