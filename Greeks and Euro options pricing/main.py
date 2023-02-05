from scipy.stats import norm
import pandas
import math
import numpy as np

# we will create a class for both a Euro Put and Call
# K is strike price; Price is asset price, R is interest rate,
# and T is time to expiration
class PutOption:
    def PricePut(
     self, K, Volatility, Price, R, T):
        b = math.exp(-R*T)
        x1 = math.log((b*K)/Price)+.5*(Volatility**2)*T
        x1 = x1/(Volatility*(T**.5))
        d1 = norm.cdf(x1)
        d1 = b*K*d1
        x2 = math.log((b*K)/Price)-0.5*(Volatility**2)*T
        x2 = x2/(Volatility*(T**.5))
        d2 = norm.cdf(x2)
        d2 = Price*d2
        return d1-d2
    def PutDelta(
        self, K, Volatility, Price, R, T):
        b = math.exp(-R*T)
        x1 = math.log(Price*(b*K))+.5*(Volatility**2)*T
        x1 = x1/(Volatility*(T**.5))
        d1 = norm.cdf(x1)
        return d1 -1
    def PutGamma(
        self, K, Volatility, Price, R, T):
        b = math.exp(-R*T)
        x1 = math.log(Price/(b*K))+.5*(Volatility**2)*T
        x1 = x1/(Volatility*(T**.5))
        d1 = norm.cdf(x1)
        d2 = d1/(Price*Volatility*math.sqrt(T))
        return d2
    def PutVega(
        self, K, Volatility, Price, R, T):
        b = math.exp(-R*T)
        x1 = math.log(Price/(b*K))+.5*(Volatility**2)*T
        x1 = x1/(Volatility*(T**.5))
        d1 = norm.cdf(x1)
        d2 = Price*d1*math.sqrt(T)
        return d2/100
    def __init__(
        self,K, Volatility, Price, R, T):
        self.K = K
        self.Volatility = Volatility
        self.Price = Price
        self.R = R
        self.T = T
        self.PricePut = self.PricePut(K, Volatility, Price, R, T)
        self.PutDelta = self.PutDelta(K, Volatility, Price, R, T)
        self.PutGamma = self.PutGamma(K, Volatility, Price, R, T)
        self.PutVega = self.PutVega(K, Volatility, Price, R, T)
class CallOption:
    def PriceCall(
        self, K, Volatility, Price, R, T):
        b = math.exp(-R*T)
        x1 = math.log(Price/(b*K))+.5*(Volatility**2)*T
        x1 = x1/(Volatility*(T**.5))
        d1 = norm.cdf(x1)
        d1 = Price*d1
        x2 = math.log(Price/(b*K))-.5*(Volatility**2)*T
        x2 = x2/(Volatility*(T**.5))
        d2 = norm.cdf(x2)
        d2 = b*K*d2
        return d1-d2
    def DeltaCall(
        self, K, Volatility, Price, R, T):
        b = math.exp(-R*T)
        x1 = math.log(Price/(b*K))+.5*(Volatility**2)*T
        x1 = x1/(Volatility*(T**.5))
        d1 =norm.cdf(x1)
        return d1
    def GammaCall(
        self, K, Volatility, Price, R, T):
        b = math.exp(-R*T)
        x1 = math.log(Price/(b*K))+.5*(Volatility**2)*T
        x1 = x1/(Volatility*(T**.5))
        d1 = norm.cdf(x1)
        d2 = d1/(Price*Volatility*math.sqrt(T))
        return d2
    def VegaCall(
        self, K, Volatility, Price,R,  T):
        b = math.exp(-R*T)
        x1 = math.log(Price/(b*K))+.5*(Volatility**2)*T
        x1 = x1/(Volatility*(T**.5))
        d1 = norm.cdf(x1)
        d2 = Price*d1*math.sqrt(T)
        return d2/100
    def __init__(
        self, K, Volatility, Price,R, T):
        self.K = K
        self.Volatility = Volatility
        self.Price = Price
        self.R = R
        self.T = T
        self.PriceCall = self.PriceCall(K, Volatility, Price, R, T)
        self.DeltaCall = self.DeltaCall(K, Volatility, Price, R, T)
        self.GammaCall = self.GammaCall(K, Volatility, Price, R, T)
        self.VegaCall = self.VegaCall(K,Volatility, Price, R, T)

if __name__ == '__main__':
    # Strike = 250
    # Implied Volatility = 0.31
    # Market Price = 245.39
    # Risk free rate = 1.5%
    # Time to expiration = 30/365 approx. 1 mon.
    BoeingOption = PutOption(250, 0.31, 245.39, .015, 30 / 365)
    print(BoeingOption.Price)
    print(BoeingOption.PutDelta)
