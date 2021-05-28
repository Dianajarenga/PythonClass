class Car:
    def __init__(self,make,model,colour,speed):
        self.make=make
        self.model=model
        self.colour=colour
        self.speed=speed

    def virtual_speak(self):
        return f"I am a {self.colour},{self.make} ,{self.model}, my maximum speed is {self.speed} km/hr press start to enjoy ride"  
    def start(self):
        return f" VOOOO...M! I am starting at {self.speed}km/hr "
    def accelerate(self):
        return f"Accelerating from 70 km/hr,to {self.speed}km/hr"
    def decelerate(self):
        return f"Decelerating to 70 km/hr"
    def stop(self):
        return f"3..2..1..speed is 0 km/hr it's safe to step out"

