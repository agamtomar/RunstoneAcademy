


class LogicGate:

    def __init__(self, n):

        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.PerformGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)   # Inheritance from Parent.  BinaryGate "IS-A" LogicGate

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate" + self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate" + self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):

        if self.pinA == None:
            self.pinA = source

        else:
            if self.pinB == None:
                self.pinB = source

            else:
                print("Error: NO EMPTY PINS!")


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)    # Inheritance from Parent.  UnaryGate "IS-A" LogicGate

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate" + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Error: NO EMPTY PINS!")


class AndGate(BinaryGate):

    def __init__(self, n):
        super(AndGate, self).__init__(n)   # Inheritance from parents. AndGate IS-A BinaryGate IS-A LogicGate

    def PerformGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        return a*b


class OrGate(BinaryGate):

    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def PerformGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):

    def __init__(self, n):
        super(NotGate, self).__init__(n)

    def PerformGateLogic(self):

        a = self.getPin()

        if a == 0:
            return 1
        else:
            return 0


class Connector:

    def __init__(self, f_gate, t_gate):
        self.fromgate = f_gate     # Connector class "HAS-A" fromgate and togate
        self.togate = t_gate

        t_gate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


## TODO Write code for NorGate and NandGate
## TODO COmplete Programming exercise 1.17


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())

main()
