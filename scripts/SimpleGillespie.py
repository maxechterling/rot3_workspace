#!/usr/bin/env python

"""
A simple implementation of the Gillespie algorithm with two possible reactions:
    1) A + B -> AB; Kd
    2) AB -> A + B; Kb

Example:
    Starting concentration of each species is given in uM along with total
    volume of the reaction in um^3 and the rate constants for both reactions.
        $ ./SimpleGillespie.py --A 1 --B 1 --AB 0 --rxnvol 10 --Kd 10 --Kb 10

Attributes:
    --A (int): starting concentration of reactant A in uM
    --B (int): starting concentration of reactant B in uM
    --AB (int): starting concentration of dimer AB in uM
    --rxnvol (int): total volume of the model in um^3
    --Kd (int): rate constant for rxn A + B -> AB
    --Kb (int): rate constant for rxn AB -> A + B
"""

from optparse import OptionParser
import sys

import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(1000000000)

def initialConditions():
    """Read in module arguments to set starting conditions of the system"""
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option("-A", "--A", action="store_const", dest="A", default=.0000001,
                      help="starting concentration of reactant A in uM, default=100")
    parser.add_option("-B", "--B", action="store_const", dest="B", default=.0000001,
                      help="startring concentration of reactant B in uM, default=100")
    parser.add_option("--AB", action="store_const", dest="AB", default=.0000001,
                      help="starting concentration of produce AB in uM, default=0")
    parser.add_option("--rxnvol", action="store_const", dest="rxnvol", default=.001,
                      help="total volume of reaction in um^3, default=10")
    parser.add_option("--Kd", action="store_const", dest="kd", default=.4,
                      help="rate constant for A + B -> AB, default=10")
    parser.add_option("--Kb", action="store_const", dest="kb", default=.4,
                      help="rate constant for AB -> A + B, default=10")
    (options, args) = parser.parse_args()
    return vars(options)
    
class Gillespie(object):
    """Performs one step in the Gillespie algorithm and updates the stepDic
    Two tasks are performed to advance the algorithm:
        1) Determine time to next step
        2) Determine which of potential reactions occurs
    """
    stepDic = {'A':[], 'B':[], 'AB':[], 't':[]}
    avogadro = 6.0221409E+23
    
    def __init__(self, a, b, ab, kd, kb, t, rxnvol):
        # Starting concentrations of all species
        self.a, self.b, self.ab = a, b, ab
        # Rate constants for both rxns
        self.kd, self.kb = kd, kb
        # Time at start of algorithm step
        self.t = t
        # Volume of reaction
        self.rxnvol = rxnvol
        self.mlcA = self.ConvertToMlcs(self.a)
        self.mlcB = self.ConvertToMlcs(self.b)
        self.mlcAB = self.ConvertToMlcs(self.ab)
        #self.mlcKd = 
        #self.mlcKb = 

    def ConvertToMlcs(self, conc):
        """Convert uM to number of molecules"""
        # Units will be coming in as micromolar & um^3, convert to molar & liters
        conc, vol = conc * 10**-6, (self.rxnvol * 10**-15)
        return int( conc * self.rxnvol * self.avogadro )
    
    def ConvertToMolarity(self, mlcs):
        """Convert number of molecules to uM"""
        # vol is in um^3
        return (( mlcs / self.avogadro ) / (self.rxnvol * 10**-15)) * 10**6
    
    def CalculateTimeStep(self, rate):
        """Calculate the time of each step in the Gillespie algorithm
        Calculates the time taken in the current reaction step by choosing randomly
        from an exponential distribution lambda*e^(-lambda*t) with mean (lambda) equal
        to the total rxn rate.
        """
        return np.random.exponential( 1./rate )
        
    def findRates(self):
        """Calculate forward and reverse reaction rates in molecules/s
        """
        a, b, ab = self.a * 10**-6, self.b * 10**-6, self.ab * 10**-6
        fRate, rRate = self.kd * a * b, self.kb*ab
        return fRate * self.rxnvol * self.avogadro, rRate * self.rxnvol * self.avogadro
    
    # def iterator(self, tmax):
    #     """
    #     """
    #     print self.t
    #     fRate, rRate = self.findRates()
    #     # rxnChoice = 0, forward rxn proceeds. rxnChoice = 1, rev rxn proceeds.
    #     rxnChoice = np.random.choice(2, p=[fRate/(fRate+rRate), rRate/(fRate+rRate)])
    #     if rxnChoice == 0:
    #         self.mlcA -= 1
    #         self.mlcB -= 1
    #         self.mlcAB += 1
    #     else:
    #         self.mlcA += 1
    #         self.mlcB += 1
    #         self.mlcAB -= 1
    #     self.t += self.CalculateTimeStep(fRate + rRate)
    #     self.stepDic['A'].append(self.mlcA), self.stepDic['B'].append(self.mlcB),\
    #             self.stepDic['AB'].append(self.mlcAB), self.stepDic['t'].append(self.t)
    #     self.A, self.B, self.AB = self.ConvertToMolarity(self.mlcA), self.ConvertToMolarity(self.mlcB),\
    #                               self.ConvertToMolarity(self.mlcAB)
    #     if self.t <= tmax:
    #         self.iterator(tmax)
    def iterator(self, tmax):
        """
        """
        while True:
            self.stepDic['A'].append(self.mlcA), self.stepDic['B'].append(self.mlcB),\
                    self.stepDic['AB'].append(self.mlcAB)
            #print self.t, self.mlcA, self.mlcAB
            if self.t >= tmax:
                break
            fRate, rRate = self.findRates()
            # rxnChoice = 0, forward rxn proceeds. rxnChoice = 1, rev rxn proceeds.
            print fRate, rRate
            print fRate/(fRate+rRate), rRate/(fRate+rRate)
            rxnChoice = np.random.choice(2, p=[fRate/(fRate+rRate), rRate/(fRate+rRate)])
            if rxnChoice == 0:
                print 'forward'
                self.mlcA -= 1
                self.mlcB -= 1
                self.mlcAB += 1
            else:
                print 'reverse'
                self.mlcA += 1
                self.mlcB += 1
                self.mlcAB -= 1
            self.t += self.CalculateTimeStep(fRate + rRate)  
            
def main():
    initCond = initialConditions()
    g = Gillespie(a=initCond['A'], b=initCond['B'], ab=initCond['AB'], kd=initCond['kd'],
              kb=initCond['kb'], rxnvol=initCond['rxnvol'], t=0)
    g.iterator(.0000001)
    plt.figure()
    plt.plot(g.stepDic['t'], g.stepDic['A'])
    plt.plot(g.stepDic['t'], g.stepDic['AB'])
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()