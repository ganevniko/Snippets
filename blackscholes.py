import math
from scipy.stats import norm
import pandas as pd
from datetime import date
import numpy as np
import datetime
 
# CLASS OPTION  
#===============================================================================
class Option:
    """
    This class will group the different black-shcoles calculations for an opion
    """
    def __init__(self, right, s, k, exp_date, price = None, rf = 0.01, vol = 0.3,
                 div = 0):
        self.k = float(k)
        self.s = float(s)
        self.rf = float(rf)
        self.vol = float(vol)
        self.eval_date = eval_date
        self.exp_date = exp_date
        self.t = self.calculate_t()
        if self.t == 0: self.t = 0.000001 ## Case valuation in expiration date
        self.price = price
        self.right = right   ## 'C' or 'P'
        self.div = div
 
    def calculate_t(self):
        
        return ((datetime.datetime.strptime(self.exp_date, "%Y-%m-%d")-datetime.datetime.now()).days+1)/365

 
    def get_price_delta(self):
        d1 = ( math.log(self.s/self.k) + ( self.rf + self.div + math.pow( self.vol, 2)/2 ) * self.t ) / ( self.vol * math.sqrt(self.t) )
        d2 = d1 - self.vol * math.sqrt(self.t)
        if self.right == 'C':
            self.calc_price = ( norm.cdf(d1) * self.s * math.exp(-self.div*self.t) - norm.cdf(d2) * self.k * math.exp( -self.rf * self.t ) )
            self.delta = norm.cdf(d1)
        elif self.right == 'P':
            self.calc_price =  ( -norm.cdf(-d1) * self.s * math.exp(-self.div*self.t) + norm.cdf(-d2) * self.k * math.exp( -self.rf * self.t ) )
            self.delta = -norm.cdf(-d1) 
 
    def get_call(self):
        d1 = ( math.log(self.s/self.k) + ( self.rf + math.pow( self.vol, 2)/2 ) * self.t ) / ( self.vol * math.sqrt(self.t) )
        d2 = d1 - self.vol * math.sqrt(self.t)
        self.call = ( norm.cdf(d1) * self.s - norm.cdf(d2) * self.k * math.exp( -self.rf * self.t ) )
        #put =  ( -norm.cdf(-d1) * self.s + norm.cdf(-d2) * self.k * math.exp( -self.rf * self.t ) ) 
        self.call_delta = norm.cdf(d1)
 
 
    def get_put(self):
        d1 = ( math.log(self.s/self.k) + ( self.rf + math.pow( self.vol, 2)/2 ) * self.t ) / ( self.vol * math.sqrt(self.t) )
        d2 = d1 - self.vol * math.sqrt(self.t)
        #call = ( norm.cdf(d1) * self.s - norm.cdf(d2) * self.k * math.exp( -self.rf * self.t ) )
        self.put =  ( -norm.cdf(-d1) * self.s + norm.cdf(-d2) * self.k * math.exp( -self.rf * self.t ) )
        self.put_delta = -norm.cdf(-d1) 
 
 
    def get_theta(self, dt = 0.0027777):
        self.t += dt
        self.get_price_delta()
        after_price = self.calc_price
        self.t -= dt
        self.get_price_delta()
        orig_price = self.calc_price
        self.theta = (after_price - orig_price) * (-1)
 
    def get_gamma(self, ds = 0.01):
        self.s += ds
        self.get_price_delta()
        after_delta = self.delta
        self.s -= ds
        self.get_price_delta()
        orig_delta = self.delta
        self.gamma = (after_delta - orig_delta) / ds
 
    def get_all(self):
        self.get_price_delta()
        self.get_theta()
        self.get_gamma()
        return self.calc_price, self.delta, self.theta, self.gamma
 
