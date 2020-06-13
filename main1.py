class Machines:
    def __init__(self, cost):
        self.machines = [(10, 'Large'), (20, 'XLarge'), (40, '2XLarge'), (80, '4XLarge'), (160, '8XLarge'), (320, '10XLarge')]
        if len(cost) == len(self.machines):
            self.preprocess(cost)
    
    def preprocess(self, cost):
        
        for i in range(len(self.machines)):
            self.machines[i] = (*self.machines[i], cost[i])

        cost_per_unit = []
        for machine in self.machines:
            cost_per_unit.append(machine[2]/machine[0])
            # print (machine[2])
            # print (machine[0])
        self.machines = sorted(self.machines, key=lambda machine: machine[2] / machine[0])
        print(self.machines)

def Cost(capacity, hours):
    
    machine_table = {'New York':Machines([120, 230, 450, 774, 1400, 2820]),
    'India':Machines([140, float('inf'), 413, 890, 1300, 2970]),
     'China':Machines([110, 200, float('inf'), 670, 1180, float('inf')])}

    output = []
    for areas in machine_table:
        area_output = {"region":areas}

        area_machine_configuration = machine_table[areas].machines
        cost , machines, required = 0, [], capacity
        for machine in area_machine_configuration:
            if machine[0] <= required:
                num = required // machine[0]
                cost += num * machine[2]
                machines.append((machine[1], num))
                required = required % machine[0]
        area_output["total_cost"] = cost * hours
        area_output["machines"] = machines

        output.append(area_output)
    
    return {
        "OUTPUT":output
    }


print(Cost(1150,1))